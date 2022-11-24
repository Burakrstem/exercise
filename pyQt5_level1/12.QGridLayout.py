"""
izgara mizanpaj duzenleme
"""

#!/usr/bin/env python3
import sys
from PyQt5 import QtWidgets

def arayuz():
    nesne=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("Arayuz Penceresi")
    pencere.setGeometry(250,250,500,300)   
    buton1=QtWidgets.QPushButton(pencere)
    buton1.setText("buton 1")
    buton2=QtWidgets.QPushButton(pencere)
    buton2.setText("buton 2") 
    buton3=QtWidgets.QPushButton(pencere)
    buton3.setText("buton 3")
    buton4=QtWidgets.QPushButton(pencere)
    buton4.setText("buton 4") #ust uste eklenmis dort buton
    


    mizanpaj=QtWidgets.QGridLayout()
    mizanpaj.addWidget(buton1,1,1)
    mizanpaj.addWidget(buton2,1,2)
    mizanpaj.addWidget(buton3,2,1)
    mizanpaj.addWidget(buton4,2,2)

    pencere.setLayout(mizanpaj)
    



    pencere.show()
    sys.exit(nesne.exec_())

arayuz()


