
#!/usr/bin/python

import os, glob, sys



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
