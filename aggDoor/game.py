from Server import Server as s
import asyncio
__author__='charlie'


class Game:
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        server = s.ChatServer("Test Server", 4455, self.loop )

    def run(self):
        try:
            self.loop.run_forever()
        finally:
            self.loop.close()
            

def main():
    g = Game()
    g.run()



if __name__ == '__main__':
    main()

