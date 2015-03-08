import os
import sys

home_dir = os.path.expanduser("~")
config_file_name = ".pyptrc"

if sys.platform == "win32":
    config_file_name = "_pyptrc"

global_config_file = os.path.join(home_dir, config_file_name)
local_config_file = os.path.join(".", config_file_name)
