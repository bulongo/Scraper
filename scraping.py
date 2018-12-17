from bs4 import BeautifulSoup as bs
import requests, sys, webbrowser

#A scipt to scrape sites and download the page of a site and then sends it to webtopdf

site = input("Enter a site to start scraping: ")

holder = requests.get(site)

soup = bs(holder.text,"lxml")

links = []

'''for items in soup.findAll("a"):
    links.append(items.text)
    if items.isalpha():
        print(items.text)

#for things in links:
#    print(things) '''

for items in soup.findAll("title"):
    print(items)
