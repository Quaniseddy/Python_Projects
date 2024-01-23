import numpy as np
import math
from collections import defaultdict
import cProfile


# default length for perimeter calculation
def perimeter_map(k):
    para_map = {
        0: "b",
        1: 0.4,
        2: "b",
        3: 0.4,
        4: "b",
        5: 0.4,
        6: "b",
        7: 0.4,
    }
    return para_map[k]


# direction map:
#   w   u   n
#   l   *   r
#   s   d   e
def get_neigbors(x, y, dir):
    neigbors_map = {
        "w": (x - 1, y - 1),
        "u": (x - 1, y),
        "n": (x - 1, y + 1),
        "r": (x, y + 1),
        "e": (x + 1, y + 1),
        "d": (x + 1, y),
        "s": (x + 1, y - 1),
        "l": (x, y - 1),
    }
    neigbors = []
    for order in dir:
        neigbors.append(neigbors_map[order])
    return neigbors


# get the new directions order according to previous move
def get_directions(n):
    dir_mode = {
        4: "unredslw",
        5: "nredslwu",
        6: "redslwun",
        7: "edslwunr",
        0: "dslwunre",
        1: "slwunred",
        2: "lwunreds",
        3: "wunredsl",
    }
    return dir_mode[n]


# For Depth Calculation
# Check if two points cut though the line or is a V shape which does not cut through the line
def point_check(grid, x, y, popos, u, l, p):
    this_poly = popos[int(grid[x, y]) - 1]
    index = this_poly.p.index((x, y))
    if index == 0:
        before = this_poly.p[-1]
        after = this_poly.p[1]
    elif index == len(this_poly.p) - 1:
        before = this_poly.p[index - 1]
        after = this_poly.p[0]
    else:
        before = this_poly.p[index - 1]
        after = this_poly.p[index + 1]

    if before in u and after in l:
        return [True]
    if before in l and after in u:
        return [True]
    if before in u and after in p:
        return [False, "u"]
    if before in l and after in p:
        return [False, "d"]
    if before in p and after in u:
        return [False, "u"]
    if before in p and after in l:
        return [False, "d"]
    return [False, "no"]


# For Depth Calculation
# Check for if the points are a line
def not_just_sitting_check(grid, x, y, popos):
    upper_neigbors = get_neigbors(x, y, "wun")
    lower_neigbors = get_neigbors(x, y, "sde")
    para_neigbors = get_neigbors(x, y, "lr")
    up_flag = False
    low_flag = False
    for up in upper_neigbors:
        if grid[up] == grid[x, y]:
            up_flag = True
    for low in lower_neigbors:
        if grid[low] == grid[x, y]:
            low_flag = True

    flag_3 = point_check(
        grid, x, y, popos, upper_neigbors, lower_neigbors, para_neigbors
    )
    if all([up_flag, low_flag, flag_3[0]]):
        return (True, "no")
    else:
        if len(flag_3) > 1:
            return (False, flag_3[1])
        return (False, "no")


# Find the depth of Current Polygons by "drawing a line" to the dimension border and check for all cross points
def find_depth(poly, grid, popos):
    edge_1 = poly.edges[0]
    line = []
    tmp_watch = "no"
    tmp_cord = "no"
    for d in range(edge_1[1]):
        if grid[edge_1[0], d] != "0":
            (result, watch) = not_just_sitting_check(grid, edge_1[0], d, popos)
            if result:
                line.append(grid[edge_1[0], d])
            else:
                if watch != "no":
                    if tmp_watch == "no" and tmp_cord == "no":
                        tmp_watch = watch
                        tmp_cord = grid[edge_1[0], d]
                    else:
                        if tmp_cord == grid[edge_1[0], d]:
                            if tmp_watch != watch:
                                line.append(grid[edge_1[0], d])
                        else:
                            tmp_cord = grid[edge_1[0], d]
                            tmp_watch = watch
    depth = 0
    for e in range(len(line)):
        occur = 0
        for f in range(len(line)):
            if line[e] == line[f]:
                occur += 1
        if occur % 2 != 0:
            depth += 1
    return depth


# Checking the number of invariantion by comparing edges of the polygon
def num_of_invariation(poly):
    dist = ""
    one = poly.edges[0]
    for p in poly.edges:
        if p != one:
            dist += str(math.dist(one, p))
            one = p
    dist += str(math.dist(one, poly.edges[0]))

    i = (dist + dist).find(dist, 1, -1)
    if i == -1:
        return 1
    else:
        return len(dist) / len(dist[:i])


