'use strict';

const nodemailer = require('nodemailer');
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

function sendMail() {
    let fromMail;
    let toMail;

    rl.on("line", (input) => {
        console.log("보낼 이메일을 입력하세요")
        input = fromMail;
    })
    .on("line", (input) => {
        console.log("받을 이메일을 입력하세요")
        input = toMail
        console.log(fromMail, toMail);
        process.exit();
    })

}

sendMail();