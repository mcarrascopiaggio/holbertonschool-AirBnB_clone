#!/usr/bin/python3
"""
Entry point of the command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    class cmd -> hbnb
    """
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """
        Exit if EOF happens
        """
        return True

    def do_quit(self, arg):
        """
        Exit if quit command is typed
        """
        return True

    def emptyline(self):
        """
        If empty line --> do nothing.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
