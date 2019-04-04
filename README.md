
# Discord Machine-Learning Bot

> This is machine learning, conversational dialog engine for Discord chat bots.

## Setup environment

1. Install [Python](https://www.python.org/downloads/) and [Node.js](https://nodejs.org/en/download/)

2. Install python package

```
$ pip install -r requirements.txt
$ python -m grpc_tools.protoc --proto_path=. ./chatbot.proto --python_out=./server/ --grpc_python_out=./server/
```

3. Install Node.js package

```
$ npm install
```

4. Run ChatBot server

```

$ python server/server.py
```

5. Run ChatBot Discord client

```
$ node client/client.js
```