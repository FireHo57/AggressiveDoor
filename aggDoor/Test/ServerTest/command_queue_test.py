import command_queue as c
__author__ ='charlie'


def main():
    my_commands = c.command_queue()
    my_commands.add_to_queue('GO')
    my_commands.add_to_queue('COMGO')
    my_commands.add_to_queue('COM2GO')
    my_commands.add_to_queue('COM3GO')
    my_commands.add_to_queue('ENDLIST')

    print("Command List: ")

    for i in my_commands.get_queue():
        print(i)

    print('Deleting list..')
    my_commands.empty_queue()

if __name__ == '__main__':
    main()    
