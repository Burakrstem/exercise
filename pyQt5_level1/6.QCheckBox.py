"""
Arayuze kontrol kutusu ekleme(QCheckBox)
radiobutton aksine mevcut seçeneklerden birkacini birden secmek veya hicbirini secmememek ixin
"""


import sys
from PyQt5 import QtWidgets

def arayuz():
    nesne=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("Arayuz Penceresi")
    pencere.setGeometry(250,250,500,300)
    

    kontrol1=QtWidgets.QCheckBox(pencere)
    kontrol1.setText("secenek 1")
    kontrol1.move(10,10)

    kontrol2=QtWidgets.QCheckBox(pencere)
    kontrol2.setText("secenek 1")
    kontrol2.move(10,30)

    kontrol3=QtWidgets.QCheckBox(pencere)
    kontrol3.setText("secenek 1")
    kontrol3.move(10,50)
    kontrol3.setCheckable(False) #secilemez

    print(kontrol3.isCheckable())


    pencere.show()
    sys.exit(nesne.exec_())

arayuz()