
""" 
 # while loop means iterate untill the condition is false
count = 1
while count < 3:
   print(count)
   count +=1

   count = 1
while count < 3:# statement (body within the while loop)
   print(count)
   count +=1
"""
# count = 0
# while count > 15:
#     print(count)
#     count +=1
# else:
#     print (f"{count} is not greater than 15")

    
#exercise
"""
import getpass

password = "kojitechs123"
user_guess = ""
user_atempt = 3 

# first condition "if user_atempt not == 0", user_guess!=password

while user_guess != password and user_atempt !=0:
    user_guess = getpass.getpass("Enter password: ")
    user_atempt -=1
    if user_atempt==0: 
        print("Sorry you have exhausted the limit of 3")  
        
    if user_guess == password:
        print("Login succesful!")
        
    else:
        print(f"You have {user_atempt} attempt left")
"""

#exercise 2
# i = range(1, 100)
# even_number = 0
# odd_number = 1
# while i !=even_number and odd_number!=1:
    
#      if (i%2==0): 
#       print(f"{i} is Even number") 
# else: 
# 		print(f"{i} is Odd Number")

i = range(1, 100)



    
