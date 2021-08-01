#! python3
# lucky.py - Opens several bing search results.

import requests, sys, webbrowser, bs4

print('bing...') # display text while downloading the bing page
res = requests.get('https://cn.bing.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

#Retrieve top search result links
soup=bs4.BeautifulSoup(res.text, features="html.parser")
link_elems = soup.select('div>h2>a[target="_blank"]')
numOpen = min(5, len(link_elems))
for i in range(numOpen):
    webbrowser.open(link_elems[i].get('href'))







