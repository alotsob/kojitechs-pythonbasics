
import csv

"""
working with csv, (comma sep, value)
First_name, last_name. date_of birth

"""
"""
req_file = input("Please enter file path")

with open(req_file, "w") as file:
    csv_writer = csv.writer(file)
    csv_writer
"""

# astring = "Hello world!"
# print(astring.startswith("Hello"))
# print(astring.endswith("asdfasdfasdf"))

"""
import csv
from pprint import pprint

'''
Working with csv, (comma sep, value)

First_name, last_name. data_of_birth
'''
req_file = input("PLEASE ENTER FILE PATH: ")

# Opening csv in a write mode. 

with open(req_file, 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["INSTANCE_ID", "STATUS", "ARN"])
    csv_writer.writerow(["TuesDay-10-05-2022", "Introduction/Installation of Terraform", "https://drive.google.com/file/d/1i9piQ_9AhRZO38Dayy5LX606PHSzusv7/view?usp=sharing"])
    csv_writer.writerow(["ThursDay-12-05-2022", "First Terraform Init, terraform plan, and terraform apply", "https://drive.google.com/file/d/1f97bfuoZQsLZmnNntdnG0mdEPdKIjOCI/view"])

"""
"""
req_file = input("Enter file name: ")
with open(req_file, 'r') as file:
  data = csv.reader(file)
for each_file in data:
    print(each_file)

"""


"""
header = ['name', 'area', 'country_code2', 'country_code3']
data = [
    {"name": "Alabama", "area": 2345, "country_code2": "alb", "country_code3" : "ABSHC"}
    {"name": "Algeria", "area": 2384545, "country_code2": "DZ", "country_code3" : "DZA"}
    {"name": "America Samoa", "area": 199, "country_code2": "AS", "country_code3" : "ASM"}
]

with open("address2.csv", 'w') as file:
    # pprint(dir(csv))
    writer_csv=csv.DictWriter(file, fieldnames=header)
    #
    writer_csv.writeheader()

    writer_csv.writerows(data)

"""
#Exercise

header = ['date', 'topic', 'videos']
data = [
    ['Tuesday-11-5', 'introduction', 'clickme'],
    ['Thursday-18-5', 'string operations', 'clickme1',],
    ['Saturday21-5', 'Dictionary', 'clickme2'],
    ['Sunday22-5', 'python operators', 'clickme3'],
    ['Tuesday25-5', 'Condtionals', 'clickme4'],
    ['Saturday28-5', 'for loop', 'clickme4']
]
with open("calendar.csv", "w") as file:
    csv_writer = csv.writer(file)
    
    csv_writer.writerow(header)
    
    csv_writer.writerows(data)

