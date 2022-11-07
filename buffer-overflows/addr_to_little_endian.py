#!/usr/bin/python3

import sys

if len(sys.argv[0]) < 2:
    sys.exit(0)

addr = sys.argv[1]
little_endian = []

for i in range(0, len(addr), 2):
    little_endian.insert(0, addr[i:i+2])

print(r'\x' + r'\x'.join([x for x in little_endian]))
