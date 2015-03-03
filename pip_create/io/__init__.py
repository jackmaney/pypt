from sys import version_info


def get_input(input_msg):

    if version_info >= (3, 0):
        return input(input_msg)
    else:
        return raw_input(input_msg)

from temp_file import process_temp_file
