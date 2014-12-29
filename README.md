MA_State_Boards
===============

Scrapes more than 600 separate lists of board members from the Massachusetts Boards & Commissions web site.

Written in Pyhthon. Uses BeautifulSoup, as well as some standard modules in Python.

Note: There are two python files. The first file downloads all the board lists and places them in a directory. 
The second file goes through the directory, grabs the key information from each file and compiles it into a new delimited
text file.

In addition, you may have to first create the empty directory for your files and make sure that directory name is 
used in the script grab_lists. Then you want to deposit the second script, analzye_lists, into that new directory.

