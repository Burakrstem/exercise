"""
Mizanpaj duzenleme nedir:
mevcut alandan en iyi sekilde yararlanmak icin araclari otomatik duzenleme
araclari otomatik konumlandirma
pencere icin makul minimum ve varsayilan boyutlar ayarlanabilir
arayuz penceresini yeniden tasarlamadan yeni araclar dinamik sekilde eklenebilir
farkli cozunurlukteki ekranlarda tek tip gorunum saglar

10.signal_slot arayuz penceresinin bir ucundan tutunca yok olacak kadar kuculebiliyor
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
    

    
    dikey=QtWidgets.QVBoxLayout()  #QVBoxLayout dikey
    dikey.addWidget(buton1)
    dikey.addWidget(buton2)
    yatay=QtWidgets.QHBoxLayout()
    yatay.addWidget(buton3)
    yatay.addWidget(buton4)

    dikey.addLayout(yatay)

    pencere.setLayout(dikey)


    

    pencere.show()
    sys.exit(nesne.exec_())

arayuz()


