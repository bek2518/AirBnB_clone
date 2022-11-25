#!/usr/bin/python3
'''
Creates a class FileStorage
'''
import json
from models.base_model import BaseModel

class FileStorage:
    '''
    Class that serializes instance to JSON file and
    deserializes JSON file to instance
    '''
    def __init__(self):
        '''
        Initialize
        '''
        self.__file_path = "file.json"
        self.__objects = {}
    
    def all(self):
        '''
        returns the dictionary __objects
        '''
        return self.__objects

    def new(self, obj):
        '''
        sets in __objects the obj with key <obj class name>.id
        '''
        self.__objects[obj.__class__.__name__] = obj

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
                self.__objects = json.load(file)
        except:
            pass