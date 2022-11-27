#!/usr/bin/python3
'''
Creates a class FileStorage
'''
import json
from models.base_model import BaseModel
import models

class FileStorage:
    '''
    Class that serializes instance to JSON file and
    deserializes JSON file to instance
    '''

    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        '''
        returns the dictionary __objects
        '''
        return type(self).__objects

    def new(self, obj):
        '''
        sets in __objects the obj with key <obj class name>.id
        '''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        type(self).__objects[key] = obj

    def save(self):
        '''
        serializes __objects to the JSON file in file path
        '''
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(new_dict, file)

    def reload(self):
        '''
        deserializes the JSON file to __objects if the file exists
        '''
        try:
            with open(self.__file_path, "r") as file:
                obj = json.load(file)
                for key, value in obj.items():
                    val = models.class_list[value["__class__"]](**value)
                    self.__objects[key] = val
        except:
            pass