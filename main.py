import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget

import gui
    
    
class Calculator(QWidget, gui.Ui_MainWindow):
    
    def __init__(self):
        super(Calculator, self).__init__()
        self.setupUi(self)
        
        self.pushButton_Calculate.clicked.connect(self\
            .hanle_calculate_button)
        
        
    def calculate_coord(self):
        EX = self.lineEdit_EX.text()
        EY = self.lineEdit_EY.text()
        EZ = self.lineEdit_EZ.text()
        
        TX = self.lineEdit_TX.text()
        TY = self.lineEdit_TY.text()
        TZ = self.lineEdit_TZ.text()
        
        RX = TX - EX
        RY = TY - EY
        RZ = TZ - EZ
        
        return RX, RY, RZ
    
    def anim_button(self): ...
    
    def show_result(self): ...
    
    def hanle_calculate_button(self):
        print(self.calculate_coord)
        



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    app.exec()
        
