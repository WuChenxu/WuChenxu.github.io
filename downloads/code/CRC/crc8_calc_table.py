#!/user/bin/python3
# coding=utf-8
__author__ = "wu_chenxu@126.com"
__version__ = "1.1"
__date__ = "2019-12-21"

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
	print("uint8 g_crc8_table[256] = {")
	for i in range(0,256):
		if (i % 8 == 0):
			print("/*", i, ":*/", end='')
		print(hex(crc8_table[i]), end='')
		if (i <255):
			print(", ", end='')
		if ((i+1) % 8 == 0):
			print()
	print("}")
	
def crc_byte(data):
	if len(crc8_table) != 256:
		generate_crc_table()

	crcTemp = InitialValue 
	for byte in data:
		crcTemp ^= byte
		crcTemp = crc8_table[crcTemp]
	return (XorValue^crcTemp)
	
if __name__ == '__main__':
	print("Polynomial=",hex(Polynomial))
	print("InitialValue=", hex(InitialValue))
	print("XorValue=", hex(XorValue))
	generate_crc_table()
	print_crc8table()
	while True:
		string_input = input("please input data:")
		input_list = string_input.split()
		print(input_list)
		input_list = [eval(a) for a in input_list]
		print("CRC value:", hex(crc_byte(input_list)))
	os.system('pause')

