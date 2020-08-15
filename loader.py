# -*- coding: utf-8 -*-
# em1tao

import requests
from bs4 import BeautifulSoup
import time

bad_chars = {bad_char: '' for bad_char in '\/:*?"<>|'} 

def main(image, tags, number_of_pages):
    s = requests.session()
    search_url = "https://pornhub.com/video/search?search=" + tags
    main_req = s.get(search_url)
    parsed_html = BeautifulSoup(main_req.content, "lxml")
    search_result = parsed_html.find("ul", {"id": "videoSearchResult"})
    video_items = search_result.findAll("li")
    for video_item in video_items[1::]:
        try:
            img_object = video_item.find("img")
            img_source = img_object["data-src"]
            img_get = requests.get(img_source)
            img_key = video_item["_vkey"]
            img_file = open(img_key+".png", "wb")
            img_file.write(img_get.content)
            img_file.close
        except:
            continue
         
    

