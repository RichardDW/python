#!/usr/bin/env python3
import sys

def readargs():
    if len(sys.argv) != 4:
        raise SystemExit('Usage:',  sys.argv[0], 'pathfile, password, pathmask')
    pathfile = sys.argv[1]
    passwd = sys.argv[2]
    pathmask = sys.argv[3]

def readfiles():
    pass
    #data = open(pathfile, "r").read() 
    #for line in data:
    # check if line is directory or file
    # if line is file then add to zip
    #addfilestozip()
    # if line is directory  chdir into directory
    # and read lines
    

def createzip():
    pass

def addfilestozip():
    pass

def encryptzip():
    pass

# to terminate program 
#raise SystemExit(0)


def main():
# read options from command line (password, listfile, compression) 
    if len(sys.argv) != 4:
        raise SystemExit('Usage:',  sys.argv[0], 'pathfile, password, pathmask')
    pathfile = sys.argv[1]
    passwd = sys.argv[2]
    pathmask = sys.argv[3]
    print(pathfile, passwd, pathmask)
# read file with directories and files to be zipped
    readfiles()
# create zip file 
# add files to zip file
# split zip file in multiple zips
# encrypt zip file 

if __name__ == "__main__":
    main()
