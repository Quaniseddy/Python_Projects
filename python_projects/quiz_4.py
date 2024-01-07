## Written by Quan Zhang for COMP9021

# Implements a function that computes the maximum
# number of primes within a window of a given size,
# the first of which starts from a given lower bound
# and the last of which ends at a given upper bound.
# For all windows that achieve that maximum number
# within the window; outputs those two primes
# from smallest to largest first primes.

from math import sqrt


def sieve_of_primes_up_to(n):
    sieve = [True] * (n + 1)
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve


# You can assume that the function will be called with
# size a strictly positive integer,
# lower_bound an integer at least equal to 2, and
# upper_bound an integer at least equal to lower_bound.
# The function won't be tested for values of upper_bound
# greater than 10,000,000.
def primes_in_window(size, lower_bound, upper_bound):
    if size > upper_bound - lower_bound + 1:
        print("Window size is too large for these bounds,", "leaving it there.")
        return

    s = sieve_of_primes_up_to(upper_bound)[lower_bound:]
    max_num = 0
    queue = []
    for i in range(len(s) + 1 - size):
        init = s[0 + i : size + i]
        n = init.count(True)
        if n > max_num:
            max_num = n
            queue = []
            queue.append(
                (
                    lower_bound + i + init.index(True),
                    lower_bound + i + len(init) - 1 - init[::-1].index(True),
                )
            )
            continue
        if n == max_num and n != 0:
            queue.append(
                (
                    lower_bound + i + init.index(True),
                    lower_bound + i + len(init) - 1 - init[::-1].index(True),
                )
            )

    if max_num == 0:
        print("There is no prime in a window of size " + str(size) + ".")
    elif max_num == 1:
        print("There is at most one prime in a window of size " + str(size) + ".")
    else:
        print(
            "There are at most "
            + str(max_num)
            + " primes in a window of size "
            + str(size)
            + "."
        )

    modified_queue = []
    [modified_queue.append(x) for x in queue if x not in modified_queue]

    for line in modified_queue:
        print(
            "In some window, the smallest prime is "
            + str(line[0])
            + " and the largest one is "
            + str(line[1])
            + "."
        )
