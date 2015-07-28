# -*- coding: utf-8 -*-
import scrapy


class DockerfileSpider(scrapy.Spider):
    name = "dockerfilespider"
    allowed_domains = ["github.com"]
    start_urls = (
        'http://www.github.com/',
    )

    def parse(self, response):
        pass
