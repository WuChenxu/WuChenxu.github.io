#encoding=utf-8
import sys
import urllib2
import re
import zlib
#http://pypi.python.org/pypi/chardet
import chardet
from chardet.universaldetector import UniversalDetector  


__author__ = 'wu_chenxu@126.com'
__version__ = '0.1'

urls = ['http://www.163.com.cn',
'http://www.sohu.com',
'http://www.qq.com',
'http://www.sina.com.cn',
'http://www.baidu.com',
'http://www.renren.com',
'http://www.iqiyi.com',
'http://www.taobao.com',
'http://www.jd.com',
'http://www.tweeter.com',
'http://www.gov.hk/',
'http://www.naver.com',
'http://www.rakuten.co.jp/']

def chardetect(html):
	#create a new detector object	
	detector = UniversalDetector()  
	for line in html.split('\n'):  
		#test in blocks until reach to limit  
		detector.feed(line)  
		if detector.done: break  
	#close detector object
	detector.close()  
	#output detect result 
	return detector.result  
	
def get_charset(url):
	request = urllib2.Request(url)
	#request for gzip file
	request.add_header('Accept-encoding', 'gzip')
	try:
		opener = urllib2.build_opener()
		response = opener.open(request, timeout=10)
		html = response.read()
		print 'URL:', url
		raw_headers = response.headers
		#print raw_headers
		#norm_header=dict(zip(map(lambda x:x.lower(), raw_headers.keys()),raw_headers.values()))
		#print norm_header
		
		#1.get the charset from response header
		contentType = raw_headers.get('Content-Type')

		matchObj = re.search('charset=(.*)', contentType)
		print 'response header: ',
		if matchObj:
			print matchObj.group(1)
		else:
			print 'None'
			
		#1.1 unzip the html if needed
		gzipped = raw_headers.get('Content-Encoding')
		if gzipped:
			html = zlib.decompress(html, 16+zlib.MAX_WBITS)
			
		#2. get charset from html page header
		matchObj = re.search('charset=([^ \t\n\r\f\v/>]*)', html[0:1024])
		print 'html     header: ',
		if matchObj:
			print matchObj.group(1).replace('"','')
		else:
			print 'None'
			
		#3. get charset by guessing the page content
		print 'chardet analysis: '+chardetect(html[0:10*1024]).get('encoding')
		#4. print the first 10 bytes of html
		print ":".join("{:02x}".format(ord(c)) for c in html[0:20])
		print " ".join( c for c in html[0:20])
		#print convert2sysEncode(html[0:1024])
	except Exception,e:  
		print url,':',Exception,":",e
		

def convert2sysEncode(data):
	'''
	convert the data content  to system charset
	'''
	sysEncode = sys.getfilesystemencoding()
	dataEncode = chardet.detect(data).get('encoding', 'utf-8')
	dataConvert2sysEncode = data.decode(dataEncode, 'ignore').encode(sysEncode)
	return dataConvert2sysEncode
	
if __name__ == '__main__':
	print "system charset:", sys.getfilesystemencoding()
	for url in urls:
		get_charset(url)
		print


