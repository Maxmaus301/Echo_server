import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(4096).strip().decode('utf-8')
        print(f'Пользователь с ip {self.client_address[0]} написал: {self.data}')
        self.request.sendall(self.data.upper().encode('utf-8'))

if __name__ == "__main__":
    HOST, PORT = "localhost", 3999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()