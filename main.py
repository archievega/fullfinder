# -*- coding: utf-8 -*-
# em1tao
import easygui
import requests
from bs4 import BeautifulSoup

print("Choose image file")
while True:
    screenshot = easygui.fileopenbox()
    if screenshot[-3::] == "png" or screenshot[-3::] == "jpg":
        print(f"You choose '{screenshot}'")
        break
    else:
        print("Choose image file")

print("Enter some tags (for example hair color)\n Type '.' to stop")
tags = []
tag = ""

while True:
    tag = input(":")
    if tag == ".":
        if len(tags) >= 1:
            break
        else:
            print("Write at least 1 tag")
            continue
    else:
        tags.append(tag)

print(tags)