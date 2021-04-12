# imports
import serial
import serial.tools.list_ports
# from numpy import *

# TO DO:
# inability to run if no serial connection
# add recording feature
# make more descriptive layout
# more baud rates, default = 9600
# pause and stop plotting

# class definitions
class SerialGet():
    baud = 9600  # default
    port = "/dev/ttyACM0"  # default

    def __init__(self, baud, port):
        if baud:
            self.baud = baud
        if port:
            self.port = port
        self.ser = serial.Serial(self.port, self.baud)
        for _ in range(10):
            self.ser.readline()
        self.readval()

    def readval(self):
        self.ser.flush()
        value = self.ser.readline()
        value = value.decode("ascii").rstrip()
        self.ypr = list(map(int, value.split(",")))
        # self.ypr = value.split(",")
        self.nPlots = len(self.ypr)

    def __del__(self):
        self.ser.close()

# main execution when run as standalone.
# If called by another module, just include this stuff below.


if __name__ == '__main__':
    x = SerialGet(9600, "/dev/ttyACM0")
    while True:
        x.readval()
        print(x.ypr)
