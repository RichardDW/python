from collections import Counter
import difflib as diff


def compare_letters(inpList):
    enen = 0
    tween = 0
    drien = 0
    for letters in inpList:
        my_counter=Counter(letters).values()
        # print(my_counter)
        # check if there is a 2 or 3 value
        if 1 in my_counter:
            enen += 1
        if 2 in my_counter:
            tween += 1
            # print(f'there is a 2 in the list')
        if 3 in my_counter:
            drien += 1
            # print(f'there is a 3 in the list')
    print(f'enen zijn met {enen}, tween zijn met {tween} en drien zijn met zn {drien}')


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
    input_file="d:\\DL\\input02.txt"
    # read input_file, strip newline and store in inputList
    input_list = [inputTxt.strip() for inputTxt in open(input_file, "r").readlines()]
    # print number of items in list
      
    compare_letters(input_list)

    lookup_letters(input_list)


if __name__ == "__main__":
    main()
