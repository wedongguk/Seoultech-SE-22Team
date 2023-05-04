import socket
from _thread import *
import sys
from player_t import Player
import pickle

server = "10.16.144.212"
port = 5555

#소켓 생성
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 소켓 바인딩
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# 소켓 리스닝
s.listen(2)
print("Waiting for a connection, Server Started")

players = [Player(0,0,50,50,(255,0,0)), Player(100,100,50,50,(0,0,255))]

# 특정 플레이어에게 정보 전달을 위함
def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            # String 값 데이터 decode
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    # player가 1 이면 pos 0의 위치를 보냄
                    reply = players[0]
                else:
                    # player가 2 이면 pos 1의 위치를 보냄
                    reply = players[1]

                # data는 받은 데이터
                print("Received: ", data)
                # reply는 보내는 데이터
                print("Sending : ", reply)

            # send 보냄
            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()
    sys.exit()

# 현재 플레이어를 계속 추적하기 위함
currentPlayer = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
    print(currentPlayer)