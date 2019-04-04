'use strict'

const grpc = require('grpc');
const proto = grpc.load(`${__dirname}/../chatbot.proto`)
const client = new proto.chatbot.ChatbotService('localhost:50051', grpc.credentials.createInsecure())

const Discord = require('discord.js')
const botConfig = require('./config.json')
const bot = new Discord.Client()

bot.on('ready', () => {

    bot.user.setStatus('online')

    bot.user.setPresence({
        game: {
            name: botConfig.watching,
            type: 'Watching'
        }
    })

})

bot.on('message', message => {

    if (message.author.bot == true) return;

    let req = message.content
    
    client.getMessage(req, (err, res) => {
        if (err) {
            return console.error(err)
        }
        message.channel.send(res.response)
    })

})

bot.login(botConfig.TOKEN)