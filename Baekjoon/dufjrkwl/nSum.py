
import sys


def input(): return sys.stdin.readline().rstrip()


def solve(a: list) :
    res = 0
    for num in a:
        res += num

    return res
