# Parsing SEC.gov files

# urllib3

import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'http://www.google.com')

# usage examples
r.status
r.headers
r.headers['server']
r.data


# beautifulsoup4

from bs4 import BeautifulSoup

soup = BeautifulSoup(markup, "xml")





# urllib2

import urllib2


