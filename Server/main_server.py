from Communications import TCPServer
from Common import message_queue
import asyncio
import datetime


def main():
    # set up the main server for running
    my_queue = MessageQueue

    server = TCPServer(myQueue)

    # main game loop

    server.run()
    while True:
        now = datetime.datetime.now()

        # get messages received and print them?






if __name__ == "__main__":
	main()