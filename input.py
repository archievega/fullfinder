# -*- coding: utf-8 -*-
# em1tao
import loader
import easygui  # pick original photo


print("Choose image file")

while True:
    screenshot_link = easygui.fileopenbox()
    if screenshot_link[-3::] == "png" or screenshot_link[-3::] == "jpg":
        print(f"You choose '{screenshot_link}'")
        break
    else:
        print("Choose image file")

print("Enter some tags (for example hair color) \nType '.' to stop")
TAGS = []
tag = ""

while True:
    tag = input(":")
    if tag == "." or len(TAGS) > 10:
        if len(TAGS) >= 1:
            break
        else:
            print("Write at least 1 tag")
            continue
    else:
        TAGS.append(tag)


while True:
    try:
        number_of_pages = int(input("Number of pages (Max 5): "))
        break
    except ValueError:
        print("Enter a normal number")
        continue


if number_of_pages > 5:
    number_of_pages = 5
elif number_of_pages < 1:
    number_of_pages = 1

TAGS = list(map(lambda x: x.replace(" ", "+"), TAGS))

TAGS = "+".join(TAGS)
loader.main(screenshot_link, TAGS, number_of_pages)

