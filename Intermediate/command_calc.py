import sys

def addition(a, b):
    add = num_1 + num_2
    return add

def subtraction(a, b):
    sub = num_1 - num_2
    return sub

def multiply(a, b):
    mul = num_1 * num_2
    return mul

def divide(a, b):
    div = num_1 / num_2
    return div

num_1 = float(sys.argv[1])
operator = sys.argv[2]
num_2 = float(sys.argv[3])

if operator == "addition":
    output = addition(num_1, num_2)
    print(output)
if operator == "subtraction":
    output = subtraction(num_1, num_2)
    print(output)
if operator == "multiplication":
    output = multiply(num_1, num_2)
    print(output)
if operator == "division":
    output = divide(num_1, num_2)
    print(output)    