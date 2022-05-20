from gettext import translation
from unicodedata import digit


test_encoded_handle = "0x0009" #?

digits = {
	"1110111":0,
	"0010010":1,
	"1011101":2,
	"1011011":3,
	"0111010":4,
	"1101011":5,
	"1101111":6,
	"1010010":7,
	"1111111":8,
	"1111011":9,
}

bits2 = [
    "HOLD","ºF","ºC","->","MAX","MIN","%","AC","F","u(F)",
	"BT?","n(F)","Hz","ohm","K(ohm)","M(ohm)","V","m(V)",
	"DC","A","auto","?7","u(A)","m(A)","?8","?9","?10","?11"
]

xorkey = [0x41,0x21,0x73,0x55,0xa2,0xc1,0x32,0x71,0x66,0xaa,0x3b,0xd0,0xe2,0xa8,0x33,0x14,0x20,0x21,0xaa,0xbb]

testvalue = [0x1b, 0x84, 0x70, 0xb1, 0x49, 0x6a, 0x9f, 0x3c, 0x66, 0xaa, 0x3b] #TEST

def xor(x,y):
	return x ^ y

def hex_to_binary(x):
	return bin(int(x, base=16)).lstrip('0b').zfill(8)

def flip_binary_order(x):
	return x[::-1]

def rearange_bits(bits):
	reorder = [0,3,2,7,6,1,5,4] #7 segment display order
	rearranged = []
	digit = ""
	for x in range(len(bits)):
		for y in reorder:
			digit += bits[x][y]
			if len(digit) == 8:
				rearranged.append(digit)
				digit = ""
	return rearranged

fullbinary = ""
binary_array = []

for x in range(len(testvalue)):
	tohex = hex(xor(testvalue[x],xorkey[x])) #Bytewyse XOR operation
	tobinary = hex_to_binary(tohex) #convert to binary
	flipped = flip_binary_order(tobinary) #reverse binary
	binary_array.append(flipped)
	fullbinary += flipped
	print(f"tohex: {tohex}")
	print(f"tobinary: {tobinary}")
	print(f"flipped: {flipped}")
	print(f"fullbinary: {fullbinary}")

digit_segment = fullbinary[28:60] #7 segment display
symbols_section = fullbinary[60:88] #symbols

print(f"digit_segment: {digit_segment}")


segment_array = []

for x in range(0,len(digit_segment),8): #split into 8 bit segments
	segment_array.append(digit_segment[x:x+8])
	
print(f"segment_array: {segment_array}")

#rearange bits
rearranged_segment_array = rearange_bits(segment_array) #rearrange bits
print(f"rearranged_segment_array: {rearranged_segment_array}")


display = ""

for x in rearranged_segment_array:
	display += str(digits[x[1:8]])
	if x[0] == "1":
		display += "."
	
for x in range(len(symbols_section)):
	if symbols_section[x] == "1":
		display += str(bits2[x])
	

print(f"display: {display}")