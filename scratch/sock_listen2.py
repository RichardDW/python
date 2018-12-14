import SocketServer
class MyHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        while 1:
            dataReceived = self.request.recv(1024)
            if not dataReceived: break
            self.request.send(dataReceived)
myServer = SocketServer.TCPServer(('',8881), MyHandler)
myServer.serve_forever(  )
