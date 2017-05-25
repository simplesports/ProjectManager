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

        self.setUpMainUiFunction()

    def setUpMainUiFunction(self):
        self.AddProjects.Button_Add_To_Table_Contacts.clicked.connect(self.addContacts)
        self.AddProjects.Button_Add_To_Table_Due_Dates.clicked.connect(self.addDates)
        #pass

    def addContacts(self):
        contactName = self.AddProjects.UserInput_Main_Contact_Name.text()
        contactNumber = self.AddProjects.UserInput_Main_Contact_PhoneNumber.text()
        title = self.AddProjects.UserInput_Title.text()
        company = self.AddProjects.UserInput_Company.text()
        email = self.AddProjects.UserInput_Email.text()

        if self.AddProjects.checkBox.isChecked():
            mainContact = 'Yes'
            self.AddProjects.checkBox.setEnabled(False)
            self.AddProjects.checkBox.setChecked(False)
        else:
            mainContact = 'No'

        rowPosition = self.AddProjects.tableWidget_Contacts.rowCount()
        self.AddProjects.tableWidget_Contacts.insertRow(rowPosition)
        self.AddProjects.tableWidget_Contacts.setItem(rowPosition,0,QTableWidgetItem(contactName))
        self.AddProjects.tableWidget_Contacts.setItem(rowPosition,1,QTableWidgetItem(contactNumber))
        self.AddProjects.tableWidget_Contacts.setItem(rowPosition,2,QTableWidgetItem(title))
        self.AddProjects.tableWidget_Contacts.setItem(rowPosition,3,QTableWidgetItem(company))
        self.AddProjects.tableWidget_Contacts.setItem(rowPosition,4,QTableWidgetItem(email))
        self.AddProjects.tableWidget_Contacts.setItem(rowPosition,5,QTableWidgetItem(mainContact))

    def addDates(self):
        Description = self.AddProjects.UserInput_Description.text()
        date = self.AddProjects.dateEdit.text()
        dateSplit = date.split('/')
        dateReformated = dateSplit[2]+'-'+dateSplit[0]+'-'+dateSplit[1]

        rowPosition = self.AddProjects.tableWidget_Dates.rowCount()
        self.AddProjects.tableWidget_Dates.insertRow(rowPosition)
        self.AddProjects.tableWidget_Dates.setItem(rowPosition,0, QTableWidgetItem(Description))
        self.AddProjects.tableWidget_Dates.setItem(rowPosition,1, QTableWidgetItem(date))
        #print(dateReformated)
