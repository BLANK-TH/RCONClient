from json import load, dump
from os import mkdir
from os.path import isfile, isdir

def load_config() -> dict:
    with open("data/config.json", "r") as f:
        return load(f)

def save_config(new_config):
    with open("data/config.json", "w") as f:
        dump(new_config, f, indent=2)

def assert_data():
    if not isdir("data"):
        mkdir("data")
    if not isfile("data/config.json"):
        with open("data/config.json", "w") as f:
            dump({}, f, indent=2)

def clean_filename(filename):
    return "".join([c if (c.isalpha() or c.isdigit() or c == '-') and c != ' ' else '_' for c in filename]).rstrip()
