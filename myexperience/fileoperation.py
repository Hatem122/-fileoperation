
import os

def read(filepath, option='all'):
    try:
        with open(filepath, 'r') as file:
            if option == 'all':
                return file.read()
            elif option == '5':
                return file.read(5)
            elif option == 'line':
                return file.readline()
            elif option == 'lines':
                return file.readlines()
            else:
                raise ValueError("Invalid option. Choose from 'all', '5', 'line', 'lines'.")
    except FileNotFoundError:
        return "File not found."

def write(filepath, content, option='write'):
    mode = 'w' if option == 'write' else 'w'
    with open(filepath, mode) as file:
        if isinstance(content, list):
            file.writelines(content)
        else:
            file.write(content)

def append(filepath, newcontent, option='write'):
    mode = 'a' if option == 'write' else 'a'
    with open(filepath, mode) as file:
        if isinstance(newcontent, list):
            file.writelines(newcontent)
        else:
            file.write(newcontent)
