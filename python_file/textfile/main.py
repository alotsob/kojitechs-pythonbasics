
# make sure the file exit
 
"""
mode of a file can be read, write or append
 read() "r", (write)

 write() "w, ("r", "w")


 append() "a" (append)

 close()
 file.close()
 # always close your file.

"""
# how to read a text file


"""
#long
#open a file

#open("name of file", "mode")
path = input("Enter name of file: ")
file = open(path, "r")
#print(dir(file))
data = file.read()
print(data)
file.close()

"""

"""
#short # recommended

path = "textfile_example.txt"
with open(path, "r") as file:
    data = file.read()
    print(data)
              #OR
path = "textfile_example.txt"
with open(path, "r") as file:
    #data = file.readlines()
    data = file.readlines()
    print(data)     

"""

# response = os.path.exists(path)
# print(response)
    

