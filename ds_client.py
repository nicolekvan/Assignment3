# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Nicole Kwan
# nkwan3@uci.edu
# 76647093
import socket
import json
import time
from ds_protocol import extract_json

def send(server:str, port:int, username:str, password:str, message:str, bio:str=None):
    pass

def join_server(server, port, username, password):
    data = {
        "join": {
            "username": username,
            "password": password,
            "token": ""
        }
    }

    # formats as json string
    json_message = json.dumps(data)

    with socket.socker(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((server, port))

        send = client.makefile('w')
        recv = client.makefile('r')

        send.write(json_message + '\r\n')
        send.flush()

        response = recv.readline()
        get_data = extract_json(response)

        print(get_data.message)

    return get_data
    