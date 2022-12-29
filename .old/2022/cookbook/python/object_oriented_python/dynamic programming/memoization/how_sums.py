from typing import Callable
from timeit import default_timer as timer

def how_sum1(target_sum, seq):
    if target_sum == 0: return []
    if target_sum < 0: return None

    for number in seq:
        remainder = target_sum - number
        remainder_result = how_sum1(remainder, seq)
        if remainder_result is not None: 
            return remainder_result + [number]
    return None


def how_sum2(target_sum, seq, mem=None):
    if mem is None: mem = dict()
    if target_sum == 0: return []
    if target_sum < 0: return None
    if target_sum in mem: return mem[target_sum]
    
    for number in seq:
        remainder = target_sum - number
        remainder_result = how_sum2(remainder, seq, mem)
        if remainder_result is not None: 
            result = remainder_result + [number]
            mem[target_sum] = result
            return mem[target_sum]
    mem[target_sum] = None
    return None

def test_timer(f: Callable, n: int, seq: list[int]) -> str:
    start = timer()
    out = f(n, seq)
    end = timer()
    return f"{out} {end-start}"


if __name__=="__main__":
    print(test_timer(how_sum2, 7, [2,3]), test_timer(how_sum1, 7, [2,3]),)
    print(test_timer(how_sum2, 7, [5, 3, 4, 7]), test_timer(how_sum1, 7, [5, 3, 4, 7]))
    print(test_timer(how_sum2, 7, [4, 2]), test_timer(how_sum1, 7, [4, 2]))
    print(test_timer(how_sum2, 8, [2, 3, 5]), test_timer(how_sum1, 8, [2, 3, 5]))
    print(test_timer(how_sum2, 300, [7, 14]))#, test_timer(n_sum1, 300, [7, 14])