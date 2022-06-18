
# we can use a global varaible inside a fuction

total = 0;

def sum(arg1, arg2)
""" This function sum up two expected arguments.
"""
    total = arg1 + arg2
    print("We are inside the body.")
    return total

response = sum (2,3)
print(response)

def sum(arg1, arg2)
"""This function sum up two expected arguments.
"""
    total = arg1 + arg2
    sum_of = 30 # local variable
    print("We are inside the body.")
    

response = add (1,1)
print(response)

a = 2
 
def define():
    b = 4
    return b

def add():
    c = a + define()
    print(c)

