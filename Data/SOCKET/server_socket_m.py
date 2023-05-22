import socket
from _thread import *
import os
import sys
sys.path.append(r'C:\Users\jongh\소공\SE-22Team')
sys.path.append(r'{}'.format(os.getcwd()))
import time

import pickle


def start_server(pw):
    server = "10.50.99.56"
    port = 5555
    password = pw

    #소켓 생성
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 소켓 바인딩
    try:
        s.bind((server, port))
    except socket.error as e:
        str(e)

    # 소켓 리스닝
    s.listen(5)
    print("Waiting for a connection, Server Started")

    from Data.GAME_LOGIC.uno_Player import Player
    players = [Player("cli1", True), Player("cli2", True)]
    
    # 입출력 테스트를 위한 샘플 handlist 1번, 2 번
    players[0].handCardList = ["1번 플레이어 카드리스트"]
    players[1].handCardList = ["2번 플레이어 카드리스트"]
    print("players handlist init")

    # 이 부분과 player 부분이 관련있음
    currentPlayer = 0

    while True:
        # 클라이언트가 접속 요청시 accept 함수를 통해 연결 수락
        conn, addr = s.accept()
        print("연결됨 : ", addr)

        start_new_thread(threaded_client, (conn, currentPlayer, players))
        currentPlayer += 1
        print(currentPlayer)


def threaded_client(socket_queue, conn, player, players):
    conn.send(pickle.dumps(players[player]))
    reply = ""

    while True:
        try:
            time.sleep(3)
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            socket_queue.put(data)
            print(data)

            if not data:
                print("연결불가")
                break
            else:
                if player == 1:
                    reply = players[0]
                elif player == 0:
                    reply = players[1]
            
            print()
            print("=======================================================")
            print("{0} 번 플레이어가 받은 카드 리스트 : {1}".format(player+1, data.handCardList))
            print("{0} 번 플레이어가 보낸 카드 리스트 : {1}".format(player+1, reply.handCardList))
            print("=======================================================")
            print()
            conn.sendall(pickle.dumps(reply))
    
        except:
            break
    
    print("연결 종료")
    conn.close()
    sys.exit()


