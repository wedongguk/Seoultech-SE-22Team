import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "10.16.144.212"
        self.port = 5555
        self.addr = (self.server, self.port)
        # connect 여부를 확인하고 connect를 통해 pos정보를 전달 받음
        self.pos = self.connect()

    def getPos(self):
        return self.pos

    def connect(self):
        try:
            # 클라이언트 연결이 되면
            self.client.connect(self.addr)
            # 클라리언트로부터 메세지를 받는다
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)