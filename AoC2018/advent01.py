# This is day 1 of Advent of code 2018
# Starting at 0(zero) apply all the numbers from input.txt
# and display end result.

# read file from d:\DL\input.txt

import os
import operator

def buildFrequencyTable(FreqList):
    calculatedFrequency = 0
    FrequencyTable = []
    for item in FreqList:
        sign = item[0]
        number = int(item[1:])
        allowed_operators={
        "+": operator.add,
        "-": operator.sub}
        calculatedFrequency=allowed_operators[sign](calculatedFrequency,number)
        # Store each calculatedFrequency in the FrequencyTable
        FrequencyTable.append(calculatedFrequency)
    return FrequencyTable

def checkFrequencyDouble(inpList, FreqTable):
    # process inpList over and over until frequency is found
    # that is in the FreqTable
    calculatedFrequency = FreqTable[-1]
    doubleFreq = None
    while doubleFreq is None:
        for item in inpList:
            sign = item[0]
            number = int(item[1:])
            allowed_operators={
            "+": operator.add,
            "-": operator.sub}
            calculatedFrequency=allowed_operators[sign](calculatedFrequency,number)
            if calculatedFrequency in FreqTable:
                doubleFreq = calculatedFrequency
                return doubleFreq

def calcFrequency(FreqList):
    calculatedFrequency = 0
    for item in FreqList:
        sign = item[0]
        number = int(item[1:])
        allowed_operators={
        "+": operator.add,
        "-": operator.sub}
        calculatedFrequency=allowed_operators[sign](calculatedFrequency,number)
    return calculatedFrequency 


def main():
    # Initialize variables
    inputFile="d:\\DL\\input.txt"
    inputList = []
    # read inputfile, strip newline and store in inputList
    inputList = [inputTxt.strip() for inputTxt in open(inputFile, "r").readlines()] 
    # Create Frequency Table from the inputList 
    FrequencyTable=buildFrequencyTable(inputList)
    # print the last calculated Frequency 
    print(f'The last calculated frequency, after one process round, is {FrequencyTable[-1]}')
    # Check for recurring frequency
    print(f'The double frequency found is {checkFrequencyDouble(inputList,FrequencyTable)}')

if __name__ == "__main__":
    main()
