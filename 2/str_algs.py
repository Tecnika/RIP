import math


def rev(string):
    new = ""
    for i in range(len(string) - 1, -1, -1):
        new += string[i]
    return new


string = "Hello, World!"
print(rev(string))