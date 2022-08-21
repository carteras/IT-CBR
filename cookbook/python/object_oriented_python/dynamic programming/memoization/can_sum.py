from typing import Callable
from timeit import default_timer as timer

def can_sum1(target_sum: int, seq: list[int]) -> bool:
    if target_sum == 0: return True
    if target_sum < 0: return False
    if target_sum == 1: return False
    for number in seq:
        if can_sum1(target_sum-number, seq): return True
    return False

def can_sum2(target_sum:int, seq:list[int], mem:dict[int, int]=None):
    if target_sum == 0: return True
    if target_sum < 0: return False
    if target_sum == 1: return False
    if mem is None: mem = dict()

    if target_sum in mem: return mem[target_sum]
    
    for number in seq:
        remainder = target_sum-number
        mem[remainder] = can_sum2(remainder, seq, mem)
        if mem[remainder]: return True
    return False



def test_timer(f: Callable, n: int, seq: list[int]) -> str:
    start = timer()
    out = f(n, seq)
    end = timer()
    return f"{out:,} {end-start}"


if __name__=="__main__":
    print(test_timer(can_sum2, 7, [2,3]), test_timer(can_sum1, 7, [2,3]),)
    print(test_timer(can_sum2, 7, [5, 3, 4, 7]), test_timer(can_sum1, 7, [5, 3, 4, 7]))
    print(test_timer(can_sum2, 7, [4, 2]), test_timer(can_sum1, 7, [4, 2]))
    print(test_timer(can_sum2, 8, [2, 3, 5]), test_timer(can_sum1, 8, [2, 3, 5]))
    print(test_timer(can_sum2, 300, [7, 14])) #, test_timer(can_sum1, 300, [7, 14])