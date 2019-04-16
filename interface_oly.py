import serial, time, os
from math import *

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
print(ser.name)
refs = [0, 0]

def get_refs():
	data = [0, 0]
	f = open('./ref_oly.txt', 'r', encoding = "UTF-8")
	lines = f.readlines()
	data[0] = int(lines[0].rstrip())
	data[1] = int(lines[1].rstrip())
	f.close()
	return data

def clear():
	os.system('clear||cls')

def write_file(data):
	f = open('./output_oly.txt', 'a', encoding = "UTF-8")
	f.write('\nCap_A = ' + str(data[0]) + '\r\n')
	f.write('US =    ' + str(data[1]) + '\r\n')
	f.write('Ref_X = ' + str(data[2][0]) + '\r\n')
	f.write('Ref_Z = ' + str(data[2][1]) + '\r\n')
	f.close()
	return

def confirm_data(data):
	clear()
	print('Received information !')
	print('Cap_A = ' + str(data[0]))
	print('US =    ' + str(data[1]))
	print('Ref_X = ' + str(data[2][0]))
	print('Ref_Z = ' + str(data[2][1]))
	print('Do you want to confirm these values ? (y/n)')
	asw = 'o'
	while asw != 'y' and asw != 'n':
		asw = input('> ').lower()
	if asw == 'y':
		write_file(data)
		return
	else:
		return

def parse_lenght(data):
	return (data / 1024) * 1.39

def handle_data(ser, asw, refs):
	if asw == 'trsm':
		data = [0, 0, [0, 0]]
		data[0] = parse_lenght(float(ser.readline().rstrip().decode()))
		data[1] = float(ser.readline().rstrip().decode())
		refs = get_refs()
		data[2][0], data[2][1] = refs
		confirm_data(data)
	return

while True:
	s = ser.read(10)
	line = ser.readline().rstrip().decode()
	print(line)
	if line != '':
		handle_data(ser, line, refs)
	ser.flushInput()
	ser.flushOutput()
	time.sleep(0.5)