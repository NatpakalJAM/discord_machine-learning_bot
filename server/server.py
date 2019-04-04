from concurrent import futures
import time
import logging

import grpc

import chatbot_pb2
import chatbot_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class ChatbotService(chatbot_pb2_grpc.ChatbotServiceServicer):

    def GetMessage(self, request, context):
        return chatbot_pb2.ChatBotResponse(response='%s' % request.message)


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
