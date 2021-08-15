import loader

while True:
    print("Choose image file")
    screenshot_link = input(":")
    if screenshot_link[-3::] in ("png","jpg"):
        print(f"You choose '{screenshot_link}'")
        break

tags = []
print("Enter some tags (for example hair color) \nType '.' to stop")

while True:
    tag = input(":")
    if tag == "." and 1 <= len(tags) or len(tags) > 5:
        break
    tags.append(tag.strip())

links,titles = loader.main(screenshot_path=screenshot_link,tags=tags)

for i in range(len(links)):
    print(titles[i])
    print(links[i])
    print()
    