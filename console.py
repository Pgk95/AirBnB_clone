#!/usr/bin/python3
"""This module is for the entry point of the console. """

import cmd


class HBNBCommand(cmd.Cmd):
    """The entry point of the commnad line"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to close or exit the program """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Empty line handler"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
