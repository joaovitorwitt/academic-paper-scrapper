from pathlib import Path
import scrapy
import json
import sys
from utils import helper

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

    
    def parse_categories(self, response):
        for category in response.css("div.side_categories ul.nav-list > li > ul > li"):
            yield {
                "category": category.css("a::text").get().strip()
            }


    def parse_books(self, response):
        for book in response.css("ol.row li.col-xs-6 article.product_pod"):
            is_available = str(book.css("div.product_price > p.instock").get())


            if "in stock" in is_available.lower():
                result = True
            else:
                result = False

            yield {
                "title": book.css("h3 > a::text").get(),
                "price": book.css("div.product_price > p.price_color::text").get(),
                "isAvailable": result 
            }


    def parse(self, response):
        book = helper.search_books()
        book_list = []
        returned_book = ""

        for element in response.css("article.product_pod"):
            book_list.append(element.css("h3 > a::attr(title)").get())

        returned_book = [bk for bk in book_list if book.lower() in bk.lower()]

        yield {
            "link" : returned_book
        }
            

        # for element in response.css("article.product_pod"):
        #     yield {
        #         "link" : element.css("h3 > a::attr(title)").get(),
        #         "book" : book
        #     }

            

