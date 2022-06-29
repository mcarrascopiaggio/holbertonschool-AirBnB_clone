#!/usr/bin/python3
"""
Entry point of the command interpreter.
"""
import cmd
from models import storage  # import storage instance inside the __init__ file
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

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class
        name and id.
        """
        split_arg = arg.split()  # use of split() method to parse "arg"

        if not split_arg:
            print("** class name missing **")
        elif split_arg[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
        elif len(split_arg) == 1:  # if len is 1, is because the id is missing
            print("** instance id missing **")
        else:
            key = f"{split_arg[0]}.{split_arg[1]}"  # generate key: class.id
            # save in variable "aux_dict" result of __objects
            aux_dict = storage.all()
            if key in aux_dict:
                print(aux_dict[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        split_arg = arg.split()  # use of split() method to parse "arg"

        if not split_arg:
            print("** class name missing **")
        elif split_arg[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
        elif len(split_arg) == 1:  # if len is 1, is because the id is missing
            print("** instance id missing **")
        else:
            key = f"{split_arg[0]}.{split_arg[1]}"  # generate key: class.id
            # save in variable "aux_dict" result of __objects
            aux_dict = storage.all()
            if key in aux_dict:
                aux_dict.pop(key)  # use of pop method to remove the chosen key
                storage.save()  # save changes into the storage in: file.json
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not
        on the class name.
        """
        split_arg = arg.split()  # use of split() method to parse "arg"
        # save return of all() method in aux_dict to be able iterate it
        aux_dict = storage.all()
        # create an empty list,this is the format of the example in main task 7
        aux_list = []

        if len(split_arg) == 0:  # esto es para el caso de solo manda "all"
            for key, value in aux_dict.items():
                aux_list.append(value)  # load data into aux_list
            print(aux_list)  # print info with the list format
        elif split_arg[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
        else:  # esto es para el caso que se pasa: all <class name>
            for key, value in aux_dict.items():
                if arg[0] in key:
                    aux_list.append(value)
            print(aux_list)


if __name__ == '__main__':
    HBNBCommand().cmdloop()