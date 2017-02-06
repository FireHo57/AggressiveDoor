

class MessageQueue(object):

    self.commands = []

    def add_command(self , command):
        self.commands.append( command )

    def get_commands(self):
        current_commands = self.commands
        self.commands = []
        return current_commands
