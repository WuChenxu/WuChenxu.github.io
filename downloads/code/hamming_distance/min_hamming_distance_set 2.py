#coding:utf-8 
#author: www.wuchenxu.com
#versin: 1.0
#date: 2016-05-18

#https://github.com/doukremt/distance
import distance as ds
def convertDec2BinStr(num):
	return '{0:08b}'.format(num)
	
	
data= [0]
min_hamming_distance = 4

for i in range(0, 255):
	counter = 0
	for j in data:
		if ds.hamming(convertDec2BinStr(j), convertDec2BinStr(i)) >= min_hamming_distance:
			counter +=1
		if counter == len(data):
			data.append(i)
			
for i in data:
	print convertDec2BinStr(i)+'(0x{0:02x})'.format(i)