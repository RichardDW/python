def main():
    print("hello world")


# Fizz Buzz
for num in range(1,101):
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


# Fibonacci sequence
a, b = 0, 1
for i in range(0,20):
    print(a)
    a, b = b, a + b




if __name__ == "__main__":
    main()
