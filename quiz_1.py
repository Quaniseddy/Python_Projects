# Written by Quan Zhang for COMP9021
#
# Prompts the user for an integer at least equal to 3 and for the
# name of a file, assumed to be stored in the working directory.
#
# The file can contain anywhere any number of blank lines
# (that is, lines containing an arbitrary number of spaces
# and tabs--an empty line being the limiting case).
#
# Nonblank lines are always of the form:
#                Give me that_many characters
# with any number of spaces at the beginning and at the end of the line
# (possibly none) and with at least one space between successive words,
# where that_many is one of 2, 3, 4, 5, 6, 7, 8 or 9
# and where characters is one of dashes, stars, carets or dollars.
#
# Outputs text and "pictures" based on the provided input.
#
# Tip: Use a dictionary that maps 2 to the word two, 3 to the word three...
#      Use another dictionary that maps the word dashes to the character -,
#      the word stars to the character *...


import sys
from os.path import exists

try:
    size = int(input("Enter an integer at least equal to 3: "))
    if size < 3:
        raise ValueError
except ValueError:
    print("Incorrect input, giving up.")
    sys.exit()
file_name = input(
    "Input the name of a file " "in the working directory: "
).removesuffix("\n")
if not exists(file_name):
    print("Incorrect input, giving up.")
    sys.exit()


# to decode number into English word and print them out
def decode(line):
    x = line.split()
    num = {
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }
    print("Here are your " + num.get(int(x[2])) + " " + x[3] + ":")
    sum = "    "
    while int(x[2]) > 0:
        if x[3] == "carets":
            sum = sum + "^ "
        elif x[3] == "stars":
            sum = sum + "* "
        elif x[3] == "dollars":
            sum = sum + "$ "
        else:
            sum = sum + "- "
        x[2] = str(int(x[2]) - 1)
    sum = sum[: len(sum) - 1]
    print(sum)


print("Here is your coffee table of size " + str(size) + ":")
line1 = "     "
line2 = "    /|"
line3 = "    "
line4 = "    |"
while size > 0:
    line1 = line1 + "-"
    line3 = line3 + "-"
    if size > 2:
        line2 = line2 + " "
        line4 = line4 + " "
    size = size - 1
line2 = line2 + "/|"
line4 = line4 + "|"
print(line1)
print(line2)
print(line3)
print(line4)
print()

file = open(file_name)
for line in file:
    if line.strip():
        decode(line)
