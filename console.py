#!/usr/bin/python3
"""A command interpreter (console.py) to have some commands"""
import cmd
import shlex
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.base_model import BaseModel
from models import storage

classes = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """command interpreter interface"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quits the program gracefully"""
        return True

    def do_EOF(self, line):
        """End of string input or stdin"""
        return True

    def emptyline(self):
        """print next line if nothing is passed to the command line"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if len(line) == 0 or line is None:
            print("** class name missing **")
        elif line in globals():
            line = line.split()
            new_inst = eval(line[0] + "()")
            new_inst.save()
            print(new_inst.id)
        elif line not in globals():
            print("**class dosen't exist**")

    def do_show(self, line):
        """Prints the string representation of an
          instance based on the clascs name and id"""

        if line is None or len(line) == 0:
            print("** class name missing **")
        else:
            line = line.split()
            if len(line) != 2:
                print("** instance id missing **")
            elif line[0] not in globals():
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    if line[1] == value.id:
                        print(value)
                        return
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if line is None or len(line) == 0:
            print("** class name missing **")
        else:
            line = line.split(" ")
            if line[0] in globals():
                if len(line) < 2:
                    print("** instance id missing **")
                else:
                    key = str(line[0]) + "." + str(line[1])
                    obj = storage.all()
                    if key in obj:
                        del (obj[key])
                        storage.save()
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """Prints all string representation of all
          instances based or not on the class name"""
        obj = storage.all()
        obj_list = []
        if line in globals():
            for key in obj:
                obj_list.append(str(obj[key]))
            print(obj_list)
        else:
            try:
                line = line.split(" ")
                eval(line[0])
                for item in obj:
                    temp = obj[item].to_dict()
                    if temp['__class__'] == line[0]:
                        obj_list.append(str(obj[item]))
                print(obj_list)
            except Exception:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id """
        line = shlex.split(line)
        if len(line) == 0:
            print("** class name missing **")
        else:
            try:
                eval(str(line[0]))
            except Exception:
                print("** class doesn't exist **")
                return
            if len(line) == 1:
                print("** instance id missing **")
            else:
                objects = storage.all()
                key = str(line[0]) + "." + str(line[1])
                if key not in objects:
                    print("** no instance found **")
                else:
                    if len(line) == 2:
                        print("** attribute name missing **")
                    else:
                        if len(line) == 3:
                            print("** value missing **")
                        else:
                            setattr(objects[key], line[2], line[3])
                            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
