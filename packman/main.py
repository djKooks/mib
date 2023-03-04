import os
from os.path import exists as file_exists

import click
import pickle

from packman.alias_group import AliasedGroup
from packman.storage import Storage
from packman.utils import copy_to_clip, command_parser

STORAGE_DIRECTORY_PATH = os.path.join('~', '.packman')
STORAGE_FILE = os.path.expanduser(os.path.join(STORAGE_DIRECTORY_PATH, 'storage.bin'))


@click.group(cls=AliasedGroup)
def cli():
    pass


@cli.command('create', help='Create key-value storage')
@click.option('-i', '--init', 'init')
def create(init):
    """
    TODO:
    """
    myhost = os.uname()[1]

    if file_exists(STORAGE_FILE):
        if init:
            print('Initiate current storage file.')
            os.remove(STORAGE_FILE)
        else:    
            print('Storage file already exists. Add -i (--init) option to re-create it.')
            return False
    else:
        from pathlib import Path
        
        storage_dir = os.path.expanduser(STORAGE_DIRECTORY_PATH)
        Path(storage_dir).mkdir(parents=True, exist_ok=True)
    
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

    try:
        with open(STORAGE_FILE, 'rb') as buf_read:
            try:
                data: Storage = pickle.load(buf_read)
                data.list()
            except EOFError:
                raise Exception('Cannot load file')
    except FileNotFoundError:
        print('No storage file found. Create new one with `create` option.')


@cli.command('run', help='Trigger command in storage')
@click.argument('key')
@click.argument('arguments', nargs=-1)
def run(key, arguments):
    """
    TODO: 
    """
    try:
        with open(STORAGE_FILE, 'rb') as pk_storage:
            storage = pickle.load(pk_storage)
            val = storage.get(key)
            command = command_parser(val, arguments)
            os.system(command)

    except FileNotFoundError:
        print('No storage, create with `create` option')

