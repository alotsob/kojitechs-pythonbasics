
"""
def my_class():
    print("i am learning")
    print("the class is getting tough")

my_class()    
"""
"""
def say_hello(name, age):
    print(f"hello{name} welcome to kojitech")
    print(f"I'm {age} years old")
"""
"""
def my_home( address, street, city):
    print(f"house {address} this is my house")
    print(f"street {street} this is my street address" )
    print(f"city {city} this is my home city")
     

my_home("nkwen", "667", "Bamenda") 
my_home("upstation", "826", "mile1")   

"""
"""
def add(a, b)
    result = a + b
    print(f " the result of a and b is : {result}")

    add("hello", "world")

"""
"""
def even_numbers():
    for i in range(1, 100):
        if i % 2 == 0:
            print(i, "is an even number")
    else:
        print(i "is an odd number")  

"""
"""
#Types of functions : print function and return function
def send_email(name)
    print (f"hello {name} Your payment is due")
"""
"""
def multiple(number):
    try:
        if number % 15==0:
            print("fizzbuzz")
        elif number % 3 ==0:  
            print("fizz")  
        elif number % 5 ==0:  
            print("buzz")     
        else:
            print(number)   
    except Exception as e:
        print(e)
multiple(15)   

"""
def fizzbuzz(number):
    
    try:
        if number % 15==0:
            return "fizzbuzz"
        elif number % 3 ==0:  
            return "fizz"
        elif number % 5 ==0:  
            return "buzz"     
        else:
            return number   
    except Exception as e:
        return(e)

user_input = eval(input("Enter number: "))        
response = fizzbuzz(user_input) 
print(response) 

