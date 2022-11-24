"""
QRadioButton=Pencere icindeki seceneklerden yalnizca birini secmeni saglar
"""
#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets

def arayuz():
    nesne=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("Arayuz Penceresi")
    pencere.setGeometry(250,250,500,300)



    radio1=QtWidgets.QRadioButton(pencere)
    radio1.setText("Secenek1")
    radio1.move(10,10)
    
    radio2=QtWidgets.QRadioButton(pencere)
    radio2.setText("Secenek2")
    radio2.move(10,30)
    
    radio3=QtWidgets.QRadioButton(pencere)
    radio3.setText("Secenek3")
    radio3.move(10,50)
    radio3.setCheckable(False) #secilemez kil  setEnable(False) da olur



    pencere.show()
    sys.exit(nesne.exec_())

arayuz()