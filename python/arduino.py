import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.close()
ser.open()

data = ser.readline()
print (data)

ser.write(str.encode('1'))
time.sleep(5)
ser.write(str.encode('0'))
ser.write(str.encode('1'))
time.sleep(1)
ser.write(str.encode('0'))

ser.close()
