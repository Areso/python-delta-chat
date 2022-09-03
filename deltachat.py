from flask import Flask, jsonify, make_response
from flask import request
import json
import time
import math

deltachat_srv = Flask(__name__)

messages = []


@deltachat_srv.route('/post_message', methods=['OPTIONS', 'POST'])
def post_message():
    reqdata = request.get_data()
    reqdata = reqdata.decode()
    msg_obj = json.loads(reqdata)
    print(msg_obj)
    msg = {"msg": msg_obj["msg"], "timestamp": time.time()}
    messages.append(msg)
    print(messages)
    return "OK"


@deltachat_srv.route('/get_messages', methods=['OPTIONS', 'POST'])
def get_messages():
    reqdata = request.get_data()
    reqdata = reqdata.decode()
    last_msg = json.loads(reqdata)
    last_id = last_msg["timestamp"]
    msgs_for_user = []
    for msg in messages:
        if msg["timestamp"] > last_id:
            msgs_for_user.append(msg)
    return msgs_for_user


if __name__ == '__main__':
    print("start")