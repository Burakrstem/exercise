"""
QSpinBox  Spin box alani ekle   
            artip azalan metin kutusu
"""


#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets

def arayuz():
    nesne=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("Arayuz Penceresi")
    pencere.setGeometry(250,250,500,300)
    
    spin=QtWidgets.QDoubleSpinBox(pencere) #float kullanmak icin Double QSpinBox=int
    spin.setRange(5,25)
    spin.setSingleStep(0.5) #0.5 er artis

    

    



    pencere.show()
    sys.exit(nesne.exec_())

arayuz()

