import serial, time, os

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
print(ser.name)
refs = [0, 0]

def get_refs():
	data = [0, 0]
	f = open('./ref.txt', 'r', encoding = "UTF-8")
	lines = f.readlines()
	data[0] = int(lines[0].rstrip())
	data[1] = int(lines[1].rstrip())
	f.close()
	return data

def clear():
	os.system('clear|cls')

def write_file(data):
	//To write

def confirm_data(data):
	clear()
	print('Received information !')
	print('Cap_A = ' + data[0])
	print('Cap_B = ' + data[1])
	print('Cap_C = ' + data[2])
	print('Ref_X = ' + data[4][0])
	print('Ref_Y = ' + data[3])
	print('Ref_Z = ' + data[4][1])
	print('Do you wnat to confirm this values ? (y/n)')
	asw = 'o'
	while asw != 'y' and asw != 'n':
		asw = input('> ').lower()
	if asw == 'y':
		write_file(data)
	else:
		return

def handle_data(ser, asw, refs):
	if asw == 'trsm':
		data = [0, 0, 0, 0, [0, 0]]
		data[0] = ser.readline().rstrip()
		data[1] = ser.readline().rstrip()
		data[2] = ser.readline().rstrip()
		data[3] = ser.readline().rstrip()
		refs = get_refs()
		data[4][0], data[4][1] = refs
		confirm_data(data)

while True:
	s = ser.read(10)
	line = ser.readline().rstrip()
	if line != '':
		handle_data(ser, line, refs)
	ser.flushInput()
	ser.flushOutput()
	sleep(0.1)