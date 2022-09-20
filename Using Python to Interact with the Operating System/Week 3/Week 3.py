# import re
# # result = re.search(r"aza", "plaza")
# # print(result)
# # result = re.search(r"aza", "bazaar")
# # print(result)
# # result = re.search(r"aza", 'maze')
# # print(result)
#
# print(re.search(r"^x", "xeon"))
# print(re.search(r"p.ng", "penguin"))
# print(re.search(r"p.ng", "sponge"))
# print(re.search(r"p.ng", "ping"))

import re

#
#
# # def check_aei(text):
# #     result = re.search(r"a.e.i", text)
# #     return result != None
# #
# #
# # print(check_aei("academia"))  # True
# # print(check_aei("aerial"))  # False
# # print(check_aei("paramedic"))  # True
#
# print(re.search(r"p.ng", "Pang", re.IGNORECASE))

# print(re.search("[Pp]ython", "Python"))
# print(re.search(r"[a-z]way", "The end of the highway"))
# print(re.search(r"[a-z]way", "What a way to go"))
# print(re.search("cloud[a-zA-Z0-9]", 'cloud9'))

# print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
# print(re.search(r"cat|dog", "I like dogs"))

# print(re.search(r"Py.*n", 'Pygmalion'))
# print(re.search(r"o+l+", "goldfish"))
# def repeating_letter_a(text):
#     result = re.search(r"[Aa].*[aA]", text)
#     return result != None
#
#
# print(repeating_letter_a("banana"))  # True
# print(repeating_letter_a("pineapple"))  # False
# print(repeating_letter_a("Animal Kingdom"))  # True
# print(repeating_letter_a("A is for apple"))  # True

# def check_character_groups(text):
#     result = re.search(r"\s \b", text)
#     return result != None
#
#
# print(check_character_groups("One"))  # False
# print(check_character_groups("123  Ready Set GO"))  # True
# print(check_character_groups("username user_01"))  # True
# print(check_character_groups("shopping_list: milk, bread, eggs."))  # False

# pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
# print(re.search(pattern, "_this_is_a_valid_variable_name"))
# print(re.search(pattern, "this isn't a valid variable"))
# print(re.search(pattern, "my_variable1"))
# print(re.search(pattern, "2my_variable1"))

# pattern = r"^[A-Z][ |a-z]*[.?\!]$"
#
#
# def check_sentence(text):
#     result = re.search(pattern, text)
#     return result != None
#
#
# print(check_sentence("Is this is a sentence?"))  # True
# print(check_sentence("is this is a sentence?"))  # False
# print(check_sentence("Hello"))  # False
# print(check_sentence("1-2-3-GO!"))  # False
# print(check_sentence("A star is born."))  # True

# def check_web_address(text):
#     pattern = r"(\.com$)|(\.org$)|(\.US$)"
#     result = re.search(pattern, text)
#     return result != None
#
#
# print(check_web_address("gmail.com"))  # True
# print(check_web_address("www@google"))  # False
# print(check_web_address("www.Coursera.org"))  # True
# print(check_web_address("web-address.com/homepage"))  # False
# print(check_web_address("My_Favorite-Blog.US"))  # True

# def check_time(text):
#     pattern = r"^[1-9][0-2]?:[0-5][0-9] ?[am|pm|AM|PM]"
#     result = re.search(pattern, text)
#     return result != None
#
#
# print(check_time("12:45pm"))  # True
# print(check_time("9:59 AM"))  # True
# print(check_time("6:60am"))  # False
# print(check_time("five o'clock"))  # False

# def contains_acronym(text):
#     pattern = r"\([A-Za-z1-9]*\)"
#     result = re.search(pattern, text)
#     return result != None
#
#
# print(contains_acronym("Instant messaging (IM) is a set of communication "
#                        "technologies used for text-based communication"))  # True
# print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a "
#                        "character encoding standard for electronic communication"))  # True
# print(contains_acronym("Please do NOT enter without permission!"))  # False
# print(contains_acronym("PostScript is a fourth-generation programming "
#                        "language (4GL)"))  # True
# print(contains_acronym("Have fun using a self-contained underwater breathing apparatus "
#                        "(Scuba)!"))  # True


# import re
#
#
# def check_zip_code(text):
#     result = re.search(r" \d{5}| \d{5}-\d{4}", text)
#     return result != None
#
#
# print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
# print(check_zip_code("90210 is a TV show"))  # False
# print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
# print(check_zip_code("The Parliament of Canada is at 111 Wellington St, "
#                      "Ottawa, ON K1A0A9."))  # False


# result = re.search(r"^(\w*), (\w*)$", "Kapitanov Igor")
# print(result)
# print(result.groups())
# print(result[0])
# print(result[1])
# print(result[2])
# print("{} {}".format(result[2], result[1]))


# def rearrange_name(name):
#     result = re.search(r"^(\w*) (\w*)$", name)
#     if result is None:
#         return name
#     return "{} {}".format(result[2], result[1])
#
#
# print(rearrange_name("Kapitanov Igor"))


# def rearrange_name(name):
#     result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
#     if result == None:
#         return name
#     return "{} {}".format(result[2], result[1])
#
#
# name = rearrange_name("Kennedy, John F.")
# print(name)

# print(re.search(r"[a-zA-Z]{5}", "a ghost"))
# print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
# print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared"))
# print(re.findall(r"\w{5,15}", "I really like strawberries"))
# print(re.search(r"s\w{,20}", "I really like strawberries"))

# def long_words(text):
#     pattern = r"\b(\w{7,})\b"
#     result = re.findall(pattern, text)
#     return result
#
#
# print(long_words("I like to drink coffee in the morning."))  # ['morning']
# print(long_words("I also have a taste for hot chocolate in the afternoon."))  # ['chocolate', 'afternoon']
# print(long_words("I never drink tea late at night."))  # []

# log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
# regex = r"\[(\d+)]"
# result = re.search(regex, log)
# print(result[1])
#
# result = re.search(regex, "A completely different string that also has numbers [34567]")
# print(result)


# result = re.search(regex, "99 elephants in a [cage]")
# print(result[1])

# def extract_pid(log_line):
#     regex = r"\[(\d+)]"
#     result = re.search(regex, log_line)
#     if result is None:
#         return None
#     return result[1]
#
#
# print(extract_pid(log))
#
#
# print(extract_pid("99 elephants in a [cage]"))


# def extract_pid(log_line):
#     regex = r"\[(\d+)]\: (\w+)"
#     result = re.search(regex, log_line)
#     if result is None:
#         return None
#     return "{} ({})".format(result[1], result[2])
#
#
# print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"))  # 12345 (ERROR)
# print(extract_pid("99 elephants in a [cage]"))  # None
# print(extract_pid("A string that also has numbers [34567] but no uppercase message"))  # None
# print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup"))  # 67890 (RUNNING)


# print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))
# print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))
#
# print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com"))
#
# print(re.sub(r"^([\w .-]*) ([\w .-]*)$", r"\2 \1", "Kapitanov Igor"))

print(re.split(r"the|a", "One sentence. Another one? And the last one!"))