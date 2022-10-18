const express = require('express');
const axios = require('axios');;
const app = express();

const PORT = process.env.PORT || 8080;

app.use(express.json());

require('dotenv').config();

const accountSid = process.env.TWILIO_ACCOUNT_SID;
const authToken = process.env.TWILIO_AUTH_TOKEN;
const from = process.env.FROM;

const client = require('twilio')(accountSid, authToken);

app.get('/', (req, res) => {
    res.send({
        'message': 'Hello! Welcome to the Weapon Detection alert server API. Here, requests will be sent to send out SMS alerts to clients if a weapon is detected and the client has requested to receive alerts. Developed by Ethan Hamilton, 2021-2022.',
        'from': process.env.FROM
    });
});

app.post('/alert', (req, res) => {
    const { to } = req.body;
    const { timestamp } = req.body;
    client.messages
        .create({
            body: `A weapon was detected at ${timestamp}`,
            from: from,
            to: to
        })
        .then(res.send({'message':`The alert was sent to ${to} at ${timestamp}`}));
    
});

app.listen(PORT, () => {
    console.log(`Server is listening on PORT ${PORT}`);
});