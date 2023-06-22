import json

def get_configs() -> dict:
    with open("config.json", "r") as config:
        return json.load(config)

def import_class(modulename, name):
    try:
        module = __import__(modulename, globals(), locals(), [name])
    except ImportError:
        return None

    return vars(module)[name]