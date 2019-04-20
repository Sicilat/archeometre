import serial, time, os
from math import *

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

def get_refs():
	data = [0, 0]
	f = open('./ref.txt', 'r', encoding = "UTF-8")
	lines = f.readlines()
	data[0], data[1] = int(lines[0].rstrip()), int(lines[1].rstrip())
	f.close()
	return data

def clear():
	os.system('clear||cls')

def write_file(data):
	f = open('./output.csv', 'a', encoding = "UTF-8")
	f.write(str(data[5]) + ',' + str(data[6]) + ',' + str(data[7]) + '\r\n')
	f.close()

def confirm_data(data):
	clear()
	print('Informations reçues !')
	print('Cap_A = ' + str(data[0]))
	print('Cap_B = ' + str(data[1]))
	print('Cap_C = ' + str(data[2]))
	print('Ultrason A = ' + str(data[3][0]))
	print('Ultrason B = ' + str(data[3][1]))
	print('Ultrason C = ' + str(data[3][2]))
	print('Moyenne Ultrasons = ' + str(data[4]))
	print('Ref_X = ' + str(data[5][0]))
	print('Ref_Z = ' + str(data[5][1]))
	print('Pos_X = ' + str(data[6]))
	print('Pos_Y = ' + str(data[7]))
	print('Pos_Z = ' + str(data[8]))
	print('Voulez-vous confirmer et enregistrer ces valeurs ? (y/n)')
	asw = 'o'
	while asw != 'y' and asw != 'n':
		asw = input('> ').lower()
	if asw == 'y':
		write_file(data)

def parse_lenght(data, cap_num):
	if cap_num == 0:
		return (data / 1024) * 1.39
	elif cap_num == 1:
		return (data / 1024) * 1.39
	else:
		return (data / 1024) * 1.39

def calculate(info):
	z, x = ((info[1] * info[1]) - (info[2] * info[2]) + 1) / 2 + info[5][1], ((info[0] * info[0]) - (info[1] * info[1]) - 1) / (-2) + info[5][0]
	return x, sqrt((info[1] * info[1]) - (x * x) - (z * z)) * -1 + info[4], z

def getUsMid(data):
	return (data[3][0] + data[3][1] + data[3][2]) / 3

def handle_data(ser, asw):
	if asw == 'trsm':
		data = [0, 0, 0, [0, 0, 0], 0, [0, 0], 0, 0, 0]
		data[0] = parse_lenght(float(ser.readline().rstrip().decode()), 0)
		data[1] = parse_lenght(float(ser.readline().rstrip().decode()), 1)
		data[2] = parse_lenght(float(ser.readline().rstrip().decode()), 2)
		data[3][0] = float(ser.readline().rstrip().decode())
		data[3][1] = float(ser.readline().rstrip().decode())
		data[3][2] = float(ser.readline().rstrip().decode())
		data[4], data[5][0], data[5][1], data[6], data[7], data[8] = getUsMid(data), get_refs(), calculate()
		confirm_data(data)

while True:
	s = ser.read(100)
	line = ser.readline().rstrip().decode()
	print(line)
	if line != '':
		handle_data(ser, line)
		ser.flushInput()
		ser.flushOutput()
	time.sleep(0.1)