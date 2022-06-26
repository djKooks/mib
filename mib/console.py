
from click import echo, style
import textwrap

def print_table_header():
    print_table_line()
    print_table_title()
    print_table_line()


def print_table_line():
    echo(style('-------------------------------------------------------------------', fg='blue'))


def print_table_title():
    echo(style(f'| {_ellipsis_string("key", 30)} | {_ellipsis_string("value", 30)} |', fg='green'))


def print_table_row(key, value):
    echo(style(f'| {_ellipsis_string(key, 30)} | {_ellipsis_string(value, 30)} |', fg='white'))


def _ellipsis_string(text, length) -> str:
    ellipsised = text[:length - 3] + '...' if len(text) > length else text
    padding = '{:<30}'.format(ellipsised)
    
    return padding
