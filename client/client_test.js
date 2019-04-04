'use strict'

const grpc = require('grpc');
const proto = grpc.load(`${__dirname}/../chatbot.proto`)
const client = new proto.chatbot.ChatbotService('localhost:50051', grpc.credentials.createInsecure())

const req = {
  message: 'TEST'
}

client.getMessage(req, (err, res) => {
  if (err) {
    return console.error(err)
  }
  console.log(res)
})
