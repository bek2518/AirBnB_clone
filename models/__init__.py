#!/usr/bin/python3
'''
__init__file
'''

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User

class_list = {
    'BaseModel': BaseModel,
    'User': User
}
storage = FileStorage()
storage.reload()