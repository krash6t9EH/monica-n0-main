const express = require('express');
const { EmailClient } = require("@azure/communication-email");
const app = express();
app.use(express.json());

const connectionString = "PASTE_YOUR_AZURE_CONNECTION_STRING_HERE";
const client = new EmailClient(connectionString);

app.post('/api/send-email', async (req, res) => {
    const { name, email, message } = req.body;
    
    const emailMessage = {
        senderAddress: "michael@digamoni.ca",
        content: {
            subject: "Monica Project Demo Request",
            plainText: `Name: ${name}\nEmail: ${email}\n\nMessage: ${message}`,
        },
        recipients: { to: [{ address: "michael@digamoni.ca" }] },
    };

    try {
        const poller = await client.beginSend(emailMessage);
        await poller.pollUntilDone();
        res.status(200).send("Email Sent");
    } catch (err) {
        res.status(500).send("Azure Error");
    }
});

app.listen(3000, () => console.log('Monica Server Running on Port 3000'));
