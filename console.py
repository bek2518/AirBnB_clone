#!/usr/bin/python3
'''
Program that contains an entry point of
the command interpreter
'''
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import class_list, storage


class HBNBCommand(cmd.Cmd):
    '''
    class definition
    '''
    prompt = '(hbnb)'

    def do_EOF(self, args):
        '''
        Quit the program when EOF
        '''
        return True

    def do_quit(self, args):
        '''
        Quit the program when quit passed
        '''
        return True

    def emptyline(self):
        '''
        Handles when an empty line is passed
        '''
        pass

    def do_create(self, args):
        '''
        Create new instance of BaseModel
        Save it to the JSON file and print the id
        '''
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        elif args[0] not in class_list:
            print("** class doesn't exist **")

        else:
            new_instance = class_list[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        '''
        Prints the string representation of an instance
        Based on the class name and the id
        '''
        args = args.split()
        if not args or len(args) == 0 or args[0] == "":
            print("** class name missing **")

        elif args[0] not in class_list:
            print("** class doesn't exist **")

        elif len(args) == 1 or args[1] == "":
            print("** instance id is missing **")

        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        '''
        Deletes an instance based on the class name and id
        '''
        args = args.split()
        if not args or len(args) == 0 or args[0] == "":
            print("** class name missing **")

        elif args[0] not in class_list:
            print("** class doesn't exist **")

        elif len(args) == 1 or args[1] == "":
            print("** instance id is missing **")

        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        '''
        Prints all representation of all instances
        based or not on the class name'''
        args = args.split()
        objects = storage.all()
        if not args:
            value_list = []
            for key, value in objects.items():
                value_list.append(str(objects[key]))
            if value_list:
                print(value_list)
        else:
            value_list = []
            for key, value in objects.items():
                if value.__class__.__name__ == args[0]:
                    value_list.append(str(objects[key]))
            if value_list:
                print(value_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, args):
        '''
        Updates an instance based on the class name and id
        by adding or updating an attribute
        '''
        args = args.split()
        objects = storage.all()
        existing_key = args[0] + "." + args[1]

        if not args or len(args) == 0 or args[0] == "":
            print("** class name missing **")

        elif args[0] not in class_list:
            print("** class doesn't exist **")

        elif len(args) == 1 or args[1] == "":
            print("** instance id is missing **")

        elif len(args) == 2 or args[2] == "":
            print("** attribute name missing **")

        elif len(args) == 3 or args[3] == "":
            print("** value missing **")

        else:
            for key, value in objects.items():
                if key == existing_key:
                    attribute = args[3].split('"')
                    try:
                        int(attribute[1])
                        return (int)
                    except ValueError:
                        pass
                    try:
                        float(attribute[1])
                        return (float)
                    except ValueError:
                        return (str)
                    objects[key].__dict__[args[2]] = (t)(arrtibute[1])
                    objects[key].updated_at = datetime.now()
                    storage.save()
                    return
                else:
                    print("** no instance found **")

    def default(self, args):
        command = {
            'all()': "do_all",
            'count()': "do_count",
            'create()': "do_create"
        }
        tokens = args.split('.', 1)
        if tokens[0] not in class_list:
            print("** class doesn't exist **")

        elif tokens[1] not in command:
            print("** command doesn't exist **")

        else:
            eval('self.{}("{}")'.format(command[tokens[1]], tokens[0]))

    def do_count(self, args):
        count = 0
        objects = storage.all()
        for key, value in objects:
            temp = key.split('.', 1)
            if temp[0] == args:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
