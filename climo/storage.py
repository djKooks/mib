import sys
import os
# import pickle

class Storage(object):
    def __init__(self, id):
        self.id = id
        self.kv = dict()

    def update(self, key, value):
        new_kv = self.kv
        new_kv[key] = value
        self.kv = new_kv

    def get(self, key) -> str:
        return self.kv[key]

    def delete(self, key):
        removed_value = self.kv.pop(key, None)
        if removed_value is None:
            print('Not exists key')
        else:
            print(f'Delete key : {key}')

    def list(self):
        for key, value in self.kv.items():
            print(f'{key} -> {value}')

