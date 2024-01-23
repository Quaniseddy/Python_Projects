# Written by Quan Zhang for COMP9021
#
# Prompts the user for two capitalised strings of letters,
# say s1 and s2, then for two years in the range 1947--2021,
# say Y1 and Y2, with s1 and s2 and with Y1 and Y2 being separated
# by at least one space, and with possibly any extra spaces
# between s1 and s2, between Y1 and Y2, at the start of either input,
# and at the end of either input.
# - s1 can be lexicographically smaller than or equal to s2
#   or the other way around;
# - Y1 can be smaller than or equal to Y2 or the other way around.
#
# Outputs an error message if input is incorrect.
# Otherwise, finds out amongst the names that are lexicographically
# between the first name that starts with s1
# and the last name that starts with s2, which name has been given
# as both a female name and a male name in a year between Y1 and Y2
# included. If there is such a name and year, then outputs all such
# names and years for which the absolute value of the difference
# between
# - the ratio defined as the count of the name as a female name
#   in that year over the count of all female names in that year,
# - the ratio defined as the count of the name as a male name
#   in that year over the count of all male names in that year,
# is minimal (so essentially, the popularities in that year
# of the name as a female name and of the name as a male name
# are as close as possible).
# Outputs the name, the year, and both ratios as percentages
# printed out with 5 digits after the decimal point.
# In case there are many solutions (that is, same minimal
# difference in popularities), then outputs all solutions
# in increasing lexicographic order of names, and for
# a given name, in increasing order of years.
#
# The directory named names is stored in the working directory.
#
# IF YOU USE ABSOLUTE PATHS, YOUR PROGRAM CAN ONLY FAIL TO RUN PROPERLY
# ON MY MACHINE AND YOU WILL SCORE 0 TO THE QUIZ, WITH NO CHANCE FOR YOU
# TO FIX THIS MISTAKE AFTER RESULTS HAVE BEEN RELEASED.
#
# YOU CANNOT USE pandas FOR THIS QUIZ; IF YOU DO, YOU WILL SCORE 0
# TO THE QUIZ.


from collections import defaultdict
from pathlib import Path
import csv
import sys


s0 = input("Enter two capitalised strings of letters: ")
s0 = sorted(s0.split())
# initialise checks to handle exceptions
check1 = False
check2 = False

if (len(s0) <= 1) or (len(s0) > 2):
    print("Incorrect input, leaving it there.")
else:
    s1, s2 = s0[0], s0[1]
    if s1.istitle() and s2.istitle():
        check1 = True
    else:
        print("Incorrect input, leaving it there.")

# when the first check passed
if check1 == True:
    y0 = input("Enter two integers between 1947 and 2021: ")
    y0 = sorted(y0.split())
    if (len(y0) <= 1) or (len(y0) > 2):
        print("Incorrect input, leaving it there.")
    else:
        y1, y2 = int(y0[0]), int(y0[1])
        if y1 in range(1947, 2022) and y2 in range(1947, 2022):
            check2 = True
        else:
            print("Incorrect input, leaving it there.")

#when the second check passed 
if check2 == True:
    names_dirname = Path("names")
    if not names_dirname.exists():
        print(f"There is no directory named {names_dirname}, giving up...")
        sys.exit()
    results = []
    min_diff = 1
    for filename in sorted(names_dirname.glob("*.txt")):
        year = int(filename.name[3:7])
        if year in range(y1, y2 + 1):
            with open(filename) as file:
                csv_file = sorted(csv.reader(file))
                flag = False
                name_dic = defaultdict(list)
                male_total = 0
                female_total = 0
                for name, gender, count in csv_file:
                    if gender == "F":
                        female_total = female_total + int(count)
                    else:
                        male_total = male_total + int(count)
                    if name > s2:
                        flag = False
                    if name.startswith(s1) and name < s2:
                        flag = True
                    if name.startswith(s2):
                        flag = True
                    if flag == True:
                        name_dic[name].append((name, gender, count))

                for x in name_dic.values():
                    if len(x) > 1:
                        if x[0][1] == "F":
                            female_ratio = int(x[0][2]) / female_total
                            male_ratio = int(x[1][2]) / male_total
                        else:
                            female_ratio = int(x[1][2]) / female_total
                            male_ratio = int(x[0][2]) / male_total

                        diff = abs(female_ratio - male_ratio)
                        if diff < min_diff:
                            min_diff = diff
                            result = (
                                x[0][0],
                                year,
                                male_ratio * 100,
                                female_ratio * 100,
                            )
                            results = []
                            if result not in results:
                                results.append(result)
                        if diff == min_diff and result not in results:
                            results.append(result)

    if results == []:
        print("No name was given as both female and male names.")
    elif len(results) == 1:
        print(
            "Here are the names that were given as both\nfemale and male names, for the smallest difference\nof ratio as a female name over all female names\nand ratio as a male name over all male names,\nfor the years when that happened:"
        )
        print(
            "  "
            + result[0]
            + " in "
            + str(result[1])
            + ", for ratios of\n"
            + "    - "
            + ("%.5f" % result[3])
            + "% as a female name,\n"
            + "    - "
            + ("%.5f" % result[2])
            + "% as a male name."
        )
    else:
        for result in sorted(results):
            print(
                "Here are the names that were given as both\nfemale and male names, for the smallest difference\nof ratio as a female name over all female names\nand ratio as a male name over all male names,\nfor the years when that happened:"
            )
            print(
                "  "
                + result[0]
                + " in "
                + str(result[1])
                + ", for ratios of\n"
                + "    - "
                + ("%.5f" % result[3])
                + "% as a female name,\n"
                + "    - "
                + ("%.5f" % result[2])
                + "% as a male name."
            )
