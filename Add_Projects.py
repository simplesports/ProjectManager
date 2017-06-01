import sys
from os.path import expanduser
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Add_Project_GUI import *
from Main import *
import datetime
import pdb



class AddProjects(QWidget):
    signal = pyqtSignal()

    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        self.AddProjects = Ui_Add_Projects()
        self.AddProjects.setupUi(self)

        self.setUpMainUiFunction()

    def setUpMainUiFunction(self):
        self.AddProjects.Button_Add_To_Table_Contacts.clicked.connect(self.addContacts)
        self.AddProjects.Button_Add_To_Table_Due_Dates.clicked.connect(self.addDates)
        self.AddProjects.Button_Add_Project.clicked.connect(self.addProject)
        self.AddProjects.Button_Contacts_Remove.clicked.connect(self.removeContact)
        self.AddProjects.Button_Dates_Remove.clicked.connect(self.removeDate)
        self.AddProjects.Button_Browse.clicked.connect(self.browse)

        self.AddProjects.dateEdit.setCalendarPopup(True)
        dt = datetime.date.today()
        self.AddProjects.dateEdit.setDate(QDate(dt.year, dt.month, dt.day))

        self.AddProjects.Button_Dates_Update_Table.hide()
        self.AddProjects.Button_Contacts_Update_Table.hide()


    def addContacts(self):
        if self.checkContactsAdd() == True:
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

    def removeContact(self):
        index_list = []
        for model_index in self.AddProjects.tableWidget_Contacts.selectionModel().selectedRows():
            index = QPersistentModelIndex(model_index)
            index_list.append(index)

        for index in index_list:
            self.AddProjects.tableWidget_Contacts.removeRow(index.row())

    def addDates(self):
        Description = self.AddProjects.UserInput_Description.text()
        date = self.AddProjects.dateEdit.text()
        dateSplit = date.split('/')
        dateReformated = dateSplit[2]+'-'+dateSplit[0]+'-'+dateSplit[1]

        rowPosition = self.AddProjects.tableWidget_Dates.rowCount()
        self.AddProjects.tableWidget_Dates.insertRow(rowPosition)
        self.AddProjects.tableWidget_Dates.setItem(rowPosition,0, QTableWidgetItem(Description))
        self.AddProjects.tableWidget_Dates.setItem(rowPosition,1, QTableWidgetItem(date))

    def removeDate(self):
        index_list = []
        for model_index in self.AddProjects.tableWidget_Dates.selectionModel().selectedRows():
            index = QPersistentModelIndex(model_index)
            index_list.append(index)

        for index in index_list:
            self.AddProjects.tableWidget_Dates.removeRow(index.row())

    def browse(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        options |= QFileDialog.ShowDirsOnly
        try:
            my_dir = QFileDialog.getExistingDirectory(self,"Open File", expanduser("~"), options=options)
        except:
            pass

        self.AddProjects.UserInput_Project_Folder.setText(my_dir)
        
    @pyqtSlot()
    def addProject(self):
        check = self.checksToAddProject()
        if check == True:
            print('Project was added')
            self.signal.emit()

    def checksToAddProject(self):

        if self.AddProjects.tableWidget_Dates.rowCount() < 1:
            QMessageBox.about(self, "No Dates", "You need to add at least one date")
            return False

        if len(self.AddProjects.UserInput_Project_Number.text()) < 1:
            QMessageBox.about(self, "No Project Number", "You need to type in a project Number")
            return False
        else:
            try:
                val = float(self.AddProjects.UserInput_Project_Number.text())
            except:
                QMessageBox.about(self, "No Project Number", "The Project Number has to actually be a number")
                return False

        if len(self.AddProjects.UserInput_Project_Name.text()) < 1:
            QMessageBox.about(self, "No Project Name", "The Project needs a name")
            return False

        return True

    def checkContactsAdd(self):
        if len(self.AddProjects.UserInput_Main_Contact_Name.text()) < 1:
            QMessageBox.about(self, "No Project Name", "The contact needs a name, or how do you know who you will be calling!")
            return False

        return True
