import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import threading
import time

site = input("naver or google : ")
toMail = input("전송할 이메일 주소를 입력하세요 : ")
title = input("메일 제목을 입력하세요 : ")
content = input("내용을 입력하세요 : ")
count = input("횟수를 입력하세요 : ")
timeout = input("끝낼 시을 입력하세요 (초단위) : ")
mail_count = 0


# gmail 계정
def google_mail():
    global mail_count
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    # 구글 이메일, 구글 앱 비밀번호 (변경할 때)
    smtp.login("khy3231@gmail.com", "구글 앱 비밀번호, read me 블로그 참조")

    msg = MIMEMultipart()
    msg['Subject'] = title
    part = MIMEText(content)
    msg.attach(part)

    # 위에서 사용한 구글 이메일
    smtp.sendmail("khy3231@gmail.com", toMail, msg.as_string())
    google_macro = threading.Timer(int(timeout) / int(count), google_mail)
    google_macro.start()
    mail_count += 1
    print(mail_count)
    if mail_count == int(count):
        google_macro.cancel()
        mail_count = 0
        print(toMail + " 로 " + timeout + " 초 동안 " + count + " 개의 메일 보내기 완료했습니다!")


# naver 계정
def naver_mail():
    global mail_count

    # 네이버 이메일
    fromMail = "dnflwlq3231@naver.com"
    smtp = smtplib.SMTP('smtp.naver.com', 587)
    smtp.ehlo()
    smtp.starttls()
    # 네이버 아이디 (@naver.com 앞부분 만 쓰면 됩니다), 네이버 비밀번호
    smtp.login("dnflwlq3231", "네이버 게정 비밀번호")

    msg = MIMEMultipart()
    msg['Subject'] = title
    msg['To'] = toMail
    msg['From'] = fromMail
    part = MIMEText(content)
    msg.attach(part)

    smtp.sendmail(fromMail, toMail, msg.as_string())
    naver_macro = threading.Timer(int(timeout) / int(count), naver_mail)
    naver_macro.start()
    mail_count += 1
    print(mail_count)
    if mail_count ==  int(count):
        naver_macro.cancel()
        mail_count = 0
        print(toMail + " 로 " + timeout + " 초 동안 " + count + " 개의 메일 보내기 완료했습니다!")


if site == "naver":
    naver_mail()
else:
    google_mail()
