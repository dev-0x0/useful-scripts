#!/usr/bin/python3

# Generate bad character byte array for BOF
# Takes one argument, a string of bad characters surrounded in quotes. Ex: "00 07 08 2e 2f a0 a1"

import sys

BADCHARS = []

def usage():
    print("USAGE:\n\tpython3 getbadchars.py [string of space separated badchars]\n")
    print('''
EXAMPLES:
\tpython3 getbadchars.py "00 07 08 2e 2f a0 a1"
\tpython3 getbadchars.py 01
\tpython3 getbadchars.py''')

if len(sys.argv) > 2:
    usage()
    sys.exit(0)

if len(sys.argv) == 2:
    BADCHARS = [int(bad, base=16) for bad in sys.argv[1].split()]

# Generate Byte-Array
for x in range(1, 256):
    
    if x in BADCHARS:
        continue

    print("\\x" + "{:02x}".format(x), end='')

# Output bad characters for convenience
if len(sys.argv) == 2:
    print("\n\nBad characters excluded:")
    print(r'\x' + r'\x'.join([bad for bad in sys.argv[1].split()]))

print()
