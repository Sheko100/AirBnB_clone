#!/usr/bin/python3
"""Module for a command line interpreter entry point"""

import cmd
import importlib
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class that defines a command line interpreter

    Attributes:
        prompt (str): a custom prompt
    """

    prompt = "(hbnb) "
    modules = {"BaseModel": "base_model"}
    objects = storage.all()

    def do_EOF(self, arg_str):
        """EOF: Terminates the command line interpreter with end of line

        Args:
            arg_str (str): the remaining of the line after the command
        """
        print()
        return True

    def do_quit(self, arg_str):
        """quit: Exits the command line interpreter

        Args:
            arg_str (str): the remaining of the line after the command
        """
        return True

    def emptyline(self):
        """prints prompt again if enter button is pressed with
        empty line
        """
        pass

    def do_create(self, arg_str):
        """Creates a new instance of the BaseModel

        Args:
            arg_str (str): the remaining of the line after the command
        """
        modules = self.modules

        if len(arg_str) < 1:
            print("** class name missing **")
        elif arg_str not in modules:
            print("** class doesn't exist **")
        else:
            model_path = "models.{}".format(modules[arg_str])
            module = importlib.import_module(model_path)
            cls = getattr(module, arg_str)
            model = cls()
            model.save()
            print(model.id)

    def do_show(self, arg_str):
        """Prints the string representaion of an instance

        Args:
            arg_str (str): the remaining of the line after the command
        """

        args = arg_str.split()
        args_len = len(args)

        if args_len < 1:
            print("** class name missing **")
        elif args_len < 2:
            print("** instance id missing **")
        else:
            objects = self.objects
            key = "{}.{}".format(args[0], args[1])
            if args[0] not in self.modules:
                print("** class doesn't exist **")
            elif key not in objects:
                print("** no instance found **")
            else:
                print(objects[key])

    def do_destroy(self, arg_str):
        """Deletes an instance base on the class name and id

        Args:
            arg_str (str): the remaining of the line after the command
        """
        args = arg_str.split()
        args_len = len(args)

        if args_len < 1:
            print("** class name missing **")
        elif args_len < 2:
            print("** instance id missing **")
        else:
            objects = self.objects
            key = "{}.{}".format(args[0], args[1])
            if args[0] not in self.modules:
                print("** class doesn't exist **")
            elif key not in objects:
                print("** no instance found **")
            else:
                del objects[key]
                storage.save()

    def do_all(self, args_str):
        """Prints all string representation of all instances
        based or not on the class name

        Args:
            arg_str (str): the remaining of the line after the command
        """
        args = args_str.split()
        objects_val = self.objects.values()

        if len(args) > 0:
            if args[0] not in self.modules:
                print("** class doesn't exist **")
            else:
                objects_list = []
                for obj in objects_val:
                    cls_name = obj.__class__.__name__
                    if cls_name == args[0]:
                        objects_list.append(str(obj))
                print(objects_list)
        else:
            objects_list = [str(object) for object in self.objects.values()]
            print(objects_list)

    def do_update(self, args_str):
        """Updates an instance based on the class name and id
        by adding or updating attribute

        Args:
            arg_str (str): the remaining of the line after the command
        """

        args = args_str.split()
        args_len = len(args)
        objs = self.objects
        if args_len < 1:
            print("** class name missing **")
        elif args_len < 2:
            print("** instance id missing **")
        elif args_len < 3:
            print("** attribute name missing **")
        elif args_len < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if args[0] not in self.modules:
                print("** class doesn't exist **")
            elif key not in objs:
                print("** no instance found **")
            elif hasattr(objs[key], args[2]):
                attr = getattr(objs[key], args[2])
                val = args[3].replace("\"", "")
                if type(attr) == int:
                    val = int(val)
                elif type(attr == float):
                    val = float(val)

                setattr(objs[key], attr, val)
            else:
                val = args[3].replace("\"", "")
                print(type(val))
                obj = objs[key]
                obj.__dict__[args[2]] = val


if __name__ == '__main__':
    HBNBCommand().cmdloop()
