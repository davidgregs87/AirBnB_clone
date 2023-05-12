#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, args):
        """ stops the program """
        return True

    def do_quit(self, args):
        """ Quits the program """
        return True

    def emptyline(self):
        pass

    def do_create(self, args):
        if len(args) == 0:
            print("** class name missing **")
        if args in globals().keys():
            obj = globals()[args]
            new_instance = obj()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")
    
    def do_show(self, args):
        if len(args) == 0:
            print("** class name missing **")
        else:
            try:
                cls_name, cls_id = args.split()
                if cls_name not in globals().keys():
                    print("** class doesn't exist **")
                cls_dict = storage.all()
                print(cls_dict)
                if cls_name+"."+cls_id in cls_dict.keys():
                    print(cls_dict[cls_name+"."+cls_id])
                else:
                    print("** no instance found **")
            except ValueError:
                print("** instance id missing **")
        print(len(args))

    def do_destroy(self, args):
        if len(args) == 0:
            print("** class name missing **")
        else:
            try:
                cls_name, cls_id = args.split()
                if cls_name not in globals().keys():
                    print("** class doesn't exist **")
                cls_dict = storage.all()
                if cls_name+"."+cls_id in cls_dict.keys():
                    del cls_dict[cls_name+"."+cls_id]
                    with open(storage._FileStorage__file_path, "r") as f:
                        json_dict = json.load(f)
                        del json_dict[cls_name+"."+cls_id]
                    with open(storage._FileStorage__file_path, "w") as f:
                        json.dump(json_dict, f)
                else:
                    print("** no instance found **")
            except ValueError:
                print("** instance id missing **")
        print(len(args))
    
    def do_all(self, args):
        all_list = []
        if len(args) == 0:
            cls_dict = storage.all()
            print(cls_dict)
            for key in cls_dict.keys():
                all_list.append(str(cls_dict[key]))
            print(all_list)
        else:
            if args not in globals().keys():
                print("** class doesn't exist **")
            else:
                cls_dict = storage.all()
                for key in cls_dict.keys():
                    all_list.append(str(cls_dict[key]))
                    print(all_list)
    
    def do_update(self, args):
        if len(args) == 0:
            print("** class name missing **")
        else:
            word  = args.split()
            if word[0] not in globals().keys():
                print("** class doesn't exist **")
            if len(word) == 1:
                print("** instance id missing **")
            else:
                cls_dict = storage.all()
                if word[0]+"."+word[1] in cls_dict.keys():
                    obj = cls_dict[word[0]+"."+word[1]]
                    if len(word) == 2:
                        print("** attribute name missing **")
                    else:
                        if len(word) == 3:
                            print("** value missing **")
                        else:
                            new_word = word[3].strip('"')
                            setattr(obj, word[2], new_word)
                            with open(storage._FileStorage__file_path, "r") as f:
                                json_dict = json.load(f)
                                json_dict[word[0]+"."+word[1]] = obj.to_dict()
                            with open(storage._FileStorage__file_path, "w") as f:
                                json.dump(json_dict, f)
                else:
                    print("** no instance found **")




 


if __name__ == '__main__':
    HBNBCommand().cmdloop()
