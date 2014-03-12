#!/usr/bin/env python
#A simple script to install config files 

from __future__ import print_function
import sys, yaml, os, shutil

home = os.path.expanduser('~')

try:
    with open('settings.yaml', 'r') as stream:
        settings = yaml.load(stream)

except IOError:
    print('Could not parse settings.yaml. Aborting.')
    sys.exit(0)

def main():

    config = sys.argv[1] if len(sys.argv) > 1 else None

    if not config:
        return "Usage: ./install.py <config>"

    settings = read_settings()

    if config not in settings:
        return "There's no config with that name."

    src = os.path.join('configs', settings[config]['src'])
    dst = settings[config]['dst']

    if not os.path.exists(src):
        return "Source config does not exist."

    if os.path.exists(dst):
        print("The destination file already exists. Over-write? [y/N/d] "), 

    shutil.copy(src, dst)

def print_available_settings():
    print("\nAvailable settings:\n")
    for config in settings.iteritems():
        print("%s:" % config[0])
        print("    src: %s" % config[1]['src'])
        print("    dst: %s" % config[1]['dst'])
        print("")

if __name__ == '__main__':
    main()