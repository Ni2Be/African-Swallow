import math

first = 'Python " '


last = 'test ""'

x = 3
y = 3.2

full = f"{first} new"
print(full)

print(x / y)
print(x // y)
print(2 ** 10)
print(2 + 4j, " + ", 2 + 44j, " = ", (2 + 4j) + (2 + 44j))


v = input("x: ")

print(float(v) + 33)


if float(v) <= 22 or float(v) > 44:
    print("wtf")
else:
    print("lol")

if 22 <= float(v) > 44:
    print("wtf")
else:
    print("lol")


for t in "this":
    print(t + ", ")


def calculate(left, right):
    return (left + right, left, right)  # tuple


print(calculate(3, 66))


def calc(left, right = 99) -> int:
    return left + right


print(calc(44, right = 33))


print(calc(3))

def sum(*all_nums) -> int:
    for num in all_nums:
        x = num
    return x


print(sum(2, 3, 4, 3, 2, 3))


def print_all(**args):
    print(args)
    print(args["name"])


print_all(name = "xol", num = 2, els = 4.3)


