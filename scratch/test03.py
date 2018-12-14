from pathlib import Path

p = Path(...)

try:
	open(p)
except IOError:

# check to see whether p is a file
p.is-file()
# check to see whether p is a directory
p.is-dir()