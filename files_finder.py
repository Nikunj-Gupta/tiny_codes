# usage python image_finder.py
#!/usr/bin/python

import os, glob, Image, sys

#path = "/home/nikunj/Desktop"
#os.chdir("/home/nikunj/Desktop")

try:
	path = str(sys.argv[1])
	os.chdir(path)
	
	extension = "*" + str(sys.argv[2])
	
	pic_list = []
	
	pic_list = glob.glob(extension)
	pic_list.sort()
	
	print len(pic_list), 'files found...'
	for temp in pic_list:
		print temp
    	
except: 
	print "Usage: python image_finder.py <path> <file extension (with the dot)>"
	print "Suggestion: Check your path or your extension"


#cmd = 'fulla -g 0.0216776:-0.0799067:0.0566601:1 '
#for temp in pic_list:
#    repair = cmd + temp
#    os.popen(repair).read()
