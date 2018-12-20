# This is day 1 of Advent of code 2018
# Starting at 0(zero) apply all the numbers from input.txt
# and display end result.

# read file from d:\DL\input.txt

import operator


def build_frequency_table(FreqList):
    calculated_frequency = 0
    frequency_table = []
    for item in FreqList:
        sign = item[0]
        number = int(item[1:])
        allowed_operators={
        "+": operator.add,
        "-": operator.sub}
        calculated_frequency=allowed_operators[sign](calculated_frequency,number)
        # Store each calculated_frequency in the frequency_table
        frequency_table.append(calculated_frequency)
    return frequency_table


def check_frequency_double(inpList, FreqTable):
    # process inpList over and over until frequency is found
    # that is in the FreqTable
    calculated_frequency = FreqTable[-1]
    double_freq = None
    while double_freq is None:
        for item in inpList:
            sign = item[0]
            number = int(item[1:])
            allowed_operators={
            "+": operator.add,
            "-": operator.sub}
            calculated_frequency=allowed_operators[sign](calculated_frequency,number)
            if calculated_frequency in FreqTable:
                double_freq = calculated_frequency
                return double_freq


def calc_frequency(FreqList):
    calculated_frequency = 0
    for item in FreqList:
        sign = item[0]
        number = int(item[1:])
        allowed_operators={
        "+": operator.add,
        "-": operator.sub}
        calculated_frequency=allowed_operators[sign](calculated_frequency,number)
    return calculated_frequency 


def main():
    # Initialize variables
    input_file="d:\\DL\\input.txt"
    # read input_file, strip newline and store in input_list
    input_list = [inputTxt.strip() for inputTxt in open(input_file, "r").readlines()] 
    # Create Frequency Table from the input_list 
    frequency_table=build_frequency_table(input_list)
    # print the last calculated Frequency 
    print(f'The last calculated frequency, after one process round, is {frequency_table[-1]}')
    # Check for recurring frequency
    print(f'The double frequency found is {check_frequency_double(input_list,frequency_table)}')


if __name__ == "__main__":
    main()
