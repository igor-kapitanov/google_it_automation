# base = 6
# height = 3
# area = (base * height) / 2
# print("The area of the triangle is: " + str(area))
#
# total = 2048 + 97658 + 4357 + 125 + 8
# files = 5
# average = total / files
# print("The average size is: " + str(average))

# def greeting(name, department):
#     print("Welcome, " + name)
#     print("You are part of " + department)
#
#
# greeting("Blake", "IT Support")
#
#
# def print_seconds(hours, minutes, seconds):
#     print(int(hours) * 3600 + int(minutes) * 60 + int(seconds))
#
#
# print_seconds(1, 2, 3)

# def area_triangle(base, height):
#     return base * height / 2
#
#
# area_a = area_triangle(5, 4)
# area_b = area_triangle(7, 3)
# sum = area_a + area_b
# print("The sum of both areas is: " + str(sum))


# def get_seconds(hours, minutes, seconds):
#     return 3600 * hours + 60 * minutes + seconds
#
#
# amount_a = get_seconds(2, 30, 0)
# amount_b = get_seconds(0, 45, 15)
# result = amount_a + amount_b
# print(result)

# def convert_seconds(seconds):
#     hours = seconds // 3600
#     minutes = (seconds - hours * 3600) // 60
#     remaining_seconds = seconds - hours * 3600 - minutes * 60
#     return hours, minutes, remaining_seconds
#
#
# hours, minutes, seconds = convert_seconds(5000)
# print(hours, minutes, seconds)


# name = "Igor"
# number = len(name) * 9
# print("Hello " + name + ". Your lucky number is " + str(number))
#
# name = "Olivia"
# number = len(name) * 9
# print("Hello " + name + ". Your lucky number is " + str(number))

# def lucky_number(name):
#     number = len(name) * 9
#     print("Hello " + name + ". Your lucky number is " + str(number))
#
#
# lucky_number("Igor")
# lucky_number("Olivia")

# def month_days(month, days):
#     print(month + " has " + days + " days.")
#
#
# month_days("June", "30")
# month_days("July", "31")


# def rectangle_area(base, height):
#     area = base * height  # the area is base*height
#     print("The area is " + str(area))
#
#
# rectangle_area(5, 6)


# # 1) Complete the function to return the result of the conversion
# def convert_distance(miles):
#     km = miles * 1.6  # approximately 1.6 km in 1 mile
#     return km
#
#
# my_trip_miles = 55
#
# # 2) Convert my_trip_miles to kilometers by calling the function above
# my_trip_km = convert_distance(55)
#
# # 3) Fill in the blank to print the result of the conversion
# print("The distance in kilometers is " + str(my_trip_km))
#
# # 4) Calculate the round-trip in kilometers by doubling the result,
# #    and fill in the blank to print the result
# print("The round-trip in kilometers is " + str(my_trip_km * 2))

# # This function compares two numbers and returns them
# # in increasing order.
# def order_numbers(number1, number2):
#     if number2 > number1:
#         return number1, number2
#     else:
#         return number2, number1
#
#
# # 1) Fill in the blanks so the print statement displays the result
# #    of the function call
# bigger, smaller = order_numbers(100, 99)
# print(smaller, bigger)


# def is_positive(number):
#     if number > 0:
#         return True
#     return False


# def hint_username(username):
#     if len(username) < 3:
#         print("Invalid username. Must be at least 3 characters long")
#     else:
#         print("Valid username")


# def is_even(number):
#     if number % 2 == 0:
#         return True
#     return False

# def hint_username(username):
#     if len(username) < 3:
#         print("Invalid username. Must be at least 3 characters long")
#     elif len(username) >15:
#         print("Invalid username. Must be at most 15 characters long")
#     else:
#         print("Valid username")


# def number_group(number):
#     if number > 0:
#         return "Positive"
#     elif number == 0:
#         return "Zero"
#     else:
#         return "Negative"
#
#
# print(number_group(10))  # Should be Positive
# print(number_group(0))  # Should be Zero
# print(number_group(-5))  # Should be Negative


# def calculate_storage(filesize):
#     block_size = 4096
#     # Use floor division to calculate how many blocks are fully occupied
#     full_blocks = block_size * filesize
#     # Use the modulo operator to check whether there's any remainder
#     partial_block_remainder = full_blocks % block_size
#     # Depending on whether there's a remainder or not, return
#     # the total number of bytes required to allocate enough blocks
#     # to store your data.
#     if partial_block_remainder > 0:
#         return full_blocks
#     return filesize
#
#
# print(calculate_storage(1))  # Should be 4096
# print(calculate_storage(4096))  # Should be 4096
# print(calculate_storage(4097))  # Should be 8192
# print(calculate_storage(6000))  # Should be 8192

# def format_name(first_name, last_name):
#     if first_name is not None and last_name is not None:
#         string = "Name: " + first_name + " " + last_name
#
#     elif first_name is None or last_name is None:
#         string = "Name: " + first_name or "Name: " + last_name
#     else:
#         print(format_name("", ""))
#
#     return string
#
#
# print(format_name("Ernest", "Hemingway"))


# # Should return the string "Name: Hemingway, Ernest"
#
# print(format_name("", "Madonna"))
# # Should return the string "Name: Madonna"
#
# print(format_name("Voltaire", ""))
# # Should return the string "Name: Voltaire"
#
# print(format_name("", ""))
# # Should return an empty string


# def sum(x,y):
#     return (x+y)
# print(sum(sum(1,2), sum(3,4)))

# print((10 >= 5 * 2) and (10 <= 5 * 2))