# function to calculation cross product of two points
def CrossProduct(A):
    X1 = A[1][0] - A[0][0]
    Y1 = A[1][1] - A[0][1]
    X2 = A[2][0] - A[0][0]
    Y2 = A[2][1] - A[0][1]
    return X1 * Y2 - Y1 * X2


# check if the polygon is convex or not by calculating cross product of all points
def con_or_non(poly):
    points = poly.p
    L = len(points)
    prev = 0
    curr = 0

    for i in range(L):
        temp = [points[i], points[(i + 1) % L], points[(i + 2) % L]]
        curr = CrossProduct(temp)
        if curr != 0:
            if curr * prev < 0:
                return False
            else:
                prev = curr
    return True


# function to calculate the area of polygon using Shoelace Formula
def area(poly):
    x = []
    y = []
    for v in poly.p:
        x.append(v[0])
        y.append(v[1])
    x = np.array(x)
    y = np.array(y)
    correction = x[-1] * y[0] - y[-1] * x[0]
    main_area = np.dot(x[:-1], y[1:]) - np.dot(y[:-1], x[1:])
    return 0.16 * 0.5 * np.abs(main_area + correction)


# BFS check of path
def check(grid, s, start, end):
    Dir = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]
    queue = set()
    queue.add(start)
    visited = set()
    visited.add(s)
    while queue:
        if end in queue:
            return True

        p = queue.pop()
        visited.add(p)

        for i in range(8):
            a = p[0] + Dir[i][0]
            b = p[1] + Dir[i][1]

            if grid[a][b] == "*" and (a, b) not in visited:
                queue.add((a, b))
    return False


# recursive call to find all possible polygons
def find_poly(pol, grid, start, end, dir):
    if start == end:
        grid[start] = str(pol.number)
        pol.p.append(end)
        neinei = get_neigbors(start[0], start[1], "wunredsl")
        if get_directions(neinei.index(pol.p[0])) != dir:
            pol.edges.append(end)
    else:
        neigbors = get_neigbors(start[0], start[1], dir)
        deafult_neigbors = get_neigbors(start[0], start[1], "wunredsl")
        new_neigbors = []

        for neigbor in neigbors:
            if grid[neigbor] == "*" and check(grid, start, neigbor, end):
                grid[start] = str(pol.number)
                curr_index = deafult_neigbors.index(neigbor)
                tmp_dir = get_directions(curr_index)
                if tmp_dir != dir:
                    pol.edges.append(start)
                pol.p.append(start)
                if perimeter_map(curr_index) != "b":
                    pol.perimeter[0] += perimeter_map(curr_index)
                else:
                    pol.perimeter[1] += 1
                start = neigbor
                dir = tmp_dir
                new_neigbors.append(neigbor)
                break
        if new_neigbors == []:
            raise PolygonsError("Cannot get polygons as expected.")
        else:
            find_poly(pol, grid, start, end, dir)


# define a default polygon class with all the attribute required and a number indicating the order of finding
class Polygon:
    def __init__(
        self,
        number=0,
        points=[],
        edges=[],
        perimeter=[0, 0],
        area=0,
        depth=0,
        convex=None,
        num_invariation=0,
    ):
        self.number = number
        self.p = points
        self.edges = edges
        self.perimeter = perimeter
        self.area = area
        self.depth = depth
        self.convex = convex
        self.num_invariation = num_invariation


class PolygonsError(Exception):
    pass


