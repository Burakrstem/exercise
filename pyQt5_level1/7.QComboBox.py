"""
QComboBox arayuze acilir secim kutusu ekleme
"""
#!/usr/bin/env python3
import sys
from PyQt5 import QtWidgets

def arayuz():
    nesne=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("Arayuz Penceresi")
    pencere.setGeometry(250,250,500,300)
    
    combo=QtWidgets.QComboBox(pencere)
    combo.addItem("scan")
    combo.addItem("odom")
    combo.addItem("cmd_vel")
    
    print("eleman sayisi",combo.count())

    combo.setItemText(2,"kamera")

    pencere.show()
    sys.exit(nesne.exec_())

arayuz()