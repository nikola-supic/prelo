"""
DOCSTRING: Simple script to compile all UI's at once.

"""

import subprocess
import os


def get_ui():
    """
    DOCSTRING: function to get all .ui files

    """
    ui_list = []
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for file in files:
        if file.endswith('.ui'):
            ui_list.append(file)
    return ui_list


def get_ui_output(ui_name):
    """
    DOCSTRING: function to get output name from .ui file (FORMAT: screen_NAME.py)

    """
    if ui_name.endswith('.ui'):
        ui_name = ui_name[:-3]
    if ui_name.startswith('ui_'):
        ui_name = ui_name[3:]
    return f'screen_{ui_name}.py'


def compile_ui(ui_list):
    """
    DOCSTRING: function to compile .ui files using subprocess module

    """
    count = 0
    for item in ui_list:
        output = get_ui_output(item)
        subprocess.run(f'pyuic5 {item} -o {output}', shell=True, check=True)
        print(f'[ + ] Successfully compiled {item} --> {output}')
        count += 1

    print(f'\n[ + ] Successfully compiled {count} UI screens.')


if __name__ == '__main__':
    ui_files = get_ui()
    compile_ui(ui_files)
