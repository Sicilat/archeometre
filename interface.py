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
	f = open('./output.txt', 'a', encoding = "UTF-8")
	f.write('Cap_A = ' + data[0] + '\r\n')
	f.write('Cap_B = ' + data[1] + '\r\n')
	f.write('Cap_C = ' + data[2] + '\r\n')
	f.write('Ref_X = ' + data[4][0] + '\r\n')
	f.write('Ref_Y = ' + data[3] + '\r\n')
	f.write('Ref_Z = ' + data[4][1] + '\r\n')
	f.write('Pos_X = ' + data[5] + '\r\n')
	f.write('Pos_Y = ' + data[6] + '\r\n')
	f.write('Pos_Z = ' + data[7] + '\r\n')
	f.close()
	return

def confirm_data(data):
	clear()
	print('Received information !')
	print('Cap_A = ' + data[0])
	print('Cap_B = ' + data[1])
	print('Cap_C = ' + data[2])
	print('Ref_X = ' + data[4][0])
	print('Ref_Y = ' + data[3])
	print('Ref_Z = ' + data[4][1])
	print('Pos_X = ' + data[5])
	print('Pos_Y = ' + data[6])
	print('Pos_Z = ' + data[7])
	print('Do you want to confirm this values ? (y/n)')
	asw = 'o'
	while asw != 'y' and asw != 'n':
		asw = input('> ').lower()
	if asw == 'y':
		write_file(data)
	else:
		return

def parse_lenght(data):
	return (data / 1024) * 1.39

def calculate(info):
	z = ((info[2] * info[2]) - (info[3] * info[3]) + 1) / 2
	x = ((info[1] * info[1]) - (info[2] * info[2]) - 1) / (-2)
	y = sqrt((info[2] * info[2]) - (x * x) - (z * z))
	return x, y, z

def handle_data(ser, asw, refs):
	if asw == 'trsm':
		data = [0, 0, 0, 0, [0, 0], 0, 0, 0]
		data[0] = parse_lenght(ser.readline().rstrip())
		data[1] = parse_lenght(ser.readline().rstrip())
		data[2] = parse_lenght(ser.readline().rstrip())
		data[3] = ser.readline().rstrip()
		refs = get_refs()
		data[4][0], data[4][1] = refs
		data[5], data[6], data[7] = calculate(data)
		confirm_data(data)

while True:
	s = ser.read(10)
	line = ser.readline().rstrip()
	if line != '':
		handle_data(ser, line, refs)
	ser.flushInput()
	ser.flushOutput()
	sleep(0.1)