import asyncio
from Common import message_queue


class EchoServerClientProtocol(asyncio.Protocol):

    def __init__(self, message_queue):
        self.message_queue = message_queue

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
        loop = asyncio.get_event_loop()
        # Each client connection will create a new protocol instance
        coro = loop.create_server(EchoServerClientProtocol, '127.0.0.1', 8888)
        server = loop.run_until_complete(coro)

        # Serve requests until Ctrl+C is pressed
        print('Serving on {}'.format(server.sockets[0].getsockname()))
        try:
         loop.run_forever()
        except KeyboardInterrupt:
        pass

        # Close the server
        server.close()
        loop.run_until_complete(server.wait_closed())
        loop.close()

