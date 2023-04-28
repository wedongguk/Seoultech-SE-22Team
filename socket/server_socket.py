import socket
import threading
import sys

HOST = 'localhost'  # 호스트 이름
PORT = 8000  # 포트 번호
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 소켓 객체 생성
server_socket.bind((HOST, PORT))  # 소켓 바인딩
server_socket.listen()  # 연결 대기

print(f"{PORT} 번 포트 연결 대기 중")

clients = {}  # 클라이언트 식별자와 소켓 정보를 저장할 딕셔너리

def shutdown_server(client_id):
    del clients[client_id]  # 클라이언트 정보 삭제
    print(f"Connection closed by {addr}, client ID: {client_id}")
    
    # global server_socket
    # for client_conn in clients.values():
    #     client_conn.close()
    server_socket.close()
    sys.exit()
    

def handle_client(conn, addr):
    client_id = conn.recv(1024).decode()  # 클라이언트 식별자 수신
    clients[client_id] = conn  # 클라이언트 정보 저장
    try:
        while True:
            server_id = "서버"
            for client in clients:  # 모든 클라이언트에게 데이터 전송
                message = input("보낼 메시지: ")
                data = f"{server_id}:{message}".encode()
                client_conn = clients[client]
                client_conn.sendall(data) # 데이터 전송

            data = conn.recv(1024)  # 데이터 수신
            
            if data.decode().split(":")[1] == "quit":
                break

            client_id, message = data.decode().split(":")  # 클라이언트 식별자와 메시지 분리
            # 서버쪽의 표시 부분
            print(f"클라이언트 {client_id} 의 메세지 : {message}")

            # 데이터에 대한 처리 작업 수행
            # ...
            
            # 데이터를 다른 클라이언트에게 보내주는 부분이 필요

            for client in clients:  # 모든 클라이언트에게 데이터 전송
                if client != client_id:  # 자신을 제외한 모든 클라이언트에게 전송
                    client_conn = clients[client]
                    client_conn.sendall(data)
                    
            
            command = input("y를 누르면 멈춥니다 ")
            if command == "y":
                shutdown_server(client_id)
            else:
                continue
    except ConnectionResetError:
        del clients[client_id]  # 클라이언트 정보 삭제
        print(f"Connection closed by {addr}, client ID: {client_id}")


while True:
    if server_socket.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR) == 0:
        print(server_socket.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR))
        conn, addr = server_socket.accept()  # 클라이언트의 요청 수락
        print(f"{addr} 번 연결 됨")
        # n = int(input())

        # for _ in range(n):
        #     client_id = conn.recv(1024).decode()  # 클라이언트 식별자 수신
        #     clients[client_id] = conn  # 클라이언트 정보 저장

        
        # 새 클라이언트를 위한 쓰레드 생성
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.daemon = True
        thread.start()
    else:
        break
