#!/usr/bin/env python3

from utils.converts import  map_cmd_to_list, map_cmd_and_tags_to_list, map_simple_list, clean_list
from utils.files import read_json_file, read_history_file, write_file, is_file
from os.path import dirname

INIT_JSON_PATH = 'bash_history_cleaner.json'
USER_JSON_PATH = '~/.bash_history_cleaner.json'
BASH_HIST_PATH = '~/.bash_history'
# INIT_PATH_USER = '~/.' + INIT_PATH
# if has_file(INIT_PATH_USER)

print('CLEAN BASH HISTORY')
init_path = dirname(__file__) + '/' + INIT_JSON_PATH
print('Init file:', init_path)

init_json = read_json_file(init_path)
cmd_list = read_history_file(BASH_HIST_PATH)

user_json = {
    "included": [],
    "excluded": []
}

if is_file(USER_JSON_PATH):
    user_json = read_json_file(USER_JSON_PATH)


included = map_cmd_and_tags_to_list(init_json['included'] + user_json['included'])

excluded_main = map_simple_list(init_json['excluded'] + user_json['excluded'])
excluded_preset = map_cmd_to_list(init_json['included'] + user_json['included'])
excluded = set(excluded_main).union(set(excluded_preset))

new_history = clean_list(cmd_list, included, excluded)

write_file(BASH_HIST_PATH, new_history)
