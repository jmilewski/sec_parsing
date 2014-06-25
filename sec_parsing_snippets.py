# SEC parsing snippets

# --- urllib3 ---

import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'http://www.google.com')

# usage examples
r.status
r.headers
r.headers['server']
r.data


# --- beautifulsoup4 ---

from bs4 import BeautifulSoup

# xml parsing
soup = BeautifulSoup(markup, "xml")


# Use GNU Wget for downloading files locally - it is a commandlline tool.
# Usage in terminal $ wget [option]... [http]...



