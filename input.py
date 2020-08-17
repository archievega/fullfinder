"""Accepts original image and tags."""
# -*- coding: utf-8 -*-
import easygui
import loader
from datetime import datetime

start_time = datetime.now()
print("Choose image file")

while True: # picks original image
    screenshot_link = easygui.fileopenbox()
    if screenshot_link[-3::] == "png" or screenshot_link[-3::] == "jpg":
        print(f"You choose '{screenshot_link}'")
        break
    print("Choose image file")

print("Enter some tags (for example hair color) \nType '.' to stop")
TAGS = []

while True:
    tag = input(":")
    if tag == "." and 1 <= len(TAGS) <= 10:
        break
    TAGS.append(tag)

while True:
    try:
        NUMBER_OF_PAGES = int(input("Number of pages (Max 5): "))
        break
    except ValueError:
        print("Enter a normal number")


if NUMBER_OF_PAGES > 5:
    NUMBER_OF_PAGES = 5
elif NUMBER_OF_PAGES < 1:
    NUMBER_OF_PAGES = 1

TAGS = list(map(lambda x: x.replace(" ", "+"), TAGS))

TAGS = "+".join(TAGS)
loader.main(screenshot_link, TAGS, NUMBER_OF_PAGES)
print(datetime.now() - start_time)
