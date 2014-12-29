#This script finds and downloads every board list on the Massachusetts governor's boards and commissions web site

#import modules
import urllib2
import re
import time

#URLs for all the sections of the state's boards and commissions site
URL=["http://appointments.state.ma.us/Results.aspx?PolArea=A%26F",
"http://appointments.state.ma.us/Results.aspx?PolArea=EDU",
"http://appointments.state.ma.us/Results.aspx?PolArea=ENV",
"http://appointments.state.ma.us/Results.aspx?PolArea=OHS",
"http://appointments.state.ma.us/Results.aspx?PolArea=C%26D",
"http://appointments.state.ma.us/Results.aspx?PolArea=LAB",
"http://appointments.state.ma.us/Results.aspx?PolArea=MISC",
"http://appointments.state.ma.us/Results.aspx?PolArea=DPL",
"http://appointments.state.ma.us/Results.aspx?PolArea=EPS",
"http://appointments.state.ma.us/Results.aspx?PolArea=T%26C"]

#Initialize global variables
strings =[]
boards = []

#Find the URLs for each individual board lists
for page in range(len(URL)):
    web_request = urllib2.urlopen(URL[page])
    html = web_request.read()
    strings = re.findall(r'brdid=\d+',html)
    time.sleep(5)
    for i in range(len(strings)):
        boards.append(strings[i])
print "There are " + str(len(strings)) + " board lists. They are: "
#print strings


#Save each board list to file directory
for board in range(len(boards)):
	web_request = urllib2.urlopen("http://appointments.state.ma.us/BoardDetail.aspx?" + (boards[board]))
	time.sleep(5)
	html_board = web_request.read()
	outfilename = (boards[board])
	outpath = 'c:/python27/boards3/' #You might want to rename directory
	outfile = open(outpath+outfilename+".html", 'w')
	outfile.write(html_board)
	outfile.close()
	print "printing" + boards[board]
print "Done"

