print("Type in your operation 'var1 var2 opr' press q to quit")
looping = True

def my_add(a, b):
    return a+b

def my_subtract(a, b):
    return a-b

def calc(user_input):
    a, b, o = user_input.split(" ")

    a = int(a)
    b = int(b)

    if o == "+":
        return f"{a} {o} {b} = {my_add(a, b)}"
    elif o == "-":
        return f"{a} {o} {b} = {my_subtract(a, b)}"

while looping:
    user_input = input("[var1 var2 opr | q]> ")
    if user_input == 'q':
        looping = False
        continue
    print(calc(user_input))
    