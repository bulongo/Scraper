from bs4 import BeautifulSoup as bs
import requests, sys

#A scipt to scrape sites and download the content depending on what file it type it is
#i.e. if it is a movie ask to download it or solmething of the sort

site = input("Enter a site to start scraping: ")

holder = requests.get(site)

soup = bs("lxml",holder.text)

for links in soup.findAll("a"):
    print(links)
