#This script is written to delete items from a file that are too 
#random and that would take a lot of time to select one at a time
#so it will be fed a list and a target directory to look in. If the files
#it is fed are in the directory then it will delete them.Else it will retur
#none.

#V 0.01

import os,sys

one,two,*three = sys.argv
#three is a list of all the items that you will give as arguments i.e. the items
#you want the script to check for in your target folder and deletes

for items in three:
    print(items)
