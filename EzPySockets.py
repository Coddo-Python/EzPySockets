import socket
import os.path
from os import path
try:
    import EzPySocketsConfig as config
except:
    with open('EzSocketsConfig.py', 'w') as f:
        print("EzSocketsConfig.py Created!")
        import EzPySocketsConfig as config

global debugStatus

debugStatus = True

print("Made Using:")
print("███████╗███████╗██████╗░██╗░░░██╗░██████╗░█████╗░░█████╗░██╗░░██╗███████╗████████╗░██████╗")
print("██╔════╝╚════██║██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗██╔══██╗██║░██╔╝██╔════╝╚══██╔══╝██╔════╝")
print("█████╗░░░░███╔═╝██████╔╝░╚████╔╝░╚█████╗░██║░░██║██║░░╚═╝█████═╝░█████╗░░░░░██║░░░╚█████╗░")
print("██╔══╝░░██╔══╝░░██╔═══╝░░░╚██╔╝░░░╚═══██╗██║░░██║██║░░██╗██╔═██╗░██╔══╝░░░░░██║░░░░╚═══██╗")
print("███████╗███████╗██║░░░░░░░░██║░░░██████╔╝╚█████╔╝╚█████╔╝██║░╚██╗███████╗░░░██║░░░██████╔╝")
print("╚══════╝╚══════╝╚═╝░░░░░░░░╚═╝░░░╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═════╝░")

def log(message):
    if debugStatus:
        print(message)

def enabledebug():
    debugStatus = True

def createserver(port, advanced):
    try:
        tempServerCreationData = bool(advanced)
    except:
        print("The advanced argument value is either not a boolean, or empty!")
        print("The advanced argument will allow further control over your socket.")
        try:
            if input("Would you like to continue learning about the 'advanced' argument? y / n\n").lower() == 'y':
                print("") #TBD
        except:
            print("Edit your code and try again!")
            return
    with open('EzSocketsConfig.py', 'r') as f:
        tempServerCreationData = f.readline()
        tempServerCreationData = tempServerCreationData
    if tempServerCreationData != "def onserverrecieve(message, socket, clientsocket):":
        with open('EzSocketsConfig.py', 'w') as f:
            f.write('def onserverrecieve(message):\n    if message != ''\n    print(f"Recieved: {message}")')
    log("Remember to write code in a function called onserverrecieve() located in your EzSocketsConfig.py file")
    log("Note: This server first sends a Heartbeat and awaits ack to confirm the Connection")
    log("Server Starting")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), port))
    log("Basic Server Startup Complete")
    s.listen(5)
    clientsocket, address = s.accept()
    while True:
        print(f"Connection Recieved From {address}\nHeartbeat Sent")
        clientsocket.send(bytes("Heartbeat","utf-8"))
        while True:
            data = clientsocket.recv(1024)
            if data.decode("utf-8") == "ack":
                print("Heartbeat Successfully Acked")
                break
        while True:
            data = clientsocket.recv(1024)
            config.onserverrecieve(data.decode("utf-8"), s, clientsocket)

def createclient(ip, port):
    if ip == "localhost":
        ip = socket.gethostname()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    data = s.recv(1024)
    print(data.decode("utf-8"))
    s.send(bytes("ack", "utf-8"))
    print("Ack Sent")
