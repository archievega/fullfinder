"""Loads PornHub and gets previews from videos."""
# -*- coding: utf-8 -*-
# em1tao
from io import BytesIO
import requests
from threading import Thread
from bs4 import BeautifulSoup
from imagehash import average_hash
from PIL import Image

def main(screenshot_link, tags, number_of_pages):
    """Search original image in PornHub's previews."""
    def page_parser(page_count, tags, *_):
        """Parses one of the page."""
        main_req = session.get(f"https://pornhub.com/video/search?search={tags}&page={page_count}")
        parsed_html = BeautifulSoup(main_req.content, "lxml")
        search_result = parsed_html.find("ul", {"id": "videoSearchResult"})
        video_items = search_result.findAll("li")
        for video_item in video_items[1::]:
            try:
                img_object = video_item.find("img") # Get an object and it's attributes
                img_source = img_object["data-src"]
                img_get = requests.get(img_source) # Convert bytestring to image
                img = Image.open(BytesIO(img_get.content)).convert("RGB")
                if average_hash(original_image) - average_hash(img) <= 15:
                    print(f"https://pornhub.com/view_video.php?viewkey={video_item['_vkey']}")
            except TypeError:
                continue
            except AttributeError:
                continue

    session = requests.session()
    original_image = Image.open(screenshot_link) # read original image
    threads = []
    for page_num in range(1, number_of_pages+1):
        thread = Thread(target=page_parser, args=(page_num, tags))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
