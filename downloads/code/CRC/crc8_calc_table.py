# coding=utf-8
import os
Polynomial=0x1D
InitialValue = 0xFF
XorValue = 0xFF
crc8_table=[]
def crc_1byte(data):
	crc_1byte = data
	for i in range(0,8):
		if (crc_1byte & 0x80):
			crc_1byte <<= 1
			crc_1byte^=Polynomial
		else:
			crc_1byte<<=1
		crc_1byte &= 0xFF	
	return crc_1byte
		
def generate_crc_table():
	for i in range(0,256):
		crc8_table.append(crc_1byte(i))
		
def print_crc8table():
	#print as C array	
	print "uint8 g_crc8_table[256] = {"
	for i in range(0,256):
		if (i % 8 == 0):
			print "/*", i, ":*/",
		print hex(crc8_table[i]), 
		if (i <255):
			print ", ",
		if ((i+1) % 8 == 0):
			print
	print "}"
	
def crc_byte(data):
	crcTemp = InitialValue 
	for byte in data:
		crcTemp ^= byte
		crcTemp = crc8_table[crcTemp]
	return (XorValue^crcTemp)
	
if __name__ == '__main__':
	print "Polynomial=",hex(Polynomial)
	print "InitialValue=", hex(InitialValue)
	print "XorValue=", hex(XorValue)
	generate_crc_table()
	print_crc8table()
	while True:
		string_input = raw_input("please input data:")
		input_list = string_input.split()
		print input_list
		input_list = [eval(a) for a in input_list]
		print "CRC value:", hex(crc_byte(input_list))
	os.system('pause')

