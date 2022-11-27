#!/usr/bin/python3
'''
Creates a class BaseModel
'''


from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    '''
    Class that defines all common attributes/ methods for other classes
    '''
    def __init__(self, *args, **kwargs):
        '''
        Initialize
        '''
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value

    def __str__(self):
        '''
        Prints [<class name>] (<self.id>) <self.__dict__>
        '''
        return ("[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__))

    def save(self):
        '''
        Updates the public instance attribute updated_at with current datetime
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
        returns dictionary containing all keys/values of
        __dict__ of the instance
        '''

        new_dictionary = self.__dict__.copy()
        new_dictionary['__class__'] = self.__class__.__name__
        new_dictionary['created_at'] = self.created_at.isoformat()
        new_dictionary['updated_at'] = self.updated_at.isoformat()
        return new_dictionary