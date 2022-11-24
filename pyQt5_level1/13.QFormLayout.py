"""
iki sutunlu mizanpaj,  sol tarafi etiket ,sag tarafi giris alani
"""
#!/usr/bin/env python3
import sys
from PyQt5 import QtWidgets

def arayuz():
    nesne=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("Arayuz Penceresi")
    pencere.setGeometry(250,250,500,300)   
    


    etiket1=QtWidgets.QLabel(pencere)
    etiket1.setText("konum x:")
    etiket2=QtWidgets.QLabel(pencere)
    etiket2.setText("konum y:")

    satir1=QtWidgets.QLineEdit(pencere)
    satir2=QtWidgets.QLineEdit(pencere)
    mizanpaj=QtWidgets.QFormLayout()
    mizanpaj.addRow(etiket1,satir1)
    mizanpaj.addRow(etiket2,satir2)

    pencere.setLayout(mizanpaj)




    pencere.show()
    sys.exit(nesne.exec_())

arayuz()


