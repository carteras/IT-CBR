from dataclasses import dataclass

@dataclass
class NumberWithLogs:
    result: float
    logs: list

def square(x: NumberWithLogs) -> NumberWithLogs:
    return NumberWithLogs(
        result=x.result**2, 
        logs=x.logs + [f"Squared {x.result} to get {x.result**2}"]
    )

def add_one(x: NumberWithLogs) -> NumberWithLogs:
    return NumberWithLogs(
        result=x.result + 1,
        logs = x.logs + [f"Added 1 to {x.result} to get {x.result+1}"]
    )

def multiply_by_three(x: NumberWithLogs) -> NumberWithLogs:
    return NumberWithLogs(
        result = x.result * 3,
        logs = x.logs + [f"Multiplied {x.result} to get {x.result*3}"]
    )



def wrap_in_logs(x: float) -> NumberWithLogs:
    return NumberWithLogs(
        result=x,
        logs = []
    )

def runWithLogs(input: int | float | NumberWithLogs, transform: callable) -> NumberWithLogs:
    match input:
        case int(input) | float(input): input = wrap_in_logs(input)
    return transform(input)


a = runWithLogs(4, add_one)
b = runWithLogs(a, square)
c = runWithLogs(b, multiply_by_three)
print(a.result, a.logs)
print(b.result, b.logs)
print(c.result, c.logs)

