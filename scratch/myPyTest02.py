import os
# open file from ..\database\US_state_capitols.txt
# read a line
STATE_LIST = "c:\\Data\src\\database\\US_state_capitols.txt"
with open(STATE_LIST, 'r') as f:
    statecap = f.read()
statecap = statecap.strip('\n')
statecap = statecap.replace(",","\n")
statecap = statecap.strip()

parts = statecap.split(':')
#parts = statecap.replace(':','')

'''
myparts = ['ab','bc','cd']
print(type(myparts))
print(myparts)
'''
print(type(statecap))
print(statecap)
#print(type(parts))
#print(parts)









'''
statecap = open(STATE_LIST).readlines()
# Get rid of newlines and white space
statecap = [word.strip() for word in statecap]
for line in statecap:
    print(f'this is a line {line}')
    print('\n')



print(type(statecap))
print(statecap)

print(os.getcwd())

mytest = {'Washington': 'Olympia', 'Delaware': 'Dover'}
print(type(mytest))
print(mytest.get('Delaware'))
'''