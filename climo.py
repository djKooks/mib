# -*- coding: utf-8 -*-
import click
import pickle


STORAGE_FILE = 'climo.bin'

@click.group()
def cli():
    pass


@cli.command()
def init():
    import os
    myhost = os.uname()[1]
    with open(STORAGE_FILE, 'wb') as storage:
        init_dict = {
            'climo': myhost,
            key: value
        }

        pickle.dump(init_dict, storage)


@cli.command()
@click.argument('key')
def get(key):
    print('get by key')
    pass


@cli.command()
@click.argument('key')
@click.argument('value')
def put(key, value):
    try:
        rf = open(STORAGE_FILE, 'rb')
        update_storage = pickle.load(rf)
        rf.close()

        wf = open(STORAGE_FILE, 'wb')
        update_storage[key] = value
        pickle.dump(update_storage, wf)
    except FileNotFoundError:
        print('No storage, create with `init` option')
        

@cli.command()
def show():
    with open(STORAGE_FILE, 'rb') as storage:
        try:
            data = pickle.load(storage)
            print(data)
        except EOFError:
            raise

