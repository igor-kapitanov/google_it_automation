# name = "Sasha"
# color = 'gold'
# place = "Cambridge"
#
# pet = ""
# pet = "loooooooooooong cat"
# print("Name: " + name + ", Favorite color: " + color)
#
# "example" * 3
# len(pet)

# def first_and_last(message):
#     if str(message[0]) == str(message[-1]) or str(message) == "":
#         return True
#     return False
#
#
# print(first_and_last("else"))
# print(first_and_last("tree"))
# print(first_and_last(""))

# message = "else"
# print(message[0])
# print(message[-1])

# def replace_domain(email, old_domain, new_domain):
#     if "@" + old_domain in email:
#         index = email.index("@" + old_domain)
#         new_email = email[:index] + "@" + new_domain
#         return new_email
#     return email

# print("...".join(["This", "is", "a", "phrase", "joines", "by", "triple", "dots"]))

# def initials(phrase):
#     words = phrase.split()
#     result = ""
#     for word in words:
#         result += word[0]
#     return result.upper()
#
# print(initials("Universal Serial Bus")) # Should be: USB
# print(initials("local area network")) # Should be: LAN
# print(initials("Operating system")) # Should be: OS

# price = 7.5
# with_tax = price*1.13
# print(price, with_tax)
#
# print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))

# x = ["Now", "we", "are", "cooking!"]
# print(type (x))
# print(x)
# print(len(x))
# print("are" in x)
# print("Today" in x)
# print(x[0])
# print(x[1:3])

# def get_word(sentence, n):
#     # Only proceed if n is not more than the number of words
#     words = sentence.split(" ")
#     if n <= len(words) and n > 0:
#         return words[n - 1]
#     else:
#         return ""
#
#
# print(get_word("This is a lesson about lists", 4))  # Should print: lesson
# print(get_word("This is a lesson about lists", -4))  # Nothing
# print(get_word("Now we are cooking!", 1))  # Should print: Now
# print(get_word("Now we are cooking!", 5))  # Nothing

# def skip_elements(elements):
#   # Initialize variables
#   new_list = []
#   i = 0
#
#   # Iterate through the list by value and not index
#   for elem in elements:
#       # Does this element belong in the resulting list? Check on index
#       if i % 2 == 0:
#           # Add this element to the resulting list
#           new_list.append(elem)
#       # Increment index
#       i += 1
#
#   return new_list
#
# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be
# ['Orange', 'Strawberry', 'Peach']
# print(skip_elements([])) # Should be []

# def convert_seconds(seconds):
#     hours = seconds // 3600
#     minutes = (seconds - hours * 3600) // 60
#     remaining_seconds = seconds - hours * 3600 - minutes * 60
#     return hours, minutes, remaining_seconds
#
#
# result = convert_seconds(5000)
# print(type(result))
# print(result)
#
# hours, minutes, seconds = result
# print(hours, minutes, seconds) # unpacking
#
# hours,minutes,seconds = convert_seconds(1000)
# print(hours,minutes,seconds)

# animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
# chars = 0
# for animal in animals:
#     chars += len(animal)
#
# print("Total characters: {}, Average length: {}" .format(chars, chars/len(animals)))

# winners = ["Ashley", "Dylan", "Reese"]
# for index, person in enumerate(winners):
#     print("{} - {}" .format(index + 1, person))

# def full_emails(people):
#     result = []
#     for email, name in people:
#         result.append("{} <{}>" .format(name, email))
#     return result
#
# print(full_emails([("alex@gillamgroup.com", "Alex Diego"), ("shay@gillamgroup.com", "Shay Brant")]))

# def skip_elements(elements):
#     # code goes here
#     result = []
#     for index, word in enumerate(elements):
#         if index % 2 == 0:
#             result.append(word)
#     return result
#
#
# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(
#     ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']

# multiples = []
# for x in range(1, 11):
#     multiples.append(x*7)
#
# print(multiples)

# multiples = [ x*7 for x in range(1, 11)]
# print(multiples)

# languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
# lengths = [len(language) for language in languages]
#
# print(lengths)

# z = [x for x in range(0, 101) if x % 3 == 0]
# print(z)

