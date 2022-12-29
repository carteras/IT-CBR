from dataclasses import dataclass
from typing import Callable
from timeit import default_timer as timer


@dataclass
class AnswerWithLogs:
    result: list[int]
    logs: list

def best_sum1(target_sum: int, seq: list[int]) -> list[int] | None:
    if target_sum == 0: return []
    if target_sum < 0: return None

    shortest_combination = None

    for number in seq:
        remainder = target_sum - number
        remainder_result = best_sum1(remainder, seq)
        if remainder_result is not None:
            combination = remainder_result + [number]
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination

    return shortest_combination

def best_sum2(target_sum: int, seq: list[int], mem: dict[int] =None) -> list[int] | None:
    if mem is None: mem = dict()
    if target_sum == 0: return []
    if target_sum < 0: return None
    if target_sum in mem: return mem[target_sum]

    shortest_combination = None

    for number in seq:
        remainder = target_sum - number
        remainder_result = best_sum2(remainder, seq, mem)
        if remainder_result is not None:
            combination = remainder_result + [number]
            
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination
    mem[target_sum] = shortest_combination
    return shortest_combination

def best_sum3(target_sum: int, seq: list[int], mem: dict[int] =None) -> list[int] | None:
    if mem is None: mem = dict()
    if target_sum <= 0: return []
    if target_sum in mem: return mem[target_sum]

    shortest_combination = None

    for number in seq:
        remainder = target_sum - number
        remainder_result = best_sum3(remainder, seq, mem)
        combination = remainder_result + [number]
        
        if shortest_combination is None or len(combination) < len(shortest_combination):
            shortest_combination = combination
    mem[target_sum] = shortest_combination
    return shortest_combination

def test_timer(f: Callable, n: int, seq: list[int]) -> str:
    start = timer()
    out = f(n, seq)
    end = timer()
    return f"{out} {end-start}"

def test(n, seq, f1, f2=None):
    if f2: return f"{test_timer(f1, n, seq)} {test_timer(f2, n, seq)}"
    return f"{test_timer(f1, n, seq)}"


    
def run_with_logs(number: int | AnswerWithLogs, sequence, transform):
    ...

if __name__=="__main__":
    print(test(7, [7], best_sum3, best_sum2))
    print(test(7, [3, 4], best_sum3, best_sum2))
    print(test( 7, [5, 3, 4, 7], best_sum3, best_sum2))
    print(test( 8, [2, 3, 5],best_sum3, best_sum2))
    print(test(8, [1, 4, 5], best_sum3, best_sum2))
    print(test(100, [1, 2, 5, 25], best_sum3, best_sum2))