from twisted.internet import reactor, protocol
from twisted.internet.protocol import ClientFactory, Protocol
port = 9090
class ClientChat(Protocol):
     def connectionMade(self):
         login = input('Enter your  login;')
         fio = input('Enter your  FIO:')
         addres = input ( ' Enter  your  address:')
         data = (login + fio+addres).encode('utf-8')
         self.transport.write(data)

     def dataReceived(self, data: str):
         print(data)
         self.connectionMade()

class ClientChatFactory(ClientFactory):
    def startedConnecting(self, connector):
        print('connected')
    def buildProtocol(self, addr):
         return ClientChat()
    def clientConnectionFailed(self, connector, reason):
        print('ConnectionFailed, reason:', reason)
        reactor.stop()
    def clientConnectionLost(self, connector, reason):
        print('ConnectionLost, reason:', reason)
        connector.connect()
reactor.connectTCP('localhost',port, ClientChatFactory())
reactor.run()
