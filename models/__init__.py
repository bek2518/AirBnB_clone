#!/usr/bin/python3
'''
__init__file
'''
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class_list = {
    'BaseModel': BaseModel
}
storage = FileStorage()
storage.reload()