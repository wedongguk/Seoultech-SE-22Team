import socket
from _thread import *
import sys

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

# position 읽기
def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

# position 만들기
def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

# position 초기화
# pos[0]은 첫번째 player 위치
# pos[1]은 두번째 player 위치
# pos는 모든 플레이어의 위치 정보를 가지고 있음

pos = [(0,0),(150,150)]

# 특정 플레이어에게 정보 전달을 위함
def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            # String 값 데이터 decode
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    # player가 1 이면 pos 0의 위치를 보냄
                    reply = pos[0]
                else:
                    # player가 2 이면 pos 1의 위치를 보냄
                    reply = pos[1]

                # data는 받은 데이터
                print("Received: ", data)
                # reply는 보내는 데이터
                print("Sending : ", reply)

            # send 보냄
            conn.sendall(str.encode(make_pos(reply)))
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