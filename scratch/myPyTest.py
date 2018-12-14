def Galatz(myNum):
    try:
        print(myNum)
        return myNum * 5

    except:
        print("Please enter an integer..")


# def main():
# get input from user
# pass input to Galatz function
try:
    mynum = int(input("Plz enter a number: "))
except ValueError:
    print("Please enter an integer...")

a = Galatz(mynum)
print(a)
""" 
myNumInput = int(input('Give number')
myret = Galatz(myNumInput)
print(myret) """

# if __name__ == "__main__":
#    main()

