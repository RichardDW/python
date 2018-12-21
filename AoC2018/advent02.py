from collections import Counter
import difflib as diff


def compare_letters(inpList):
    has1 = 0
    has2 = 0
    has3 = 0
    for letters in inpList:
        my_counter=Counter(letters).values()
        # print(my_counter)
        # check if there is a 2 or 3 value
        # since there are single characters in each line, the
        # total of enen must be the same as number of lines in inpList.
        has1 += 1 in my_counter
        has2 += 2 in my_counter
        has3 += 3 in my_counter

    print(f'ones are with {has1}, twos are with {has2} and threes are with {has3}')
    return has2 * has3


def lookup_letters(inpList):
    # compare first string to second string, then 3rd string until last string
    # compare a with b
    inner = 1
    outer = 0
    maximum = len(inpList)
    print(maximum)

    first_string = inpList[outer]
    second_string = inpList[inner]
    print(f'{first_string}\n{second_string}')
    # d = diff.Differ()
    # result = d.compare(first_string, second_string)
    # print(result)
    total = sum([int(i != j) for i, j in zip(first_string, second_string)])
    print(total)

    # compare second string to next string


def main():
    # Initialize variables
    input_file = "d:\\DL\\input02.txt"
    # read input_file, strip newline and store in inputList
    input_list = [inputTxt.strip() for inputTxt in open(input_file, "r").readlines()]
    # print number of items in list
      
    print(compare_letters(input_list))

    #lookup_letters(input_list)


if __name__ == "__main__":
    main()
