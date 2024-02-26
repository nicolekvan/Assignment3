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
    