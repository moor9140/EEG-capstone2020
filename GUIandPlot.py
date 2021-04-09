# A GUI for a live plot of serial data. Specifically for an EEG headset.

# imports
# from PyQt5 import QtCore, QtGui
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
                             QDial, QDialog, QGridLayout, QGroupBox,
                             QHBoxLayout, QLabel, QLineEdit, QProgressBar,
                             QPushButton, QRadioButton, QScrollBar,
                             QSizePolicy, QSlider, QSpinBox, QStyleFactory,
                             QTableWidget, QTabWidget, QTextEdit,
                             QVBoxLayout, QWidget)
import serial
import serial.tools.list_ports
from numpy import *

# TO DO:
# inability to run if no serial connection
# add recording feature
# make more descriptive layout
# more baud rates, default = 9600
# pause and stop plotting

# class definitions


# Set up plot window
class MainWindow(QtGui.QMainWindow):
    baud = 9600
    port = "/dev/ttyACM0"
    windowWidth = 500
    nPlots = 8
    ser = None
    curves = []
    Xm = [[], [], [], [], [], [], [], []]  # there's gotta be a better way...
    ptr = -windowWidth

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.central_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.login_widget = LoginWidget(self)
        self.login_widget.button.clicked.connect(self.plotter)
        self.central_widget.addWidget(self.login_widget)
        self.curve = self.login_widget.plot.getPlotItem()
        self.timer = QtCore.QTimer()

    def plotter(self):
        '''runs once when button clicked. Sets up the plot'''
        self.curve.setWindowTitle("ok")
        self.baud = int(self.login_widget.baudcombo.currentText())
        self.port = self.login_widget.portcombo.currentText()
        self.ser = serial.Serial(self.port, self.baud)
        for i in range(self.nPlots):
            c = pg.PlotCurveItem(pen=(i, self.nPlots*1.3))
            self.curve.addItem(c)
            self.Xm[i] = linspace(0, 0, self.windowWidth)
            self.curves.append(c)
        for _ in range(10):
            self.ser.readline()
        self.timer.timeout.connect(self.updater)
        self.timer.start(0)


    def updater(self):
        '''Updates plot visuals and data.'''
        self.ser.flush()
        value = self.ser.readline()
        value = value.decode("ascii").rstrip()
        ypr = value.split(",")
        print(ypr)            # show outputs of arduino to console
        self.nPlots = len(ypr)
        self.ptr += 1
        for i in range(self.nPlots):
            self.Xm[i][:-1] = self.Xm[i][1:]
            self.Xm[i][-1] = int(ypr[i])
            self.curves[i].setData(self.Xm[i])
            self.curves[i].setPos(self.ptr, i*200)
        QtGui.QApplication.processEvents()


# Set up GUI buttons and lists
class LoginWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(LoginWidget, self).__init__(parent)
        layout = QtGui.QHBoxLayout()
        buttonlayout = QtGui.QVBoxLayout()

        self.baudcombo = QtGui.QComboBox()  # baud rates
        self.baudcombo.addItems(["9600", "115200"])
        buttonlayout.addWidget(self.baudcombo)

        self.portcombo = QtGui.QComboBox() # port names
        comports = serial.tools.list_ports.comports()
        comlist = []
        for item in comports:
            comlist.append(str(item[0]))
        # self.portcombo.addItems("/dev/ttyACM0")
        self.portcombo.addItems(comlist)
        buttonlayout.addWidget(self.portcombo)

        self.button = QtGui.QPushButton('Start') # start button
        buttonlayout.addWidget(self.button)

        layout.addLayout(buttonlayout) # finish layout
        self.plot = pg.PlotWidget()
        layout.addWidget(self.plot)
        self.setLayout(layout)

# main execution when run as standalone.
# If called by another module, just include this stuff below.


if __name__ == '__main__':

    app = QtGui.QApplication([])
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    app.exec_()
