import socket
import threading
import os

HOST = 'localhost'
PORT = 9009

def rcvMsg(sock):
   while True:
      try:
         data = sock.recv(1024)
         if not data:
            break
         print(data.decode())
      except:
         pass

def runChat():
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      sock.connect((HOST, PORT))
      t = threading.Thread(target=rcvMsg, args=(sock,))
      t.daemon = True
      t.start()
    #   print('thread id', threading.get_native_id())
      print('process id', os.getpid())

      while True:
         msg = input()
         if msg == '/quit':
            sock.send(msg.encode())
            break

         sock.send(msg.encode())
            

