from collections import deque
_author__ = "Charlie"


class command_queue:
    def __init__(self):
        self.commands=[]

    def add_to_queue(self,command):
        self.commands.append(commmand)
        return "Appended "+command

    def get_queue(self):
        return self.commands

    def empty_queue(self):
        print("Deleting...\n")
        for com in self.commands:
            print(com)
        self.commands=[]


