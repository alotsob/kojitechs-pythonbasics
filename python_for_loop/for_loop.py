
# Recap
#for loop means iterating. over a list or dict or tupple
fruits = ["apple", "pawpaw", "orange", "pear", "mango"]
user_data = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [ {"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1} ]
}
"""
maginumber = [(1,2),(23,4),(23,8)]
hello = "My name if koji Bello and i'm the lead Devops Engineer at plastig"

for fruit in fruits:
    print(fruit)
#[item for item in items] comprehensive list
# fruit=[fruit for fruit in fruits]    

    # iterate over a dict
for user in user_data:
  print(user)

for user in user_data.items():
   print(user)

   # unpackaging
   for key, value in user_data.items():
       print(key) # print(value)

for number in maginumber:
    print(number)

for x in hello:
    print(x)

            # nested loop
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end = "") # body of inner loop

number = [1,4, 7,8,9,15,20,30,35,40]
for i in number:
    # inner loop
    if i > 15:

        break # (exit)
    else:
        print(i)

"""
# name = "mariya mennen"  
# count = 0  
# for m in  name:
#     if m != 'm'  :
#         continue
#     else:
#         count = count + 1
#         print("The number of times m occured is: ", count)

name = "mariya mennmbellm men"

count = 0

for m in name:
    if m != 'm':
        continue
    else:
        count =  count + 1    
#print("The amount of time m occured is:", count)      

for i in range(1, 100):
   # in loop(condition)
   if i % 2 == 0:
       print(f"{i}is an Even Number")
else: 
    print(f"{i} is an Odd Number")

