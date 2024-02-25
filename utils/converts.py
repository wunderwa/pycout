import json
import re

def key_as_list(dct, key):
    if isinstance(dct, dict) and key in dct and isinstance(dct[key], list):
        return dct[key]
    else:
        return []

def clean_list(cmd_list, included, excluded, excluded_start):
    new_list = included
    ex_set = set(excluded).union(set(included))
    for line in cmd_list:
        if not line in ex_set and not line.startswith(excluded_start):
            new_list.append(line)
            ex_set.add(line)
    return new_list

def map_simple_list(cmds):
    return list(map((lambda cmd: mono_space(cmd)), cmds))

def map_cmd_to_list(cmds):
    return list(map((lambda cmd: mono_space(cmd['cmd'])), cmds))

def map_tags(tags):
    return ' '.join(list(map((lambda tag: '#' + tag), tags)))

def map_cmd_and_tags_to_list(cmds):
    return list(map((lambda cmd: mono_space(cmd['cmd']) + ' ' + map_tags(cmd['tags'])), cmds))

def mono_space(line):
    line = line.rstrip()
    parts = re.split(r'\s+',line)
    return ' '.join(parts)

def json_fmt(json_dict):
    return json.dumps(json_dict, indent=4, sort_keys=True)

