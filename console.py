#!/usr/bin/python3
"""
Entry point of the command interpreter.
"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    class cmd -> hbnb
    """
    prompt = "(hbnb) "

    classes_list = ["BaseModel"]

    def do_EOF(self, arg):
        """
        Exit if EOF happens
        """
        print()
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

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, sabes it to tje JSON file and
        prints the "id".
        Use of method "eval" to create an instance of the correct class if it
        is in the list of the class attribute: "classes_list".
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
        else:
            # create a new instance of one of the models in the list
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
