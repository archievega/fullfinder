# -*- coding: utf-8 -*-
# em1tao

import requests
from bs4 import BeautifulSoup

def main(image, tags):
    s = requests.session()
    search_url = "https://pornhub.com/video/search?search=" + tags
    main_req = s.get(search_url)
    parsed_html = BeautifulSoup(main_req.content, "lxml")
    search_result = parsed_html.find("ul", {"id": "videoSearchResult"})
    print(search_result)

