# with open("spider.txt") as file:
#     print(file.readline())

# with open("spider.txt") as file:
#     for line in file:
#         print(line.strip().upper())

# file = open ("spider.txt")
# lines = file.readlines()
# file.close()
# lines.sort()
# print(lines)

# with open("novel.txt", "w") as file:
#     file.write("It was a dark and stormy night")


# guests = open("guests.txt", "w")
# initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]
#
# for i in initial_guests:
#     guests.write(i + "\n")
#
# new_guests = ["Sam", "Danielle", "Jacob"]
#
# with open("guests.txt", "a") as guests:
#     for i in new_guests:
#         guests.write(i + "\n")
#
# guests.close()
#
# with open("guests.txt") as guests:
#     for line in guests:
#         print(line)
#
# guests.close()
#
#
# checked_out=["Andrea", "Manuel", "Khalid"]
# temp_list=[]
#
# with open("guests.txt", "r") as guests:
#     for g in guests:
#         temp_list.append(g.strip())
#
# with open("guests.txt", "w") as guests:
#     for name in temp_list:
#         if name not in checked_out:
#             guests.write(name + "\n")
#
# with open("guests.txt") as guests:
#     for line in guests:
#         print(line)
#
# guests_to_check = ['Bob', 'Andrea']
# checked_in = []
#
# with open("guests.txt","r") as guests:
#     for g in guests:
#         checked_in.append(g.strip())
#     for check in guests_to_check:
#         if check in checked_in:
#             print("{} is checked in".format(check))
#         else:
#             print("{} is not checked in".format(check))


import os
# os.remove("novel.txt")
# os.rename("guests.txt", "guests_new.txt")
# os.path.exists("guests_new.txt")
# os.path.abspath("spider.txt")

# import os
#
#
# def new_directory(directory, filename):
#     # Before creating a new directory, check to see if it already exists
#     if os.path.isdir(directory) == False:
#         os.mkdir(directory)
#     # Create the new file inside of the new directory
#     path = os.path.join(directory, filename)
#     # Return the list of files in the new directory
#     os.mkdir(path)
#     return os.listdir(directory)
#
#
# print(new_directory("PythonPrograms", "script.py"))

# import os
# import datetime
# from datetime import date
#
#
# def file_date(filename):
#     # Create the file in the current directory
#     os.mkdir(filename)
#     timestamp = os.path.getmtime(filename)
#     # Convert the timestamp into a readable format, then into a string
#     timestamp = date.fromtimestamp(timestamp)
#     # Return just the date portion
#     # Hint: how many characters are in “yyyy-mm-dd”?
#     return ("{}".format(timestamp))
#
#
# print(file_date("newfile.txt"))
# # Should be today's date in the format of yyyy-mm-dd

#
# import os
#
#
# def parent_directory():
#     # Create a relative path to the parent
#     # of the current working directory
#     path = os.getcwd()
#     relative_parent = os.path.abspath(os.path.join(path, os.pardir))
#     # Return the absolute path of the parent directory
#     return relative_parent
#
#
# print(parent_directory())


# import csv
# hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
# with open("hosts.csv", "w") as hosts_csv:
#     writer = csv.writer(hosts_csv)
#     writer.writerows(hosts)


import os
import csv


# Create a file with data in it
# def create_file(filename):
#     with open(filename, "w") as file:
#         file.write("name,color,type\n")
#         file.write("carnation,pink,annual\n")
#         file.write("daffodil,yellow,perennial\n")
#         file.write("iris,blue,perennial\n")
#         file.write("poinsettia,red,perennial\n")
#         file.write("sunflower,yellow,annual\n")


# Read the file contents and format the information about each row
# def contents_of_file(filename):
#     return_string = ""
#
#     # Call the function to create the file
#     create_file(filename)
#
#     # Open the file
#     with open(filename) as file:
#         # Read the rows of the file
#         rows = csv.DictReader(file)
#         # Process each row
#         for row in rows:
#             name, color, type = row
#             # Format the return string for data rows only
#
#         return_string += "a {} {} is {}\n".format(row["color"])
#     return return_string
#
#
# # Call the function
# print(contents_of_file("flowers.csv"))


# import csv
#
#
# def read_employees(csv_file_location):
#     csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
#     employee_file = csv.DictReader(open(csv_file_location), dialect='empDialect')
#     employee_list = []
#     for data in employee_file:
#         employee_list.append(data)
#     return employee_list
#
#
# employee_list = read_employees('<file_location>')
# print(employee_list)
#
#
# def process_data(employee_list):
#     department_list = []
#     for employee_data in employee_list:
#         department_list.append(employee_data['Department'])
#     department_data = {}
#     for department_name in set(department_list):
#         department_data[department_name] = department_list.count(department_name)
#     return department_data
#
#
# dictionary = process_data(employee_list)
# print(dictionary)
#
#
# def write_report(dictionary, report_file):
#     with open(report_file, "w+") as f:
#         for k in sorted(dictionary):
#             f.write(str(k) + ':' + str(dictionary[k]) + '\n')
#         f.close()
#
#
# write_report(dictionary, '/home/student-03-aaa245253840/data/report.txt')
