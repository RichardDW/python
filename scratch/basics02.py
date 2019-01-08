import itertools

counter = itertools.count()

# infinite loop
for num in counter:
    print(num)

# each print will print next number
print(next(counter))

# the zip function pairs data
data = [100, 200, 300, 400]
daily_data = zip(itertools.count(), data)
# or convert to a list right away
daily_data = list(zip(itertools.count(), data))


def squared(x):
    return x * x


for i in range(10):
    print("{} squared is {}".format(i, squared(i)))
    print(f"{i} squared is {squared}.")

n = int(input())
for i in range(0,n):
    print(i*i)

