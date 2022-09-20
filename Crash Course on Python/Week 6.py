# members = [4,6,2,7,1]
# members.sort()
# print(members)
#
# names = ["Carlos", "Ray", "Alex", "Kelly"]
# print(names)
# print(sorted(names))
# print(sorted(names, key=len))

# def get_event_date(event):
#     return event.date
#
#
# def current_users(events):
#     events.sort(key=get_event_date)
#     machines = {}
#     for event in events:
#         if event.machine not in machines:
#             machines[event.machine] = set()
#         if event.type == "login":
#             machines[event.machine].add(event.user)
#         elif event.type == "logout":
#             machines[event.machine].remove(event.user)
#     return machines
#
#
# def generate_report(machines):
#     for machine, users in machines.items():
#         if len(users) > 0:
#             user_list = ", ".join(users)
#             print("{}: {}".format(machine, user_list))
#
#
# class Event:
#     def __init__(self, event_date, event_type, machine_name, user):
#         self.date = event_date
#         self.type = event_type
#         self.machine = machine_name
#         self.user = user
#
#
# events = [
#     Event("2020-01-21 12:45:56", "login", "myworkstation.local", "jordan"),
#     Event("2020-01-22 15:53:42", "logout", "webserver.local", "jordan"),
#     Event("2020-01-21 18:53:21", "login", "webserver.local", "lane"),
#     Event("2020-01-22 10:25:34", "logout", "myworkstation.local", "jordan"),
#     Event("2020-01-21 08:20:01", "login", "webserver.local", "jordan"),
#     Event("2020-01-23 11:24:35", "login", "mailserver.local", "chris")
# ]
#
# users = current_users(events)
# print(users)
#
# generate_report(users)

# def get_event_date(event):
#     return event.date
#
#
# def current_users(events):
#     events.sort(key=get_event_date)
#     machines = {}
#     for event in events:
#         if event.machine not in machines:
#             machines[event.machine] = set()
#         if event.type == "login":
#             machines[event.machine].add(event.user)
#         elif event.type == "logout" and event.user in machines[event.machine]:
#             machines[event.machine].remove(event.user)
#     return machines
#
#
# def generate_report(machines):
#     for machine, users in machines.items():
#         if len(users) > 0:
#             user_list = ", ".join(users)
#             print("{}: {}".format(machine, user_list))
#
#
# class Event:
#     def __init__(self, event_date, event_type, machine_name, user):
#         self.date = event_date
#         self.type = event_type
#         self.machine = machine_name
#         self.user = user
#
#
# events = [
#     Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
#     Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
#     Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
#     Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
#     Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
#     Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
# ]
#
# users = current_users(events)
# print(users)
import fileupload as fileupload
import jupyter
import pip
import wordcloud as wordcloud
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys


# This is the uploader widget


def _upload():
    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 ** 10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)


_upload()


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~"'''
    uninteresting_words = ["the", "a", "to", "if", "is", "in" "it", "of", "and", "or", "on", "an", "as", "i", "me",
                           "my", \
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", \
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being", \
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how", \
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just"]

    # LEARNER CODE START HERE
    frequencies = {}
    taken = []
    for letter in punctuations:
        file_contents = file_contents.replace(letter, '')
    for word in uninteresting_words:
        w = ' ' + word + ' '
        file_contents = file_contents.replace(w, ' ')
    for word in file_contents.split():
        if word.lower() not in taken:
            taken.append(word.lower())
            if word not in frequencies:
                frequencies[word] = 1
            else:
                frequencies[word] += 1

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()


myimage = calculate_frequencies('download.png')
plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.show()
