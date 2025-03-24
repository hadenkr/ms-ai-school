import json

def get_config_info(file_name):
    with open(file_name, encoding="UTF-8") as f:
        config = json.load(f)

    return config
