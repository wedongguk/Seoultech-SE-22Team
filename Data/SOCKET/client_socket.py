import socket

HOST = 'localhost'  # 호스트 이름
PORT = 8000  # 포트 번호
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 소켓 객체 생성
client_socket.connect((HOST, PORT))  # 서버에 연결

client_id = input("클라이언트 ID : ")
client_socket.sendall(client_id.encode())  # 서버에 클라이언트 ID 전송

while True:
    data = client_socket.recv(1024)  # 데이터 수신
    if not data:
        break

    # 데이터에 대한 처리 작업 수행
    # ...

    print(f"받은 메세지 : {data.decode()}")

    message = input("메세지 입력 : ")
    if message == "quit":
        data = f"{client_id}:{message}".encode()
        client_socket.sendall(data)  # 데이터 전송
        break
    data = f"{client_id}:{message}".encode()
    client_socket.sendall(data)  # 데이터 전송

client_socket.close()  # 소켓 닫기
