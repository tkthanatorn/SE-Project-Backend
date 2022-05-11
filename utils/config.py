from yaml import safe_load, YAMLError
import os


def get_config(names=[]):
    # Load config.yaml
    configs = dict()
    with open(os.path.abspath('./utils/config.yaml'), 'r') as stream:
        try:
            configs = safe_load(stream)
        except YAMLError as err:
            print(err)

    # Find specific config
    for key in names:
        configs = configs[key]

    return configs  # return result
