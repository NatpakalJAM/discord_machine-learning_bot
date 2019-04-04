'use strict'

const grpc = require('grpc');
const proto = grpc.load(`${__dirname}/../chatbot.proto`)
const client = new proto.chatbot.ChatbotService('localhost:50051', grpc.credentials.createInsecure())

const Discord = require('discord.js')
const botConfig = require('./config/config.json')
const command = require('./commands/index.js')
const bot = new Discord.Client()

bot.on('ready', () => {

    bot.user.setStatus('online')

    bot.user.setPresence({
        game: {
            name: '....',
            type: 'Watching'
        }
    })

})

bot.on('message', message => {

    if (message.author.bot == true) return;

    client.getMessage(req, (err, res) => {
        if (err) {
            return console.error(err)
        }
        message.channel.send(res)
        console.log(res)
    })

})

bot.login(botConfig.TOKEN)