# def odd_numbers(n):
#     return [x for x in range(0, n + 1) if x % 2 != 0]
#
#
# print(odd_numbers(5))  # Should print [1, 3, 5]
# print(odd_numbers(10))  # Should print [1, 3, 5, 7, 9]
# print(odd_numbers(11))  # Should print [1, 3, 5, 7, 9, 11]
# print(odd_numbers(1))  # Should print [1]
# print(odd_numbers(-1))  # Should print []


# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# # Generate newfilenames as a list containing the new filenames
# newfilenames = []
# # using as many lines of code as your chosen method requires.
# for filename in filenames:
#     if filename.endswith(".hpp"):
#         filename = filename.replace(".hpp", ".h")
#         newfilenames.append(filename)
#     else:
#         newfilenames.append(filename)
#
# print(newfilenames)
# # Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


# def pig_latin(text):
#     words = text.split()
#     pigged_text = []
#
#     for word in words:
#         word = word[1:] + word[0] + "ay"
#         pigged_text.append(word)
#     return " ".join(pigged_text)
#
#
# print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"


# def octal_to_string(octal):
#     value_letters = [(4, "r"), (2, "w"), (1, "x")]
#     result = ""
#     value_letters = [(4, "r"), (2, "w"), (1, "x")]
#     # Iterate over each of the digits in octal
#     for ___ in [int(n) for n in str(octal)]:
#         # Check for each of the permissions values
#         for value, letter in value_letters:
#             if ___ >= value:
#                 result += letter
#                 ___ -= value
#             else:
#                 result += "-"
#     return result


# print(octal_to_string(755))  # Should be rwxr-xr-x
# print(octal_to_string(644))  # Should be rw-r--r--
# print(octal_to_string(750))  # Should be rwxr-x---
# print(octal_to_string(600))  # Should be rw-------

# def group_list(group, users):
#     members = ", ".join(users)
#     return "{}: {}".format(group, members)
#
#
# print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))  # Should be "Marketing: Mike, Karen, Jake, Tasha"
# print(group_list("Engineering", ["Kim", "Jay", "Tom"]))  # Should be "Engineering: Kim, Jay, Tom"
# print(group_list("Users", ""))  # Should be "Users:"


# def guest_list(guests):
#     for guest in guests:
#         name, age, job = guest
#         print("{} is {} years old and works as {}".format(name, age, job))
#
#
# guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
#
# # Click Run to submit code
# """
# Output should match:
# Ken is 30 years old and works as Chef
# Pat is 35 years old and works as Lawyer
# Amanda is 25 years old and works as Engineer
# """


# file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
# print(file_counts)
# print(file_counts["txt"])
# print("jpg" in file_counts)
# print("html" in file_counts)
# file_counts["cfg"] = 8
# print(file_counts)


# toc = {"Introduction": 1, "Chapter 1": 4, "Chapter 2": 11, "Chapter 3": 25, "Chapter 4": 30}
# toc["Epilogue"] = 39
# toc["Chapter 3"] = 24
# print(toc)
# print("Chapter 5" in toc)
#
# # Epilogue starts on page 39
# # Chapter 3 now starts on page 24
# # What are the current contents of the dictionary?
# # Is there a Chapter 5?


# file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
# for extension in file_counts:
#     print(extension)
#
# for ext, amount in file_counts.items():
#     print("There are {} files with the .{} extension" .format(amount, ext))
#
# print(file_counts.keys())
# print(file_counts.values())
#
# for value in file_counts.values():
#     print(value)

# cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
# for value, ext in cool_beasts.items():
#     print("{} have {}".format(value, ext))

# def count_letters(text):
#     result = {}
#     for letter in text:
#         if letter not in result:
#             result[letter] = 0
#         result[letter] += 1
#     return result
#
# print(count_letters("kapitanov"))
# print(count_letters("cit corporation"))

# wardrobe = {"shirt": ["red", "blue", "white"], "jeans": ["blue", "black"]}
# for clothers, colors in wardrobe.items():
#     for color in colors:
#         print("{} {}".format(color, clothers))


# def email_list(domains):
# 	emails = []
# 	for domain, users in domains.items():
# 	  for user in users:
# 	    emails.append(user + "@" + domain)
# 	return(emails)
#
# print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

# wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
# new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
# wardrobe.update(new_items)
# print(wardrobe)

