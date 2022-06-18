

'''
from datetime import datetime
import sys, os
from pprint import pprint

def checkFileLessThanXdays(file_path = ''):
    """ This function check all files less than x days and delete
    Parameter: 1(str) Description:
    file_path: requires directory path
    variables: []
    return None
    """
    age = 3
    try: 
        if not os.path.exists(file_path):
            print("please provide a valid path")
        if os.path isfile(file_path):
            print("Oooops!, you just provided a file. please provide directory path.!")
        for each_file in os.listdir(file_path):
            result = os.path.join(file_path, each_file)
            if os.path.isfile(each_file)  
               time_stamp = datetime.fromtimestamp
               file_creation_date = time_stamp(os.getctime(result))  
               if file_creation_date.day > age:
               print(f"{result}, created {file_creation_date.day} Days ago")

    except Exception as e:        
      print(e)
    return None

file_path = input("Please provide a directory")
checkFileLessThanXdays(file_path)

'''

# write a function 
# This function will require on argument("name of file")
#system wild search to check the file
#print out the full path of the file



import sys, os
from pprint import pprint
 
#files = input()

def checkfilepath(file = ''):
    try:
        if not os.files.exist(file):
            print('please provide file name')
        if os.path isfile(file):
            print('you have provided a file')   
        for each_file in os.listdir(file):
            result = os.files.join(file_path, each_file)
            if os.files.isfile(each_file)
            print(f"{result},")
    
    except Exception as e:
        print(e)
        return None

file = input("please provide a directory")    
checkfilepath(file)    