import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Add_Project_GUI import *



class AddProjects(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        self.AddProjects = Ui_Add_Projects()
        self.AddProjects.setupUi(self)

        #self.setUpMainUiFunction()

    def setUpMainUiFunction(self):
        pass
