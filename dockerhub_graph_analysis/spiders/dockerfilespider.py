# -*- coding: utf-8 -*-
import scrapy


class DockerfileSpider(scrapy.Spider):
    name = "dockerfilespider"
    allowed_domains = ["github.com"]
    start_urls = (
        'https://github.com/docker-library/redis/tree/5e3f74f3edbbf8311b86e40e7ebe47f602981387/2.6',
    )

    def parse(self, response):
        pass
