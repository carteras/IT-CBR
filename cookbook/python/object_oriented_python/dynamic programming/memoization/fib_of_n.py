from typing import Callable
from timeit import default_timer as timer


def fib1(n:int) -> int:
    if (n <= 2): return 1
    return fib1(n - 1) + fib1(n - 2)

def fib2(n:int, memo: dict[int, int] =None) -> int:
    if (n <=2): return 1
    if memo is None: memo = dict()
    if n in memo: return memo[n]
    memo[n] = fib2(n - 1, memo) + fib2(n - 2, memo)
    return memo[n]

def test_fib(f: Callable, n: int) -> str:
    start = timer()
    out = f(n)
    end = timer()
    return f"{out:,} {end-start}"

for n in range(1, 41):
    print(n, test_fib(fib2, n), test_fib(fib1, n))
