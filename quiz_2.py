# Written by Quan Zhang for COMP9021
# ID:z5089022
# Prompts the user for the integers 0, 1... n, input
# in some order, for some natural number n,
# making up a list your_list,
# and for two integers, the second of which, say p,
# is between 0 and 10, to create a permutation of
# {0, ... p-1}, say my_list.
#
# Removes from your_list what is currently the smallest
# or largest element if it is curently the first or last
# element of the list, for as long as it can be done.
#
# Displays a picture that represents how to travel from
# 0 to p-1 in my_list, based on where they are located
# in the list.


from random import seed, shuffle
import sys


try:
    your_list = [
        int(x)
        for x in input("Enter a permutation of 0, ..., n " "for some n >= 0: ").split()
    ]
    if not your_list:
        raise ValueError
    your_list_as_set = set(your_list)
    if len(your_list_as_set) != len(your_list) or your_list_as_set != set(
        range(len(your_list))
    ):
        raise ValueError
except ValueError:
    print("Incorrect input, giving up.")
    sys.exit()
try:
    for_seed, length = (
        int(x)
        for x in input(
            "Enter two integers, " "the second one between 0 and 10: "
        ).split()
    )
    if not 0 <= length <= 10:
        raise ValueError
except ValueError:
    print("Incorrect input, giving up.")
    sys.exit()
seed(for_seed)
my_list = list(range(length))
shuffle(my_list)
print("Here is your list:")
print("  ", your_list)
print("Here is my list:")
print("  ", my_list)


def remove_list(list):
    while len(list) != 0 and (
        is_largest(list[0], list)
        or is_largest(list[-1], list)
        or is_smallest(list[0], list)
        or is_smallest(list[-1], list)
    ):
        if is_largest(list[0], list) or is_smallest(list[0], list):
            list.remove(list[0])
        elif is_largest(list[-1], list) or is_smallest(list[-1], list):
            list.remove(list[-1])


def is_largest(obj, list):
    for num in list:
        if num > obj:
            return False
    return True


def is_smallest(obj, list):
    for num in list:
        if num < obj:
            return False
    return True


print()
remove_list(your_list)
print(
    "Removing again and again the currently largest\n"
    "or smallest element in your list for as long as\n"
    "it currently starts or ends the list, we get:"
)
print(your_list)
print()
print("That's how to travel in my list:")


def travel_list(list):
    current_index = 0
    for i in range(len(list)):
        previous_index = current_index
        current_index = list.index(i)
        if i == 0:
            print("  " * current_index + str(i))
        else:
            if current_index < previous_index:
                print(
                    "  " * current_index
                    + str(i)
                    + "--" * (previous_index - current_index)
                )
            else:
                print(
                    "  " * previous_index
                    + "--" * (current_index - previous_index)
                    + str(i)
                )


travel_list(my_list)
