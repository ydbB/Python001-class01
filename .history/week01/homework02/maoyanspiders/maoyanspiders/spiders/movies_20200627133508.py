# -*- coding: utf-8 -*-
import scrapy


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com\']
    start_urls = ['http://maoyan.com\/']

    # def parse(self, response):
    #     pass
    def start_request(self):
        url = f'https://maoyan.com/board/4'
        yie
