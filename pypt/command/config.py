"""
Usage:  pypt config [--local | --global] [--type=<type>] set <key> <value>
        pypt config [--local | --global] [--type=<type>] <key>
        pypt config [--local | --global] --new
        pypt config --help

Options:
    --local         Only configure local settings (default)
    --global        Configure global settings
    --type=<type>   Specify a type (str, int, float, bool, null) [default: str].
    --set <key> <value>    Set the value to the given key. Dots in keys specify subsections (eg init.setup.author)
                            If this flag is not specified, then find the value(s) for the specified key.
    --new           If this flag is set, the specified config file will be squashed and replaced with defaults
                    (WARNING: this is irreversible!)
    --help, -h      Display this screen and quit.
"""

from docopt import docopt
from ..io.config.file import global_config_file, local_config_file
from ..io.config import reader, writer
import sys


def _get_value(key, config_data, config_file, penultimate=False):

    result = config_data
    keys = key.split(".")
    if penultimate:
        keys = keys[:-1]

    for k in keys:
        if k in result:
            result = result[k]
        else:
            msg = "No such option found in config file {}: '{}'".format(
                config_file, key)
            raise ValueError(msg)
    return result


def config(argv):

    args = docopt(__doc__, argv=argv)

    global_flag = args["--global"]

    config_file = global_config_file if global_flag else local_config_file

    config_data = reader.from_file(config_file)

    if args["set"]:

        last_kv = _get_value(args["<key>"], config_data, config_file,
                             penultimate=True)
        last_key = args["<key>"].split(".")[-1]
        if last_key not in last_kv:
            msg = "No such option found in config file {}: '{}'".format(
                config_file, args["<key>"])
            raise ValueError(msg)
        last_kv[last_key] = args["<value>"]
        writer.write_config(config_data, global_config=global_flag)
    elif args["--new"]:
        writer.write_default_config(global_config=global_flag)
    else:
        result = _get_value(args["<key>"], config_data, config_file)

        if isinstance(result, dict):
            for k in result:
                print "{}={}".format(k, result[k])
        else:
            print result
