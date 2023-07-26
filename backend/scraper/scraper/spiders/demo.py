from pathlib import Path
import scrapy


"""
    Scrapy documentation for reference
    "https://docs.scrapy.org/en/latest/index.html"

"""

class BooksSpider(scrapy.Spider):
    name = "books"

    def start_requests(self):
        urls = [
            "https://books.toscrape.com/"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = f"books-{page}.html"
    #     Path(filename).write_bytes(response.body)

    
    def parse(self, response):
        for category in response.css("div.side_categories ul.nav-list > li > ul > li"):
            yield {
                "category": category.css("a::text").get().strip()
            }

    