a = int(input("a variable = "))
b = int(input("b variable = "))
o = input('operator')

def my_add(a, b):
    return a+b

def my_subtract(a, b):
    return a-b

if o == "+":
    print(my_add(a, b))
elif o == "-":
    print(my_subtract(a, b))