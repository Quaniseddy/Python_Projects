# Written by Quan Zhang for COMP9021
#
# Identifies in a grid the rhombuses (of any size)
# that are not included in any other rhombus.
#
# This is a rhombus of size 1:
#        *
#      *   *
#        *
#
# This is a rhombus of size 2:
#        *
#      *   *
#    *       *
#      *   *
#        *


from collections import defaultdict
from random import seed, randrange
import sys
import numpy as np
import math


def display_grid():
    print("  ", "-" * (2 * dim + 3))
    for row in grid:
        print("   |", *row, "|")
    print("  ", "-" * (2 * dim + 3))


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
seed(for_seed)
grid = [
    ["*" if randrange(density) != 0 else " " for _ in range(dim)] for _ in range(dim)
]
print("Here is the grid that has been generated:")
display_grid()

results = defaultdict(list)

grid = np.array(grid)


# function to find the largest possible rhombus of a given point with the predicted largest size
def find_largest(i, j, size):
    n = 0
    l = (i, j)
    r = (i, j)
    for s in range(1, size + 1):
        if grid[i + s, j - s] == "*" and grid[i + s, j + s] == "*":
            if grid[i + s + s, j] == "*":
                if s == 1:
                    n = s
                else:
                    for h in range(1, s):
                        if (
                            grid[i + s + s - h, j - h] != "*"
                            or grid[i + s + s - h, j + h] != "*"
                        ):
                            break
                        if (
                            h == s - 1
                            and grid[i + s + s - h, j - h] == "*"
                            and grid[i + s + s - h, j + h] == "*"
                        ):
                            n = s
        else:
            break
    return n


# function to check if the given top point rhombus is included in any other found rhombuses
def included(i, j, n):
    c1 = (i + n, j)
    flag = False
    for size in sorted(results, reverse=True):
        for x, y in results[size]:
            c2 = (x + size, y)
            d = math.dist(c1, c2)
            if d + n > size:
                flag = False
            else:
                return True
    return flag


# check all the point in grid
for i in range(dim - 2):
    for j in range(1, dim - 1):
        if grid[i, j] == "*":
            posi_size = min((dim - i - 3) // 2 + 1, min(j, dim - j - 1))
            n = find_largest(i, j, posi_size)
            if n != 0:
                if not included(i, j, n):
                    results[n].append((i, j))


print("Here are the rhombuses that are not included in any other:")
for size in sorted(results):
    print(f"Of size {size}:")
    for i, j in results[size]:
        print(f"  - with top vertex at location ({i}, {j})")
