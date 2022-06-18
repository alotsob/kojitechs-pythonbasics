
# condtions in python

#what if we don't know the value of x or y
"""
x = eval(input("Enter number: "))
y = eval(input("Enter number: "))
if (x > y):
    print(f"{x} is greater than {y}")
else:
    print(f"{x} is  not greater than {y}")

file = ["file1", "file2", "file3 "]    

"""


"""
#FIZBUSS theory in in python
  # user_input = eval(input("Please enter number! "))
  # check if the user_input is a multiple of 3 print "FIZZ"
  # if user_input is a multiple of 5 print "BUZZ"
  # if user_input is both multiple of 3 and 5 then print FIZZBUZZ
  # otherwise print the number

user_input = eval(input("Please enter number! "))
if user_input %3 == 0 and user_input % 5 == 0:
    print("FZZBUZZ")
elif user_input% 3 == 0:
    print("FIZZ")
elif user_input  %5==0:
    print("BUZZ")
else:
    print(user_input)

    #OR
user_input = eval(input("Please enter number! "))
if user_input %3 == 0 and user_input % 5 == 0:
    print("FZZBUZZ", user_input)
elif user_input% 3 == 0:
    print("FIZZ", user_input)
elif user_input  %5==0:
    print("BUZZ",user_input)
else:
    print(user_input)
"""

# hello = "my name is rob and i love python and i teach python"
# for hello print the most occuring character

from ast import Or


hello = "my name is rob and i love python and i am learning python"


    # What is for_loop
list_1 = ["apple", "orange","pawpaw","pear"]
for each_item in list_1:
    print(each_item)
     
     #OR

list_1 = ["apple", "orange","pawpaw","pear"]
item = [item for item in list_1]
print(item)

list_2 = "apple"
for each_item in list_2:
    print(each_item)

items= ["apple", "orange","pawpaw","pear"]
for item in items:
    print(item)
       

"""
#EX1
#Loop through and print out all even numbers from the numbers list in the same order they are received. 
# Don't print any numbers that come after 237 in the sequence

       numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
for number in numbers:
    if number == 237:
        break

    if number % 2 == 1:
        continue

    print(number)
       

 EX2
  #Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.  
phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  

# your code goes here
phonebook["Jake"] = 938273443  
del phonebook["Jill"]  

# testing code
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")  

 """
