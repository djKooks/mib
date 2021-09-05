import sys
import os
# import pickle
from mib.console import print_table_line, print_table_row, print_table_header


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
            print(f'Cannot find key `{key}`')
        else:
            print(f'Delete key : {key}')

    def list(self):
        print()
        print_table_header()
        for key, value in self.kv.items():
            print_table_row(key, value)

        print_table_line()
