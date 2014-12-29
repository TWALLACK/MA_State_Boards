MA_State_Boards
===============

Scrapes more than 600 separate lists of board members from the Massachusetts Boards & Commissions web site. http://appointments.state.ma.us/

Written in Python. Uses BeautifulSoup, as well as some standard modules in Python.

Note: There are two Python files. The first file downloads all the board lists and places them in a directory. 
The second file goes through the directory, grabs the key information from each file and compiles it into a new delimited
text file.

In addition, you may have to first create the empty directory for your files and make sure that directory name is 
used in the script GrabLists. Then you want to deposit the second script, AnalzyeLists, into that new directory.

