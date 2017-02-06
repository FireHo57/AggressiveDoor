import asyncio
from aggDoor.Common import message_queue
from aggDoor.Client.Communications import TCPClient as cC


class TCPServer(asyncio.Protocol):

    def __init__(self, message_queue):
        self.message_queue = message_queue
        print("I'm all made up!")

    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        message_queue.add_command( message )

        print('Data received: {!r}'.format(message))

        print('Send: {!r}'.format(message))
        self.transport.write(data)

        print('Close the client socket')
        self.transport.close()

    def run(self):
        self.loop = asyncio.get_event_loop()
        # Each client connection will create a new protocol instance
        coro = loop.create_server(cC.TCPClient, '127.0.0.1', 8888)
        self.server = loop.run_until_complete(coro)

        # Serve requests until Ctrl+C is pressed
        print('Serving on {}'.format(self.server.sockets[0].getsockname()))
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            pass

    def close(self):
        self.server.close()
        self.loop.run_until_complete(self.server.wait_closed())
        self.loop.close()

