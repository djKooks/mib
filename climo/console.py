
from click import echo, style


def print_table_header():
    print_table_line()
    print_table_row('key', 'value')
    print_table_line()

def print_table_line():
    echo(style('-----------------------------------------------', fg='blue'))


def print_table_row(key, value):
    echo(style(f'| {_ellipsis_string(key, 20)} | {_ellipsis_string(value, 20)} |', fg='green'))


def _ellipsis_string(text, length) -> str:
    ellipsised = text[:length - 3] + '...' if len(text) > 20 else text
    padding = '{:<20}'.format(ellipsised)
    return padding
