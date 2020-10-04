import EzPySockets as es

check = input("Say y to create a server and x to create a client.")
if check == "y":
    port = int(input("What is the port number?\n"))
    es.createserver(1432)
if check == "x":
    port = int(input("What is the port number?\n"))
    es.createclient("localhost", 1432)
