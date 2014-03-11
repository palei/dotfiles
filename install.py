#! /usr/bin/env python
from optparse import OptionParser
import sys, yaml, os, shutil

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
        print "The destination file already exists. Over-write? [y/N/d] ", 

    shutil.copy(src, dst)    



def read_settings():
    try:
        stream = open('settings.yaml', 'r')
        return yaml.load(stream)
    except Error:
        print "Could not parse settings.yaml. Aborting."
        sys.exit(0)

if __name__ == '__main__':
    print main()
