import random
import numpy as np


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def for_test():
    for i in range(0, 10, 2):
        print(f"{i}, {i + 1}")


def range_test():
    l = [x for x in range(10) if x % 2 == 0]
    print(l)


def bits_test():
    n = 1
    n = n << 1
    n = 1 | 2
    print(n)


def random_test():
    print(random.random())
    print(random.randint(1, 10))
    print(random.randrange(1, 100, 5))
    print(random.randbytes(10))


def random_int_array(size, start, end):
    return [random.randint(start, end) for _ in range(size)]


def random_array_test():
    print(list(np.random.randint(1, 100 + 1, 10)))


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # random_array_test()

    # Example usage
    size = 10
    start = 1
    end = 100
    random.seed(42)
    random_numbers = random_int_array(size, start, end)
    print(random_numbers)

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
