import requests
import httplib2
from io import BytesIO
from threading import Thread
from bs4 import BeautifulSoup
from imagehash import average_hash
from PIL import Image


class Page(Thread):
    pageCount = 1
    fulls: list = []
    titles: list = []

    def __init__(self):
        super().__init__()
        self.link = f"https://pornhub.com/video/search?search={Page.tags}&page={Page.pageCount}"
        Page.pageCount += 1

    def run(self):
        """Parses one of the page."""
        main_request = requests.get(self.link)
        parsed_html = BeautifulSoup(main_request.content, "lxml")
        if search_result:= parsed_html.find("ul", {"id": "videoSearchResult"}):
            video_items = search_result.findAll("li")[1::]
            for video_item in video_items:
                preview_tag = video_item.find("img")
                preview_url = preview_tag["data-src"]
                image_driver = httplib2.Http('.cache')
                _, preview_bytes = image_driver.request(preview_url)
                preview_image = Image.open(BytesIO(preview_bytes)).convert("RGB")
                if self.are_similar(preview_image):
                    video_id = video_item['data-video-vkey']
                    Page.fulls.append(f"https://pornhub.com/view_video.php?viewkey={video_id}")
                    Page.titles.append(preview_tag["alt"])

    def are_similar(self, image) -> bool:
        return average_hash(Page.original_image) - average_hash(image) <= 16


def main(screenshot_path: str, tags: list) -> list:
    Page.original_image = Image.open(screenshot_path)
    Page.tags = "+".join(tags)
    pages = [Page() for x in range(1, 4)]
    for page in pages:
        page.start()
        page.join()
    return [Page.fulls, Page.titles]
