from typing import Callable
from timeit import default_timer as timer


def grid_traveller2(m: int, n: int, mem: dict[(int, int), int] = None) -> int:
    if m * n == 0: return 0
    if m * n == 1: return 1
    if mem is None: mem = dict()
    if (m,n) in mem: return mem[m,n]
    mem[(m,n)] = grid_traveller2(m - 1, n, mem) + grid_traveller2(m, n-1, mem)
    return mem[(m,n)]

def grid_traveller1(m, n):
    if m * n == 0: return 0
    if m * n == 1: return 1
    return grid_traveller1(m - 1, n) + grid_traveller1(m, n-1)

def test_grid_traveller(f: Callable, n: int, m: int) -> str:
    start = timer()
    out = f(n, m)
    end = timer()
    return f"{out:,} {end-start}"

if __name__ == "__main__":
    for n, m in zip(range(1, 50), range(1, 50)):
        # print(n, m, test_grid_traveller(grid_traveller1, n, m), test_grid_traveller(grid_traveller2, n, m))
        print(n, m, test_grid_traveller(grid_traveller2, n, m))

