import socket, threading
class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)
    def run(self):
        print ("Conection from : ", clientAddress)
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        mensage = ''
        while True:
            data = self.csocket.recv(2048)
            mensage = data.decode()
            text = mensage.split(": ", 1)
            if text[1] == 'quit':
             break
            print ("Client mensage ", mensage)
            self.csocket.send(bytes(mensage,'UTF-8'))
        print ("Client ", text[0] , " disconnected..")
LOCALHOST = "localhost"
PORT = 4444
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server connected  ")
print("Waiting requests..")
while True:
    server.listen()
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()