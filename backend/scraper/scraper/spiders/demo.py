from pathlib import Path
import scrapy
import json
import sys
from utils import helper
import re

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
        book_searched = helper.get_user_input("enter book: ")
        books_list = []
        found_books = False
        for books in response.css("article.product_pod"):
            book_title = books.css("h3 > a::attr(title)").get()
            is_available = str(books.css("div.product_price > p.instock").get())

            if "in stock" in is_available.lower():
                result = True
            else:
                result = False

            if book_searched in book_title.lower():
                book_page = re.sub(r'^<Request\s(GET|POST|PUT|DELETE|HEAD)\s(.*?)>$',r'\2',books.css("h3 > a::attr(href)").get())
                if book_page:
                    books_list.append(book_title)
                    found_books = True
                    yield {
                        "link" : response.follow(book_page, callback=self.parse),
                        "title": book_title,
                        "is_available" : result,
                        "price": books.css("div.product_price > p.price_color::text").get(),
                    }

        if not found_books:
            yield {
                "response": "book not found"
            }
        else:
            yield {
                "list_of_books": books_list
            }
    
    # TODO - create dictionary to store the titles and its corresponding links

