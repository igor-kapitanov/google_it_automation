# x = 0
# while x < 5:
#     print("Not there yet, x = " + str(x))
#     x = x + 1
# print("x = " + str(x))


# def attempts(n):
#     x = 1
#     while x <= n:
#         print("Attempt " + str(x))
#         x += 1
#     print("Done")
#
#
# attempts(5)

# username = get_username()
# while not valid_username(username):
#     print("Invalid username")
#     username = get_username()

# def count_down(start_number):
#     current = start_number
#     while current > 0:
#         print(current)
#         current -= 1
#     print("Zero!")
#
#
# count_down(3)

# x = 10
# while x != 0 and x % 2 == 0:
#     x = x / 2
#     print(x)


# def print_range(start, end):
#     # Loop through the numbers from start to end
#     n = start
#     while n <= end:
#         print(n)
#         n += 1
#
#
# print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line)

# def sum_divisors(n):
#     x = 1
#     sum = 0
#     for x in range(x, n):
#         if n % x == 0 and x < n:
#             sum +=x
#         else:
#             x +=1
#     # Return the sum of all divisors of n, not including n
#     return sum
#
#
# print(sum_divisors(0))
# # 0
# print(sum_divisors(3))  # Should sum of 1
# # 1
# print(sum_divisors(36))  # Should sum of 1+2+3+4+6+9+12+18
# # 55
# print(sum_divisors(102))  # Should be sum of 2+3+6+17+34+51
# # 114


# def sum_squares(x):
#     sum = 0
#     for n in range(x):
#         sum += n
#     return sum
#
#
# print(sum_squares(10))  # Should be 285

# values = [23, 52, 59, 37, 48]
# sum = 0
# length = 0
# for value in values:
#     sum += value
#     length += 1
#
# print("Total sum: " + str(sum) + " - Average: " + str(sum/length))

# product = 1
# for n in range(1,10):
#     product *= n
#
# print(product)

# def factorial(n):
#     result = 1
#     for i in range (1, n+1):
#         result *= i
#     return result
#
# print(factorial(4)) # should return 24
# print(factorial(5)) # should return 120

# def to_celsius(x):
#     return (x-32)*5/9
#
# for x in range (0,101,10):
#     print(x, to_celsius(x))

# for left in range(7):
#     for right in range(left, 7):
#         print("[" + str(left) + "|" + str(right) + "]", end=" ")
#     print()


# teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
# for home_team in teams:
#     for away_team in teams:
#         if home_team != away_team:
#             print(home_team + " vs " + away_team)

# def factorial(n):
#     if n < 2:  # base case
#         return 1  # base case
#     return n * factorial(n - 1)  # recurse case

# def factorial(n):
#     print("Factorial called with " + str(n))
#     if n < 2:
#         print("Returning 1")
#         return 1
#     result = n * factorial(n - 1)
#     print("Returning " + str(result) + " for factorial of " + str(n))
#     return result
#
#
# factorial(4)

# def sum_positive_numbers(n):
#     # The base case is n being smaller than 1
#     if n < 1:
#         return n
#
#     # The recursive case is adding this number to
#     # the sum of the numbers smaller than this one.
#     return n + sum_positive_numbers(n - 1)
# print(sum_positive_numbers(3))  # Should be 6
# print(sum_positive_numbers(5))  # Should be 15


# def is_power_of(number, base):
#     # Base case: when number is smaller than base.
#     number /= base
#     if number < base:
#         # If number is equal to 1, it's a power (base**0).
#         return False
#     else:
#         return True

# Recursive case: keep dividing number by base.
# return is_power_of(number, base)


# print(is_power_of(8, 2))  # Should be True
# print(is_power_of(64, 4))  # Should be True
# print(is_power_of(70, 10))  # Should be False

# def decade_counter():
# 	while year < 50:
# 		year += 10
# 	return year

# for x in range(1, 10, 3):
#     print(x)


# for x in range(10):
#     for y in range(x):
#         print(y)

# def votes(params):
#     for vote in params:
#         print("Possible option:" + vote)
#
#
# votes(["yes", "no", "maybe"])
