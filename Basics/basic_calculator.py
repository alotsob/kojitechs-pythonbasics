# Built basic calculators
'''
first_num = input( "please enter first number: ")
sec_num = input( "please enter second number: ")
result = first_num + sec_num

print(f"")
'''
# set  => thisdict = {"milo", "mill", "bread"} 
         # dictionary
from itertools import product


my_dict_1 = {"name": "rob", "nationality": "Cam", "age": 20, "sex": "male"}
#print(type(my_dict_1))

my_dict = dict(name = "rob", country=["Cam", "Ghana", "Egypt"], age = 22, is_male=True)
#print(type(my_dict))
#print(dir(my_dict))

#print(my_dict.get("name"))
#NB () => tuple
# another method


thisdict = {"brand": "Ford", "model": "focus", "year": 1994}
thisdict["brand"] = "buic"
#print(thisdict)

#when the key doesn't exist
thisdict = {"brand": "Ford", "model": "focus", "year": 1994}
thisdict["country"] = ["Nigeria", "Cam", "Togo"]
#print(thisdict)

keys = {"a","e", "i", "o", "u"}
value = "vowels"
vowels = thisdict.fromkeys(keys)
#print(vowels)

keys = {"a","e", "i", "o", "u"}
value = [1]
vowels = thisdict.fromkeys(keys,value)
#print(vowels)
new_dict = {
    "brand": "Ford",
    "model": "focus", 
    "year": 1994,
    'country':['Nigeria', 'Cam', 'Togo'] }


people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female'},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male'}}

var = people.get(4)
#print(f"Mr peter's age is {var.get('age')}),\nhis sex is {var.get('sex')}")

# Assignment 
products = [
    ("product_1", 200),
    ("product_2", 400),
    ("product_3", 900),
    ("product_4", 1000)
]

# print out all the prouct that is greater than 500

# p = 500
# print(all(p >500 for p in products ))

# products = [items for items in products if product > 500]
# print(products)

# p = 500 
# for i in range(len(products)):
#     if products[i] > p:
#         print(i, end='')

# Assignment 
products = [
    ("product_1", 200),
    ("product_2", 400),
    ("product_3", 900),
    ("product_4", 1000)
]

for item in products:
    if item[1] >= 500:
        print(item)

result = [item for item in products if item[1] > 500]
print(result)
''' 
print(products)

my_products = [i for i in products if i[1] > 500]
print("The resultant list of product greater than 500 is : ")
print(my_products)
'''
