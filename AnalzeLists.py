# This program goes through all the board files that we have downloaded and grabs the list of board members
# Place program in directory where you downloaded all the board lists

import os
import re
import urllib2
from bs4 import BeautifulSoup
# Import modules

# Get the current working directory 
path = os.getcwd()

# Build a list of the html files in there
reports = [ i for i in os.listdir(path) if i[-4:] == 'html' ]
outfilename = 'board_list.txt'
outfile = open(outfilename, 'w')
outfile.write("Board_Name|Person_Name|Title|Chair?|Date_Term_ends")
boards = str(len(reports))
print "There are " + boards + " boards in the folder."
seats = 0  #This is the number of seats on all the boards

#Goes through each list, grabs the table of board members and outputs them to pipe delimted text file
for g in reports:
   infile = open(g)
   board_list = infile.read()
   list =[]
   print g
   match = re.search(r"""730px; height:70px">([a-zA-Z0-9_\'\-&,\(\)\. ]*)<""", board_list)
   BoardName = match.group(1)
   soup = BeautifulSoup(board_list)
   for tag in soup.find_all(text=re.compile('Member Name')):
      table = tag.findParent('table').findParent('table')
   for string in table.strings:
      string=string.replace(u'\xa0',u'BLANK')
      if string != "\n":
         list.append(string)   
   for i in range(len(list)):
      if i>4 and (i+1)%4==0:
          #print BoardName + "|" + list[i-3] + "|" + list[i-2] + "|" + list[i-1] + "|" + list[i] 
          seats+=1
          outfile.write(BoardName + "|" + list[i-3] + "|" + list[i-2] + "|" + list[i-1] + "|" + list[i]+"\n") #Save results to file

print "There are " + str(seats) + " seats on " + boards + " boards." 
outfile.close()



