"""
1.sys modulu ile QtWidgets modulunu ice aktar
2.uygulama nesnesi QApplication olustur
3.QWidget ile pencere olustur
4.Islemleri yap
5.Pencereyi goster
6.exec_() ile ana dongu saglanir
"""
#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets

def arayuz():
    nesne=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()

    pencere.setWindowTitle("Arayuz Penceresi")
    pencere.setGeometry(250,250,500,300)
    
    pencere.show()
    sys.exit(nesne.exec_())

arayuz()
