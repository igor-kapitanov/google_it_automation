# import PIL
#
# image = PIL.Image.open("houses.jpg")
# print(image.size)


# !/usr/bin/env python3
import requests
import socket


def check_localhost():
    localhost = socket.gethostbyname('127.0.0.1')
    return localhost


def check_connectivity(status_code):
    request = requests.get("http://www.google.com")
    if status_code == 200:
        return True
    return False
