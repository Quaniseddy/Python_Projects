# Written by Quan Zhang for COMP9021
#
# Implements a function that takes as argument a string
# consisting of arrows pointing North, East, South or West.
#
# Following the provided directions,
# - if the exploration gets back to the starting point, then this
#   common location will be represented by a black circle;
# - otherwise, the starting point will be represented by a blue circle
#   and the final destination by a red circle.

# All other visited locations will be represented by a square, of colour:
# - yellow if visited exactly once, 6 times, 11 times, 16 times...
# - orange if visited exactly twice, 7 times, 12 times, 17 times...
# - brown if visited exactly trice, 8 times, 13 times, 18 times...
# - green if visited exactly 4 times, 9 times, 14 times, 19 times...
# - purple if visited exactly 5 times, 10 times, 15 times, 20 times...

# The explored area is displayed within the smallest rectangle in
# which it fits; all unvisited locations within that rectangle are
# represented by white squares.
#
# The code points of the characters involved in this quiz are:
# 9899, 11036, 128308, 128309, 128999, 129000, 129001, 129002, 129003


def explore_this_way(directions):
    symbols = {
        0: "\u2b1c",
        1: "\U0001f7e8",
        2: "\U0001f7e7",
        3: "\U0001f7eb",
        4: "\U0001f7e9",
        5: "\U0001f7ea",
        -1: "\U0001f535",
        -2: "\U0001F534",
        -3: "\u26AB",
    }
    x = max_x = min_x = y = max_y = min_y = 0
    for i in range(len(directions)):
        if directions[i] == "\u2b06":
            y = y + 1
            if y > max_y:
                max_y = y
        elif directions[i] == "\u2b07":
            y = y - 1
            if y < min_y:
                min_y = y
        elif directions[i] == "\u2b95":
            x = x + 1
            if x > max_x:
                max_x = x
        else:
            x = x - 1
            if x < min_x:
                min_x = x

    x_diff = max_x - min_x
    y_diff = max_y - min_y
    table = [[0 for w in range(x_diff + 1)] for h in range(y_diff + 1)]
    if min_x == 0:
        start = (max_y, 0)
    else:
        start = (max_y, -min_x)

    r, c = start[0], start[1]

    for j in range(len(directions)):
        if directions[j] == "\u2b06":
            r = r - 1
        if directions[j] == "\u2b07":
            r = r + 1
        if directions[j] == "\u2b95":
            c = c + 1
        if directions[j] == "\u2b05":
            c = c - 1
        table[r][c] += 1

    end = r, c
    table[r][c] = -2
    table[start[0]][start[1]] = -1
    if end == start:
        table[r][c] = -3

    for o in range(y_diff + 1):
        for p in range(x_diff + 1):
            root = table[o][p]
            if root > 0:
                if root % 5 != 0:
                    print(symbols[root % 5], end="")
                else:
                    print(symbols[5], end="")
            else:
                print(symbols[root], end="")
        print()
