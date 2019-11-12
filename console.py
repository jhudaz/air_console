#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
base = BaseModel()


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

    def do_create(self, line):
        if line is "":
            print('** class name missing **')
        elif line != 'BaseModel':
            print('** class doesn\'t exist **')
        else:
            self.line = base
            print(base.id)

    def do_show(self, line):
        linea = line.split(' ')
        if len(linea) < 1:
            print('** instance id missing **')
        if linea[0] is "":
            print('** class name missing **')
        if linea[0] != 'BaseModel':
            print('** class doesn\'t exist **')
        if len(linea) < 1:
            print('** instance id missing **')
        if len(linea) < 2:
            print('** no instance found **')
        else:
            print(base)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
