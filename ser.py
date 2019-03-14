import serial

try:
	arduino = serial.Serial("/dev/ttyACM0", timeout=1)
except:
	print('Please check the port')

rawdata = 0

rawdata = str(arduino.readLine())
print(rawdata)
