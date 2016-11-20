# coding=utf-8
import os
Polynomial=0x1D
InitialValue = 0xFF
XorValue = 0xFF
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
def crc_byte(data):
	crcTemp = InitialValue 
	for byte in data:
		crcTemp = (crc_1byte(crcTemp^byte))
	return XorValue^crcTemp
if __name__ == '__main__':
	print "Polynomial=",hex(Polynomial)
	print "InitialValue=", hex(InitialValue)
	print "XorValue=", hex(XorValue)
	while True:
		string_input = raw_input("please input data:")
		input_list = string_input.split()
		print input_list
		input_list = [eval(a) for a in input_list]
		print "CRC value:", hex(crc_byte(input_list))
	os.system('pause')

