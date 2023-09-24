import requests
from bs4 import BeautifulSoup


target_url="https://www.haberler.com"
foundLinks=[]

def make_request(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")  # burada bunu özellikle hmtl.parser diye belli etmezsem allta bir uyarı verir ama çalışmasına engel olmaz
    return soup

def crawl(url):
    links=make_request(url)
    for link in links.find_all('a'):
        found_link=link.get("href")
        if found_link: #if found_link not in None
            if "#" in found_link:
                found_link=found_link.split("#")[0]
            if target_url in found_link and found_link not in foundLinks:
                foundLinks.append(found_link)
                print(found_link)
                #recursive
                crawl(found_link)

crawl(target_url)
#HTML Parsing