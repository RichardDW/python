from sys import argv

script, filename = argv

txt = open(filename)

print('>>>>>>>>>>>>> ', repr(txt))

print(f"here is your file {filename}:")
print(txt.read())
