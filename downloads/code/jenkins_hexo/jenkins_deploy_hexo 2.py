#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import subprocess


print ""

print "########################################################################################################"

print ""

print "deploy hexo using Jenkins"

print "author:Wu Chenxu"

print "version:v2.0"

print ""

print "############################################## PARAMETERS  ##############################################"

print ""
hexo_dir = 'D:\快盘\hexo'

par_deploy_type =  os.environ.get('Deploy_type')

print "Deploy_type:"+par_deploy_type

print "############################################ hexo generate ##############################################"
subprocess.call('hexo clean', shell=True)
subprocess.call('hexo g', shell=True)


if par_deploy_type == 'local':
	print "start local server ...."
	p=subprocess.Popen(["start", "hexo", "server"], cwd = unicode(hexo_dir, 'utf8').encode('mbcs'),shell=True)
	print "start chrome web browser..."
	subprocess.Popen(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "http://localhost:4000"], shell=True)

else:
	print "start to deploy in github ..."
	subprocess.Popen(['start', 'hexo', 'deploy'], cwd = unicode(hexo_dir, 'utf8').encode('mbcs'), shell=True)
	
	
