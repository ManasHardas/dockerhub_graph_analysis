import requests
import json


def github_urls():
	baseurl = 'https://api.github.com/search/repositories'
	queryparams = '?q=docker%20in:name,description,readme'

	r = requests.get(baseurl + queryparams)
	if(r.ok):
		repoItems = json.loads(r.text or r.content)
		urllist = map(html_url_getter, repoItems['items'])
		print urllist


def html_url_getter(adict):
	return adict['html_url']

github_urls()
