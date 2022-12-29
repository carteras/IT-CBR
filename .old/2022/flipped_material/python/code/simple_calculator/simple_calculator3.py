print("Type in your operation 'var1 var2 opr'")
user_input = input("[var1 var2 opr]> ")
a, b, o = user_input.split(" ")

a = int(a)
b = int(b)

def my_add(a, b):
    return a+b

def my_subtract(a, b):
    return a-b

if o == "+":
    print(my_add(a, b))
elif o == "-":
    print(my_subtract(a, b))