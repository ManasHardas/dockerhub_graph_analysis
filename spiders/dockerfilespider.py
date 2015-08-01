# -*- coding: utf-8 -*-
import scrapy
import unicodedata
from bs4 import BeautifulSoup


class DockerfileSpider(scrapy.Spider):
    name = "dockerfilespider"
    allowed_domains = ["github.com"]
    start_urls = github_urls()

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')

        title_uni = soup.title.get_text()
        title_str = uni_to_str(title_uni)

        filename = title_str.split()[3].replace('/', '-')
        print filename

        _filepath = r'../data/' + filename
        f = open(_filepath, 'w')
        f.write('NAME ' + filename + '\n')

        for line in soup.find_all('td'):
            stripped_line = uni_to_str(line.get_text()).strip()
            print stripped_line
            if stripped_line:
                f.write(stripped_line + '\n')


def uni_to_str(uni):
    return unicodedata.normalize('NFKD', uni).encode('ascii', 'ignore')
