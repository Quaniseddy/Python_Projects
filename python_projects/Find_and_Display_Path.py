# Written by Quan Zhang ID:z5089022 for COMP9021
#
# Prompts the user for a ranking of the four horizontal and vertical
# directions, ⬆, ⮕, ⬇ and ⬅, from most preferred to least
# preferred, say d1, d2, d3 and d4.
#
# Determines the path that goes from a given point to another given
# point by following stars in a grid, provided that is possible,
# the path being uniquely defined by the following condition:
# to go from A to B,
# - if it is possible to start taking direction d1,
#   then the path from A to B starts by taking direction d1;
# - otherwise, if it is possible to start taking direction d2,
#   then the path from A to B starts by taking direction d2;
# - otherwise, if it is possible to start taking direction d3,
#   then the path from A to B starts taking direction d3;
# - otherwise, if it is possible to start taking direction d4,
#   then the path from A to B starts by taking direction d4.
#
# The grid and the path, if it exists, are output,
# - the endpoint of the path being represented by a red circle;
# - taking direction North being represented by a yellow square;
# - taking direction East being represented by a brown square;
# - taking direction South being represented by a green square;
# - taking direction West being represented by a purple square;
# - points not on the path being represented by black and white
#   squares depending on whether they are or not occupied by a star.
# (All these characters have been used in quiz 3.)
#
# Also outputs the length of the path, if it exists.


from random import seed, randrange
import sys

# default settings of dimension and symbols representation
dim = 10
symbols = {
    0: "\u2b1c",
    1: "\u2b1b",
    "⬆": "\U0001f7e8",
    "⮕": "\U0001f7eb",
    "⬇": "\U0001f7e9",
    "⬅": "\U0001f7ea",
    -2: "\U0001F534",
}
length = 1


def display_grid():
    print("   ", "-" * (2 * dim + 1))
    for i in range(dim):
        print(
            "   |", " ".join("*" if grid[i][j] else " " for j in range(dim)), end=" |\n"
        )
    print("   ", "-" * (2 * dim + 1))


# BFS to chekc if there is a possible path between given start point from previous point and end point
def check(s, start, end):
    Dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    queue = []
    queue.append(start)
    tmp_grid = [row[:] for row in grid]
    while len(queue) > 0:
        if end in queue:
            return True

        p = queue[0]
        queue.pop(0)
        tmp_grid[p[0]][p[1]] = 0

        for i in range(4):
            a = p[0] + Dir[i][0]
            b = p[1] + Dir[i][1]

            if (
                a >= 0
                and b >= 0
                and a < dim
                and b < dim
                and tmp_grid[a][b] == 1
                and s != [a, b]
            ):
                queue.append([a, b])
    return False


# recursion function to recursively find the next move as required
def connect(start, end):
    global length
    if grid[start[0]][start[1]] != 1 or grid[end[0]][end[1]] != 1:
        print("There is no path joining both points.")
    elif start == end:
        grid[end[0]][end[1]] = -2
        print("There is a path joining both points, of length " + str(length) + ":")
        for i in grid:
            print("    " + "".join(symbols[j] for j in i))
    else:
        for d in direction_preferences:
            if d == "⬆":
                tmp_start = [start[0] - 1, start[1]]
            if d == "⮕":
                tmp_start = [start[0], start[1] + 1]
            if d == "⬇":
                tmp_start = [start[0] + 1, start[1]]
            if d == "⬅":
                tmp_start = [start[0], start[1] - 1]

            if (
                0 <= tmp_start[0]
                and tmp_start[0] < dim
                and 0 <= tmp_start[1]
                and tmp_start[1] < dim
                and grid[tmp_start[0]][tmp_start[1]] == 1
            ):
                if check(start, tmp_start, end):
                    grid[start[0]][start[1]] = d
                    start = tmp_start
                    length = length + 1
                    break

        if grid[tmp_start[0]][tmp_start[1]] == 0:
            print("There is no path joining both points.")
        else:
            connect(start, end)


try:
    for_seed, density, dim = (
        int(x)
        for x in input(
            "Enter three integers, "
            "the second and third ones "
            "being strictly positive: "
        ).split()
    )
    if density <= 0 or dim <= 0:
        raise ValueError
except ValueError:
    print("Incorrect input, giving up.")
    sys.exit()
try:
    start = [int(x) for x in input("Enter coordinates " "of start point:").split()]
    if len(start) != 2 or not (0 <= start[0] < dim) or not (0 <= start[1] < dim):
        raise ValueError
except ValueError:
    print("Incorrect input, giving up.")
    sys.exit()
try:
    end = [int(x) for x in input("Enter coordinates " "of end point:").split()]
    if len(end) != 2 or not (0 <= end[0] < dim) or not (0 <= end[1] < dim):
        raise ValueError
except ValueError:
    print("Incorrect input, giving up.")
    sys.exit()
direction_preferences = input(
    "Input the 4 directions, from most " "preferred to least preferred:"
)
if set(direction_preferences) != {"⬆", "⮕", "⬇", "⬅"}:
    print("Incorrect input, giving up.")
    sys.exit()

seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)] for _ in range(dim)]
print("Here is the grid that has been generated:")
display_grid()
print()
connect(start, end)
