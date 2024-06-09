num_1 = 15
num_2 = 3

def sum(a, b):
    sum = num_1 + num_2
    return sum

def difference(a, b):
    dif = num_1 - num_2
    return dif

def product(a, b):
    prod = num_1 * num_2
    return prod

def quotient(a, b):
    quo = num_1 // num_2
    return quo

p = sum(num_1, num_2)
q = difference(num_1, num_2)
r = product(num_1, num_2)
s = quotient(num_1, num_2)

print(p)
print(q)
print(r)
print(s)