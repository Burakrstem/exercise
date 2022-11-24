"""
QSlider= slider alani ekle
        kullanici icin uzerinde kontrolcunun hareket edebilecegi alan
        robot hizi ayarlanabilir         
"""


#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets,QtCore

def arayuz():
    nesne=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("Arayuz Penceresi")
    pencere.setGeometry(250,250,500,300)
    
    
    slider=QtWidgets.QSlider(QtCore.Qt.Horizontal,pencere)
    slider.move(10,50)
    slider.setMinimum(0)
    slider.setMaximum(10)
    slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
    slider.setTickInterval(2)
    slider.setValue(5)


    pencere.show()
    sys.exit(nesne.exec_())

arayuz()

