import json
from os.path import abspath, expanduser,isfile
from utils.converts import mono_space

def full_path (path):
    return abspath(expanduser(path))

def read_history_file(path):
    with open(full_path(path)) as file:
        lines = [mono_space(line) for line in file]
    return lines

def read_json_file(path):
    with open(full_path(path), "r") as read_file:
        data = json.load(read_file)
    return data

def write_file(path, lines):
    with open(full_path(path), "w") as file:
        for  line in lines:
            file.write(line + '\n')
        file.close()

def is_file(path):
    return isfile(full_path(path))
