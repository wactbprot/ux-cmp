import json

def get_config_dict():
    with open('./config.json') as json_config_file:
        config = json.load(json_config_file)

    return config
