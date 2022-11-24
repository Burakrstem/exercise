"""
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
    satir.setReadOnly(True)

    buton=QtWidgets.QPushButton(pencere)
    buton.move(0,30)
    buton.setText("Gonder")

    def guncelle():
        satir.setText("1.22")

    buton.clicked.connect(guncelle)
    


    pencere.show()
    sys.exit(nesne.exec_())

arayuz()

