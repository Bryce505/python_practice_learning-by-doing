# !python3
# download all xkcd comics -- code extracted from 'Automate the Boring Stuff with Python'

import requests,os,bs4

url = 'http://xkcd.com'
os.makedirs('xkcd',exist_ok=True)

while not url.endswith('#'):
    #download the page
    print('download page %s....'%url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text,"html.parser")

    #find the url of the comic image
    comic_elem = soup.select('#comic img')
    if comic_elem == []:
        print('cannot fiand comic image')
    else:
        comic_url = 'http:'+comic_elem[0].get('src')
        #download the image
        print('downloading image %s...'%(comic_url))
        res = requests.get(comic_url)
        res.raise_for_status()

        #save the image to ./xkcd
        image_file =open(os.path.join('xkcd',os.path.basename(comic_url)),'wb')
        for chunk in res.iter_content(1000000):
            image_file.write(chunk)
        image_file.close()
    #get the prev button is  url
    prev_link =soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com'+prev_link.get('href')
print('done')