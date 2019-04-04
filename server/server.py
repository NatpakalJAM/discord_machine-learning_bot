#!/usr/bin/env python
# -*- coding: utf-8 -*-

from concurrent import futures
import time
import logging

import grpc

import chatbot_pb2
import chatbot_pb2_grpc

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


chatbot = ChatBot(
    'ChatBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database='ChatBot.sqlite3',
    read_only=True
)

chatbot.set_trainer(ChatterBotCorpusTrainer)
# chatbot.train(
#     './server/data/thai/',
#     './server/data/english/',
#     './server/data/japanese/'
# )


class ChatbotService(chatbot_pb2_grpc.ChatbotServiceServicer):

    def GetMessage(self, request, context):
        user_input = request.message
        bot_response = chatbot.get_response(user_input)
        # return chatbot_pb2.ChatBotResponse(response='%s' % bot_response)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chatbot_pb2_grpc.add_ChatbotServiceServicer_to_server(
        ChatbotService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()
