"""Loads PornHub and gets previews from videos."""
# -*- coding: utf-8 -*-
# em1tao
from io import BytesIO
import requests
from bs4 import BeautifulSoup
import cv2
import numpy as np
import compare

def main(screenshot_link, tags, number_of_pages):
    """Search original image in PornHub's previews."""
    session = requests.session()
    original_image = cv2.imread(screenshot_link) # read original image
    for page_num in range(1, number_of_pages+1):
        search_url = f"https://pornhub.com/video/search?search={tags}&page={page_num}"
        main_req = session.get(search_url)
        parsed_html = BeautifulSoup(main_req.content, "lxml")
        search_result = parsed_html.find("ul", {"id": "videoSearchResult"})
        video_items = search_result.findAll("li")
        for video_item in video_items[1::]:
            try:
                img_object = video_item.find("img") # Get an object and it's attributes
                img_source = img_object["data-src"]
                img_get = requests.get(img_source) # Convert bytestring to image
                img_stream = BytesIO(img_get.content)
                img = cv2.imdecode(np.fromstring(img_stream.read(), np.uint8), 1)
                if compare.compare_image(original_image, img) <= 12:
                    print(f"https://rt.pornhub.com/view_video.php?viewkey={video_item['_vkey']}")
            except IndexError:
                continue
