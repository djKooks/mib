import click
import pickle

from membli.storage import Storage
from membli.utils import copy_to_clip

STORAGE_FILE = 'membli.bin'


@click.group()
def cli():
    pass


@cli.command('create', help='Create key-value storage')
# @click.option('-l', '--lock', 'lock')
def create(lock):
    """
    TODO:
    """
    import os
    myhost = os.uname()[1]
    
    with open(STORAGE_FILE, 'wb') as f:
        storage = Storage(myhost)
        pickle.dump(storage, f)
    

@cli.command('get', help='Get value from storage with key')
@click.argument('key')
@click.option('-c', '--copy', 'is_copy', is_flag=True)
def get(key, is_copy: bool):
    """
    TODO:
    """

    try:
        with open(STORAGE_FILE, 'rb') as pk_storage:
            storage = pickle.load(pk_storage)
            val = storage.get(key)

            if is_copy:
                if copy_to_clip(val):
                    print(f'Value for key "{key}" has been copied to clipboard')
                else:
                    print('Copy has been failed for unexpected reason')
            else:
                print(val)
    except FileNotFoundError:
        print('No storage, create with `create` option')


@cli.command('put', help='Put key-value set to storage')
@click.argument('key')
@click.argument('value')
def put(key, value):
    """
    TODO:
    """

    try:
        rf = open(STORAGE_FILE, 'rb')
        update_storage = pickle.load(rf)
        rf.close()

        wf = open(STORAGE_FILE, 'wb')
        update_storage.update(key, value)
        pickle.dump(update_storage, wf)
    except FileNotFoundError:
        print('No storage, create with `create` option')
        

@cli.command('delete', help='Delete key-value set from storage')
@click.argument('key')
def delete(key):
    """
    TODO:
    """

    try:
        rf = open(STORAGE_FILE, 'rb')
        update_storage = pickle.load(rf)
        rf.close()

        wf = open(STORAGE_FILE, 'wb')
        update_storage.delete(key)
        pickle.dump(update_storage, wf)
        wf.close()
        
    except FileNotFoundError:
        print('No storage, create with `create` option')


@cli.command('list', help='Display list of key-value sets in storage')
def list():
    """
    TODO:
    """

    with open(STORAGE_FILE, 'rb') as buf_read:
        try:
            data: Storage = pickle.load(buf_read)
            data.list()
        except EOFError:
            raise Exception('Cannot load file')

