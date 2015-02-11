from sys import version_info
from subprocess import Popen, PIPE
from getpass import getuser


def get_input(input_msg):

    if version_info >= (3, 0):
        return input(input_msg)
    else:
        return raw_input(input_msg)


def get_username():
    '''Get git config values.'''
    username = ''

    # use try-catch to prevent crashes if user doesn't install git
    try:
        # run git config --global <key> to get username
        git_command = ['git', 'config', '--global', 'user.name']
        p = Popen(git_command, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()

        # turn stdout into unicode and strip it
        username = output.decode('utf-8').strip()

        # if user doesn't set global git config name, then use getuser()
        if not username:
            username = getuser()
    except OSError:
        # if git command is not found, then use getuser()
        username = getuser()

    return username


def get_email():

    try:
        git_command = ['git', 'config', '--global', 'user.email']
        p = Popen(git_command, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()

        email = output.decode('utf-8').strip()

        if not email:
            return None
        else:
            return email

    except OSError:

        return None
