#Practicing the with the urllib2 library
#this script will open a url and save the page source into a file called 'source.txt'


import urllib2
from urllib2 import urlopen


#web_header = 'Mozilla/4.0'
website = raw_input('Please enter your website: ')
x = 'http://'

openSite = urllib2.urlopen(x+website)
data = openSite.read()

f = open('source.txt', 'w')
f.write(data)
f.close()

