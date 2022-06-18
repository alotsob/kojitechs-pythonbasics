
# string casting
'''
x = 1
y = 2
'''
# string  casting
'''
x,y,d = 1,2,3
print(y)
'''
# list casting
#fruits, *third_v, second_var =["apple", "pawpaw", "plum","orange"]

"""
print("hello world")
print("what is your name?")
myName = input()
print("it is good to meet you," + myName)
print("the length of my name is: ")
print(len(myName))
print("what is your age? ")
myAge = input()
print("You will be " + str(int(myAge)+1)+ "in a year")

"""
"""
name = 'Elise'
age = 101
if name == 'Alice':
    print('Hi, Alice')
elif age < 12:
    print('You are not Alice Kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not undead, immortal vampire.')
elif age > 100:
    print('You are not Alice grannie.')

"""
"""
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you')
"""
'''
while True:
    print('who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. what is the password?(Is it fish?)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')        
'''
'''
import sys
while True:
    print('Type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
        print('You typed' + response + '.')
'''