# when a polygons classed is defined the initial grid from a txt file will be scanned
class Polygons:
    def __init__(self, file_name):
        num_of_poly = 0
        self.file_name = file_name[:-3]
        with open(file_name) as file:
            popos = []
            grid = []
            max = -1
            min = 9999
            digits_count = []
            for line in file:
                if line.strip():
                    line = "".join(line.strip().split())
                    row = []
                    for n in line:
                        if n == "0" or n == "1":
                            row.append("*") if n == "1" else row.append(n)
                        else:
                            raise PolygonsError("Incorrect input.")

                    if len(row) < 2 or len(row) > 50:
                        raise PolygonsError("Incorrect input.")
                    else:
                        digits_count.append(len(row))
                        grid.append(row)

        if len(grid) < 2 or len(grid) > 50:
            raise PolygonsError("Incorrect input.")
        if len(set(digits_count)) != 1:
            raise PolygonsError("Incorrect input.")

        # After handling exception and invalid format the grid is then been analysed and replaced 1s with the polygon number
        grid = np.array(grid, dtype="U25")
        (x, y) = grid.shape
        grid = np.pad(grid, [(1, 1), (1, 1)], mode="constant")
        starting_dir = "wunredsl"
        for i in range(1, x + 1):
            for j in range(1, y + 1):
                if grid[i, j] == "*":
                    neigbors = get_neigbors(i, j, starting_dir)
                    new_neigbors = []
                    for point in neigbors:
                        if grid[point] == "*":
                            new_neigbors.append(point)
                    if len(new_neigbors) < 2:
                        raise PolygonsError("Cannot get polygons as expected.")
                    else:
                        num_of_poly += 1
                        grid[i, j] = num_of_poly
                        start = new_neigbors[0]
                        end = new_neigbors[-1]
                        start_index = neigbors.index(start)
                        end_index = neigbors.index(end)
                        direction = get_directions(start_index)
                        pol = Polygon(points=[], edges=[], perimeter=[0, 0])
                        pol.number = num_of_poly
                        pol.p.append((i, j))
                        pol.edges.append((i, j))
                        if perimeter_map(start_index) != "b":
                            pol.perimeter[0] += perimeter_map(start_index)
                        else:
                            pol.perimeter[1] += 1
                        if perimeter_map(end_index) != "b":
                            pol.perimeter[0] += perimeter_map(end_index)
                        else:
                            pol.perimeter[1] += 1
                        find_poly(pol, grid, start, end, direction)
                        pol.area = round(area(pol), 2)
                        if pol.area > max:
                            max = pol.area
                        if pol.area < min:
                            min = pol.area
                        pol.convex = "yes" if con_or_non(pol) else "no"
                        pol.num_invariation = int(num_of_invariation(pol))
                        pol.depth = find_depth(pol, grid, popos)
                        popos.append(pol)
        self.max = max
        self.min = min
        self.grid = grid[1:-1, 1:-1]
        self.popos = popos

    # analyse will just print the information in desired format since the actual analyse has been done and stored in Polygons Class
    def analyse(self):
        for p in self.popos:
            print(f"Polygon {p.number}:")
            if p.perimeter[1] == 0:
                print(f"    Perimeter: {round(p.perimeter[0],1)}")
            else:
                if p.perimeter[0] != 0:
                    print(
                        f"    Perimeter: {round(p.perimeter[0],1)} + {p.perimeter[1]}*sqrt(.32)"
                    )
                else:
                    print(f"    Perimeter: {p.perimeter[1]}*sqrt(.32)")
            print(f"    Area: {format(p.area, '.2f')}")
            print(f"    Convex: {p.convex}")
            print(f"    Nb of invariant rotations: {p.num_invariation}")
            print(f"    Depth: {p.depth}")

    # create a tex file with the desired format
    def display(self):
        name = self.file_name + "tex"
        f = open(name, "w")
        f.write(
            "\documentclass[10pt]{article}\n\\usepackage{tikz}\n\\usepackage[margin=0cm]{geometry}\n\\pagestyle{empty}\n\n\\begin{document}\n\n\\vspace*{\\fill}\n\\begin{center}\n\\begin{tikzpicture}[x=0.4cm, y=-0.4cm, thick, brown]\n"
        )
        (r, c) = self.grid.shape
        s = f"\\draw[ultra thick] (0, 0) -- ({str(c-1)}, 0) -- ({str(c-1)}, {str(r-1)}) -- (0, {str(r-1)}) -- cycle;\n\n"
        f.write(s)
        dict = defaultdict(list)
        diff = self.max - self.min
        for p in self.popos:
            if diff != 0:
                portion = abs((self.max - p.area) / diff * 100)
                portion = int(round(portion, 0))
            else:
                portion = 0
            points = " -- ".join(f"({point[1]-1}, {point[0]-1})" for point in p.edges)
            s = f"\\filldraw[fill=orange!{portion}!yellow] " + points + " -- cycle;\n"
            dict[p.depth].append(s)

        for dep in sorted(dict):
            comment = f"% Depth {dep}\n"
            f.write(comment)
            for content in dict[dep]:
                f.write(content)

        f.write(
            "\\end{tikzpicture}\n\\end{center}\n\\vspace*{\\fill}\n\n\\end{document}\n"
        )


# tests I have put in code to test the running time while coding
# cProfile.run('poly = Polygons("poly_1.txt") \nprint(poly.grid) \npoly.analyse()')
