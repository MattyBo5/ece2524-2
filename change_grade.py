#!/usr/bin/env python

import re
import fileinput
from sys import stderr,stdout,argv,exit

def changeGrade(name,newGrade):
	for line in fileinput.input('-'):
		m = re.search(name,line)
		line = re.sub(r'\n','',line)
		if m:
			newline = re.sub(r'\d+',newGrade,line)
			print newline
		else:
			print line
	return



if __name__=='__main__':
	 
	if len(argv) != 3:
		stderr.write("Usage: change_grade.py STRING INTEGER\n")
		exit(1)
	else:
		changeGrade(argv[1],argv[2])
	
	










