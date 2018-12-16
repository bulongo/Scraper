from bs4 import BeautifulSoup as bs
import requests, sys, webbrowser

#A scipt to scrape sites and download the content depending on what file it type it is
#i.e. if it is a movie ask to download it or solmething of the sort

site = input("Enter a site to start scraping: ")

holder = requests.get(site)

soup = bs(holder.text,"lxml")

links = []

for items in soup.findAll("a"):
    links.append(items.text)


for things in links:
    print(things)
