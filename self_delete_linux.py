#!/usr/bin/env python

import subprocess as sp
from os import path

# This gives us the absolute(full) path to this python script
self_path = path.abspath(__file__)

# Do stuff -- I just created a folder
# Here you could perform a cleanup 
# Delete files, reset configurations or anything else
sp.call(["mkdir", "/home/User/Desktop/thinair"])

# At the end of the script, the file shreds itself
sp.call(["/usr/bin/shred", "-fuz" , self_path])

