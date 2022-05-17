#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("[?] Usage: python3 " + sys.argv[0] + " <register contents (hex)>")
    sys.exit(0)

def getchars(eip):
    x = [eip[i:i+2] for i in range(0,8,2)]
    h = [chr(int('0x'+i, base=16)) for i in x]
    return ''.join(h)[::-1]


print(getchars(sys.argv[1]))

