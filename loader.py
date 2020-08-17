"""Loads PornHub and gets previews from videos."""
# -*- coding: utf-8 -*-
from io import BytesIO
from threading import Thread
import requests
from bs4 import BeautifulSoup
from imagehash import average_hash
from PIL import Image

def main(screenshot_path, tags, number_of_pages):
    """Search original image in PornHub's previews."""
    class Page(Thread):
        """Page class"""
        TAGS = tags
        def __init__(self, link, *args, **kwargs):
            """Initialize page object."""
            super(Page, self).__init__(*args, **kwargs)
            self.link = link
            self.fulls = []

        def run(self):
            """Parses one of the page."""
            main_req = session.get(self.link)
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
                        self.fulls.append(f"https://pornhub.com/view_video.php?viewkey={video_item['_vkey']}")
                except TypeError as Exception:
                    print(Exception)
                    continue
                except AttributeError as Exception:
                    print(Exception)
                    continue

    session = requests.session()
    original_image = Image.open(screenshot_path) # Read original image
    pages = []
    for page_count in range(1, number_of_pages+1):
        page = Page(link=f"https://pornhub.com/video/search?search={tags}&page={page_count}") # Create page objects
        pages.append(page)
    for page in pages:
        page.start()
    for page in pages:
        page.join()
        print(*page.fulls, sep="\n")
