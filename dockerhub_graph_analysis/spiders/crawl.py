import requests
import os

def crawl_urls(urls):

	user = os.environ['github_user']
	password = os.environ['github_pass']

	r = requests.get(baseurl + queryparams + pagination, auth=(user, password))
	if(r.ok):
		repoItems = json.loads(r.text or r.content)
		urllist = map(html_url_getter, repoItems['items'])
		print urllist
		print len(urllist)


def html_url_getter(adict):
	return adict['html_url']
