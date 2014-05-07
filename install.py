#!/usr/bin/env python
from __future__ import print_function
import sys, yaml, os, shutil
import readline
import signal

version    = 3000
use_colors = True

colors = {
'yellow' : '\033[33m',
'green'  : '\033[32m',
'cyan'   : '\033[36m',
'blue'   : '\033[94m',
'bold'   : '\033[1m',
'red'    : '\033[91m',
'end'    : '\033[0m' # <-- reset
}

try:
    with open('settings.yaml', 'r') as stream:
        settings = yaml.load(stream)

except IOError:
    print('Could not parse settings.yaml. Aborting.')
    sys.exit(0)

def install(config):
    """Installs config. Prompts user for confirmation."""

    if config not in settings:
        return "Invalid config id: %s" % config

    src = os.path.join('configs', settings[config]['src'])
    dst = os.path.expanduser(settings[config]['dst'])

    dst_exists = os.path.exists(dst)
    src_exists = os.path.exists(src)

    if not src_exists:
        print(colorize('Source file "%s" does not exist. Abort!' % src, 'red'))
        return

    print(colorize('\nsrc:', 'bold'), '\t', src)
    print(colorize('dst:', 'bold'), '\t', dst, end="\n\n")

    if dst_exists:
        print("Destination file already exists!", end="\n\n")

    while True:
        response = raw_input("Install this config? [y/n] ")

        if response == 'y': 
            print(colorize("\nCONFIG INSTALLED: %s" % dst, 'green'))
            shutil.copy(src, dst)
            break

        elif response == 'n':
            print(colorize('\nCONFIG NOT INSTALLED: %s' % src, 'red'))
            break

        else:
            print(colorize("Please answer y or n.", 'cyan'))

def install_all():

    for config in settings:
        install(config)

def colorize(string, color):
    if color in colors:
        return "%s%s%s" % (colors[color], string, colors['end'])
    return string

def main():
    config = sys.argv[1] if len(sys.argv) > 1 else None

    if not config: install_all()
    else: install(config)

    print(colorize('Done.', 'bold')) 


def exit_handler(signal, frame):
    print(colorize("\n\nABORT MISSION!!!!", 'red'), end="\n\n")
    exit(1)

if __name__ == '__main__':

    signal.signal(signal.SIGINT, exit_handler)

    readline.set_history_length(50)

    if not use_colors: 
        colors = {}

    install_all()
