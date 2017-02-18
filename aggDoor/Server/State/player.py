from  .command_queue import command_queue as c
__author__ = 'charlie'


class player:
    
    def __init__(self,username):
        self.username = username
        self.commands = c()

    def get_name(self):
        return self.username

    # I could write accessor functions for all the methods off of
    # command_queue but it's simpler to just expose the object
    def get_commands(self):
        return self.commands

