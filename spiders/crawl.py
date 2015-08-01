import os

import requests
import unicodedata
from bs4 import BeautifulSoup
from credentials import github_user, github_pass


def crawl_github_urls():
	from url_datasets.github_archive_urls import urls_with_docker
	pages = map(request_url_page, urls)


def request_url_page(url):
	r = requests.get(url, auth=(github_user, github_pass))

	if(r.ok):
		# repoItems = json.loads(r.text or r.content)
		parse_dockerfile_page(r.body)


def parse_dockerfile_page(self, response):
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

	return 0


def uni_to_str(uni):
    return unicodedata.normalize('NFKD', uni).encode('ascii', 'ignore')
