"""
QLineEdit=tek satirli giris kutusu
"""



#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets

def arayuz():
    nesne=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("Arayuz Penceresi")
    pencere.setGeometry(250,250,500,300)
    
    satir=QtWidgets.QLineEdit(pencere)
    #satir.setEchoMode(QtWidgets.QLineEdit.Password)    
    satir.setText("Robot1 Konum:2.4,5.8")
    satir.setReadOnly(True) 
    satir.setFixedSize(200,50)

    pencere.show()
    sys.exit(nesne.exec_())

arayuz()

