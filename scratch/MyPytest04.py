
# open file C:\Data\src\database\US_state_capitols.txt for reading
STATE_LIST = "c:\\Data\src\\database\\US_state_capitols.txt"
with open(STATE_LIST, 'r') as f:
    statecap = f.read()
    # print each line
    print(statecap)


print('\nNext task;\n')

STATE_LIST = "c:\\Data\src\\database\\US_state_capitols.txt"
for line in open(STATE_LIST).readlines():
    # strip newline
    line = line.strip()
    #line = line.strip("'")
    line = line.replace("'","",4)
    line = line.split(sep=',')
    # print(line[0])
    # print(line[1])
    # print(line[2])
    # mydata=[line[0],line[1],line[2]]
    # write to table c:\sqlite\db\us_states.db
    # first establish connecting to database
    #print(type(line))
    print(line)
