#Version 0.2
#this version aims to use a different approach
#it also only works on sites that have a next button

from bs4 import BeautifulSoup as bs
import requests

#A scipt to scrape sites and download the page of a site and then sends it to webtopdf

www = "www."
site = ""
new_site = ''

#def changer(): 

def site_getter():
    global site,new_site
    ext = "http://"
    choice = input("Would you like to add the http extension? (Y/N): ")
    if choice.capitalize() == "Y":
        site = input("Enter a site name: ")
        #kept having problems becuase i was using a local variable gloabally
        new_site = ext + www + site
    else:
        site = input("Enter name: ")
        new_site = www + site

site_getter()

holder = requests.get(new_site)

soup = bs(holder.text,"lxml")

tutorial_links = []
counter = 0

for links in soup.findAll("a"):
    if "Next" in links.text.strip().capitalize():
        tutorial_links.append(new_site + links['href'])
        print(tutorial_links)


