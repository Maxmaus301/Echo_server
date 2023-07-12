import socket

with socket.create_connection(('127.0.0.1', 3999)) as s:
    s.sendall(input().encode('utf-8'))
    answer = s.recv(4096).decode('utf-8')
    print(answer)
