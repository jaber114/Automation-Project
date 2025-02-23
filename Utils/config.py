# 1. Create a file called config.py
# 2. Copy this code to the file (config.py)
# 3. Call this function to get values from the config.ini file (Ex. user = ConfigReader.read_config('email', 'user'))
import configparser
import sys

class ConfigReader:
    config = None
    @staticmethod
    def read_config(section, key):
        global config
        root_dir = sys.path[0]
        config = configparser.ConfigParser()
        config.read(root_dir + '/config.ini')
        # Check that the Section & key exists

        if config.has_section(section) and config.has_option(section, key):
            return config[section][key]
        else:
            # return config[section][key]
            raise KeyError(f"Section '{section}' or key '{key}' not found in config.ini")
