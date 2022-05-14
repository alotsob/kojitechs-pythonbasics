
import builtins
# from tkinter import Variable
# print(dir(builtins))
# from pprint import pprint

# print("hello world!")

# print(len("hello Rob"))

# print([1,2,3,4,5,6])

# print(sum(1,2,3,4,5,6))

# print(type("builtins"))

# print(input("please enter user name"))

#Python Variables
first_name = "Rob"
last_name = "Bob"

print(type(last_name))
print(type(first_name))

age = 90
print(type(age))

# The expected output is 
#my first name is Rob and my last name is Bob and i am 90 years!
print(f"my first name is {first_name} and my last name is {last_name} and i am {age} years")

school = "gbhs"
classroom = "python"

# write a program that would print
# my name is Rob and i school in kojitechs, and i learn python
print(f"my name is Rob and i school in {school}, and i learn {classroom}")

# How to name your varaibles
# avoid using python builtins functions to name your varaibles
# variables are case sensitive

## Built-in Data Types
# Some data types in python
# text = string  | type("classroom")
# Numeric types : int | num = 1234
# float data type | type(12.5)
# dict {} | mapping. dict has a key and a value
student_info = {"name":"rob", "age" : 24}
type(student_info)
#set
set_numbers = {1,2,3,4,5}
type(set_numbers)
#list
list_of_items = {"banana", "pear", "plum"}
print(type(list_of_items))
# bool
y = None
print(type(y))