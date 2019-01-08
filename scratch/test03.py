#!/usr/bin/env python
import os
if os.path.isdir("/tmp"):
    print ("/tmp is a directory")
else:
    print ("/tmp is not a directory")

from pathlib import Path

p = Path('.')
[x for x in p.iterdir() if x.is_dir()]

try:
    open(p)
except IOError:

# check to see whether p is a file
p.is_file()
# check to see whether p is a directory
p.is_dir()

