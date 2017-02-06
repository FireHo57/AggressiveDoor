from Communications import TCPServer as TCP
from aggDoor.Common import message_queue as mq

import datetime


def main():
    # set up the main server for running
    my_queue = mq.MessageQueue()

    server = TCP.TCPServer(my_queue)

    # main game loop

    while True:
        now = datetime.datetime.now()

        # get messages received and print them?






if __name__ == "__main__":
	main()