#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
base = BaseModel()


class HBNBCommand(cmd.Cmd):
    """Command example"""
    

    list_t = list()
    prompt = '(hbnb) '
    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        exit()
        return True

    def emptyline(self):
        pass

    def help_EOF(self):
        print('EOF signal to interrupt a file\n')

    def help_quit(self):
        print('Quit command to exit the program\n')

    def help_create(self):
        print('Create a new instance of BaseModel\n')

    def help_show(self):
        print('Print the string representation\n')
    def do_create(self, line):
        if line is "":
            print('** class name missing **')
        elif line != 'BaseModel':
            print('** class doesn\'t exist **')
        else:
            self.list_t = base
            print(self.list_t.id)

    def do_show(self, line):
        linea = line.split(' ')
        if len(linea) < 1:
            print('** instance id missing **')
        elif linea[0] is "":
            print('** class name missing **')
        elif linea[0] != 'BaseModel':
            print('** class doesn\'t exist **')
        elif len(linea) < 2:
            print('** instance id missing **')
        elif not self.list_t:
            print('** no instance found **')
        elif linea[1] != self.list_t.id:
            print('** no instance found **')
        else:
            print(self.list_t)

    def do_destroy(self, line):
        linea = line.split(' ')
        ide = base.id
        if linea[0] is "":
            print('** class name missing **')
        elif linea[0] != 'BaseModel':
            print('** class doesn\'t exist')
        elif len(linea) < 1:
            print('** instance id missing **')
        elif linea[1] != ide:
            print('** no instance found **')
        else:
            del self.list_t

    def do_all(self, line):
        linea = line.split()
        if linea[0] != 'BaseModel':
            print('** class doesn\'t exist **')
        else:
            print('{}'.format(str(self.list_t)))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
