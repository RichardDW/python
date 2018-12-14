from sys import argv
from os.path import exists

script, filename = argv
print(f"Does output file already exist? {exists(filename)}")
target = open(filename, 'w')

print('>>>>>>>>>>>   ', repr(argv))
print('>>>>>>>>>>>   ', repr(target))
print("truncating")
target.truncate()

line1 = input('give line 1')
line2 = input('give line 2')
line3 = input('give line 3')
line4 = input('give line 4')

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')
target.write(line4)
target.write('\n')

target.close()

