"""
Tiklaninca belirli fonksiyonu cagirir

"""
import sys
from PyQt5 import QtWidgets

def arayuz():
    nesne=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("Arayuz Penceresi")
    pencere.setGeometry(250,250,500,300)
    
    buton=QtWidgets.QPushButton(pencere)
    buton.setText("Kaydet")
    buton.setEnabled(False) #buton gecersiz kilmak


    pencere.show()
    sys.exit(nesne.exec_())

arayuz()