const { app } = require('@azure/functions');
const nodemailer = require('nodemailer');

app.http('sendEmail', {
    methods: ['POST'],
    authLevel: 'function',
    handler: async (request, context) => {
        const body = await request.json();

        const transporter = nodemailer.createTransport({
            service: 'gmail',
            auth: {
                user: process.env.EMAIL_USER,
                pass: process.env.EMAIL_PASS
            }
        });

        await transporter.sendMail({
            from: process.env.EMAIL_USER,
            to: process.env.EMAIL_TO,
            subject: body.subject || "New message",
            text: body.message || ""
        });

        return { body: "Email sent" };
    }
});
