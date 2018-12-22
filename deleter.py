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


os.chdir(target)
#need to add absolute path to this

'''for items in three:
#the for loop is not finding the items in os.getcwd,think B
    if items in os.getcwd():
        print(items)'''

#we will use os.walk for now

check = []

def get_items():
    global target
    for i,j,k in os.walk("./"):
        for items in k:
            check.append(items)

get_items()

#managed to make it show me the items in the target directory and to check if
#what I am looking equals one of the items in the directory. Now we need to make
#it ask to delete the item using the os command for deleting. #Multi platform baby
for items in check:
    if two == items:
        print("found it")
