#!/usr/bin/python3

import sys

def usage():
    print("USAGE: python3 hexify-badchars.py [space separated string of badchars]")
    print('EXAMPLE: python3 hexify-badchars.py "00 07 08 2e 2f a0 a1"')
    sys.exit(0)

if len(sys.argv) < 2:
    usage()
    sys.exit(0)

badchars_list = sys.argv[1].split()

print(r'\x' + r'\x'.join([bad for bad in badchars_list]))



