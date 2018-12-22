#This script is written to delete items from a file that are too 
#random and that would take a lot of time to select one at a time
#so it will be fed a list and a target directory to look in. If the files
#it is fed are in the directory then it will delete them.Else it will retur
#none.

#V 0.01

import os,sys


one,two,*three = sys.argv
target = input("Enter your target folder: ")
#three is a list of all the items that you will give as arguments i.e. the items
#you want the script to check for in your target folder and deletes

#review: make it easier to identify files in later versions e.g. give it a folder
#of items it should store and then use the list it stores as arguments for the 
#removal in the target directory

os.chdir(target)
#need to add absolute path to this

'''for items in three:
#the for loop is not finding the items in os.getcwd,think B
    if items in os.getcwd():
        print(items)'''

#we will use os.walk for now

check = []

def get_items():
    for i,j,k in os.walk("./"):
        for items in k:
            check.append(items)

get_items()

for items in check:
    if two == items:
        os.remove(two)
        print(two + " removed")

#deletes items. It works....but why?!
