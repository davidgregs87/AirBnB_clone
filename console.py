#!/usr/bin/python3

"""
The console module - command line interpreter
"""

import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Class for command line interpreter
    """
    prompt = "(hbnb) "

    class_list = [
            "Amenity", "BaseModel",  "City", "Place",
            "State", "Review", "User"
            ]

    def emptyline(self):
        """Empty line"""
        pass

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        End of File Method - Quit program
        """
        return True

    def do_create(self, line):
        """
        Creates a new instance of BaseModel and prints the id
        """
        if not line:
            print("** class name missing **")
        elif line not in self.class_list:
            print("** class doesn't exist **")
        else:
            new = eval(line)()
            new.save()
            print(new.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        """
        line_list = line.split()

        if not line:
            print("** class name missing **")
        elif line_list[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(line_list) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(line_list[0], line_list[1])
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """
        line_list = line.split()

        if not line:
            print("** class name missing **")
        elif line_list[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(line_list) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(line_list[0], line_list[1])
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                del (storage.all()[key])
                storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances
        """
        if line:
            if line not in self.class_list:
                print("** class doesn't exist **")
            else:
                all_list = []
                for val in storage.all().values():
                    if type(val).__name__ == line:
                        all_list.append(str(val))
                print(all_list)
        else:
            all_list = []
            for key, val in storage.all().items():
                all_list.append(str(val))
            print(all_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        """
        line_list = line.split()

        if not line:
            print("** class name missing **")
        elif line_list[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(line_list) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(line_list[0], line_list[1])
            if key not in storage.all().keys():
                print("** no instance found **")

            elif len(line_list) == 2:
                print("** attribute name missing **")
            elif len(line_list) == 3:
                print("** value missing **")
            else:
                attr = line_list[2]
                _type = type(line_list[3])
                value = line_list[3]
                for k, val in storage.all().items():
                    if k == key:
                        obj = val

                obj_dict = obj.__dict__
                obj_dict[attr] = _type(value)
                storage.save()

    def do_count(self, line):
        """
        Retrieves the number of instances of a class
        """
        if line not in self.class_list:
            print("** class doesn't exist **")
        else:
            count = 0
            obj_keys = storage.all().keys()
            class_key = []
            for k in obj_keys:
                name = k.split('.')
                class_key.append(name[0])
            for v in class_key:
                if v == line:
                    count += 1
            print(count)

    def default(self, line):
        """
        Called When the prefix is not a command
        """
        args = line.split('.')
        if len(args) == 1:
            print("** instance id missing **")
            return
        className = args[0]
        comArg = args[1]  # command + other args
        if className not in self.class_list:
            print("** class doesn't exist **")
        else:
            args = comArg.split('(')
            if len(args) == 1:
                print("Invalid!")
                return
            comd = args[0]  # command
            otherArgs = args[1]  # other args x)

            if comd == "all":
                HBNBCommand.do_all(self, className)
            elif comd == "count":
                HBNBCommand.do_count(self, className)
            elif comd == "show":
                args = otherArgs.split(')')
                _id = args[0].replace('"', "")
                others = args[1]
                line = className + " " + _id
                HBNBCommand.do_show(self, line)
            elif comd == "destroy":
                args = otherArgs.split(')')
                _id = args[0].replace('"', "")
                others = args[1]
                line = className + " " + _id
                HBNBCommand.do_destroy(self, line)
            elif comd == "update":
                args = otherArgs.split(',')
                try:
                    _id = args[0].replace('"', "")
                    attr = args[1].replace('"', "")
                    attr = attr.strip()
                    val = args[2].replace('"', "")
                    val = args[2].replace(')', "")
                    val = val.strip()
                    line = className + " " + _id + " " + attr + " " + val
                    HBNBCommand.do_update(self, line)
                except IndexError:
                    print("Invalid!")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
