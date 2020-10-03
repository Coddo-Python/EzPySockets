import socket
import os.path
from os import path
try:
    import EzSocketsConfig as config
except:
    with open('EzSocketsConfig.py', 'w') as f:
        print("EzSocketsConfig.py Created!")
        import EzSocketsConfig as config

global debugStatus

debugStatus = True

def log(message):
    if debugStatus:
        print(message)

def enabledebug():
    debugStatus = True

def createserver(port):
    with open('EzSocketsConfig.py', 'r') as f:
        tempServerCreationData = f.readline()
        tempServerCreationData = tempServerCreationData
    if tempServerCreationData != "def onserverrecieve(message):":
        with open('EzSocketsConfig.py', 'w') as f:
            f.write('def onserverrecieve(message):\n  print(f"Recieved: {message}")')
    log("Remember to write code in a function called onserverrecieve() located in your EzSocketsConfig.py file")
    log("Note: This server first sends a Heartbeat and awaits ack to confirm the Connection")
    log("Server Starting")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), port))
    log("Basic Server Startup Complete")
    s.listen(5)
    clientsocket, address = s.accept()
    while True:
        clientsocket.send(bytes("Heartbeat","utf-8"))
        while True:
            data = conn.recv(1024)
            if data.decode("utf-8") == "ack":
                print("Heartbeat Successfully Acked")
                break
        while True:
            data = conn.recv(1024)
            config.onserverrecieve(data.decode("utf-8"))

def createclient(port):
    print("Test")
