# -*- coding: utf-8 -*-
# em1tao
import loader
import easygui

print("Choose image file")

while True:
    screenshot = easygui.fileopenbox()
    if screenshot[-3::] == "png" or screenshot[-3::] == "jpg":
        print(f"You choose '{screenshot}'")
        break
    else:
        print("Choose image file")

print("Enter some tags (for example hair color) \n Type '.' to stop")
TAGS = []
tag = ""

while True:
    tag = input(":")
    if tag == ".":
        if len(TAGS) >= 1:
            break
        else:
            print("Write at least 1 tag")
            continue
    else:
        TAGS.append(tag)

TAGS_STRING = "+".join(TAGS)
loader.main(screenshot, TAGS_STRING)