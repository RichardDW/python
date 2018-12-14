from collections import Counter
import difflib as diff


def compareLetters(inputlist):
    enen = 0
    tween = 0
    drien = 0
    for letters in inputlist:
        myCounter=Counter(letters).values()
        #print(myCounter)
        # check if there is a 2 or 3 value
        if 1 in myCounter:
            enen += 1
        if 2 in myCounter:
            tween += 1
            #print(f'there is a 2 in the list')
        if 3 in myCounter:
            drien += 1
            #print(f'there is a 3 in the list')
    print(f'enen zijn met {enen}, tween zijn met {tween} en drien zijn met zn {drien}')

def lookupLetters(inputList):
    # compare first string to second string, then 3rd string until last string
    # compare a with b
    inner = 1
    outer = 0
    maximum = len(inputList)
    print(maximum)
    for 

    first_string = inputList[outer]
    second_string = inputList[inner]
    print(f'{first_string}\n{second_string}')
    #d = diff.Differ()
    #result = d.compare(first_string, second_string)
    #print(result)
    total = sum([int(i!=j) for i,j in zip(first_string, second_string)])
    print(total)

    # compare second string to next string


def main():
    # Initialize variables
    inputFile="d:\\DL\\input02.txt"
    inputList = []
    # read inputfile, strip newline and store in inputList
    inputList = [inputTxt.strip() for inputTxt in open(inputFile, "r").readlines()] 
    # print number of items in list
      
    compareLetters(inputList) 

    lookupLetters(inputList)

if __name__ == "__main__":
    main()
