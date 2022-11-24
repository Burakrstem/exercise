"""
duzenlenemeyen metin icin yer tutucu
hatirlatici-belirtec
QLabel
"""

#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets

def arayuz():
    nesne=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("Arayuz Penceresi")
    pencere.setGeometry(250,250,500,300)
    

    etiket=QtWidgets.QLabel(pencere)
    etiket.setText("Robot1 Konum")
    etiket.move(20,10)

    pencere.show()
    sys.exit(nesne.exec_())

arayuz()

