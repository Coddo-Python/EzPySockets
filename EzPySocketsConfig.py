def onserverrecieve(message, socket, clientsocket):
    if message != '':
        print(f"Recieved: {message}")
