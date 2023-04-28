from _thread import *
import json
import socket
import time

class socketClient():

    HOST = "127.0.0.1"
    PORT = 9999
    json_object = {
        "state" : "change",
        "ticker" : "BTC",
        "buylimit" : 2000
    }

    def __init__(self):
        super().__init__()
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.HOST, self.PORT))
        self.alive = True
    
    def client_run(self):
        start_new_thread(self.recv_data, (self.client_socket,))
        print("서버와 연결")

        while self.alive:
            print("json : ", self.json_object)
            json_string = json.dumps(self.json_object)
            self.client_socket.send(json_string.encode())
            message = input()
            dic_message = {"클라이언트 메세지" : message}
            json_message = json.dumps(dic_message)
            self.client_socket.send(json_message.encode())
            time.sleep(3)
        self.client_socket.close()
    
    def recv_data(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024)
                print("recive : ", repr(data.decode()))
            except ConnectionResetError as ex:
                break
            except Exception as ex:
                print(ex)
        self.alive = False

client = socketClient()
client.client_run()
