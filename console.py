#!/usr/bin/python3
'''
Program that contains an entry point of
the command interpreter
'''
import cmd

class HBNBCommand(cmd.Cmd):
    '''
    class definition
    '''
    prompt = '(hbnb)'

    def do_EOF(self, arg):
        '''
        Quit the program when EOF
        '''
        return True
    
    def do_quit(self, arg):
        '''
        Quit the program when quit passed
        '''
        return True

    def emptyline(self):
        '''
        Handles when an empty line is passed
        '''
        pass

    def help_EOF(self):
        '''
        Defines the help for EOF
        '''
        print ('EOF command to exit the program\n')
    
    def help_quit(self):
        '''
        Defines the help for quit command
        '''
        print ('Quit command to exit the program\n')

if __name__ == '__main__':
    HBNBCommand().cmdloop()