import sys


def get_simplified_path(path):
    stack = []
    path = path.split("/")

    for item in path:
        if item == "..":
            if stack: stack.pop()
        elif item and item != ".":
            stack.append(item)
    return "/" + "/".join(stack)


# path = input()
# get_simplified_path("/home/")
# for line in sys.stdin:
#     print(get_simplified_path(line))


def base_convert(from_base, number, to_base):
    convert_dict = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "a": 10,
        "b": 11,
        "c": 12,
        "d": 13,
        "e": 14,
        "f": 15,
        "g": 16,
        "h": 17,
        "i": 18,
        "j": 19,
        "k": 20,
        "l": 21,
        "m": 22,
        "n": 23,
        "o": 24,
        "p": 25,
        "q": 26,
        "r": 27,
        "s": 28,
        "t": 29,
        "u": 30,
        "v": 31,
        "w": 32,
        "x": 33,
        "y": 34,
        "z": 35
    }
    number = str(number)

    ten_number = 0
    base = 0
    for i in range(len(number) - 1, -1, -1):
        ten_number += convert_dict.get(number[i]) * (from_base ** base)
        base += 1

    res_list = []
    while ten_number:
        num = ten_number % to_base
        ten_number = ten_number // to_base
        res_list = [num] + res_list

    print(res_list)
    return int("".join([str(i) for i in res_list]))


print(base_convert(10, "100", 7))

