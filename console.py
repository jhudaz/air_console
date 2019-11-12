#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Command example"""


    prompt = '(hbnb) '

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        exit()
        return True

    def emptyline(self):
        pass

    def help_EOF(self):
        print('EOF signal to interrupt a file')

    def help_quit(self):
        print('Quit command to exit the program\n')

if __name__ == '__main__':
    HBNBCommand().cmdloop()

