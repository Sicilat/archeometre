import serial

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
print(ser.name)

while True:
	s = ser.read(10)
	line = ser.readline().rstrip().decode()
	print(line)