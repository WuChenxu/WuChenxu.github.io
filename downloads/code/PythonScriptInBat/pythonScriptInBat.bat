rem = """
@echo off
python.exe -d %0 %*
pause
goto endofPython """
 
import os
import sys
print "hello,python "
print "pwd: " + os.getcwd()

for i in range(0, len(sys.argv)):
	print "argv", i, sys.argv[i]
 
 
 
 
rem = """
:endofPython """