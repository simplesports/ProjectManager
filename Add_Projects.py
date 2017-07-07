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
        self.AddProjects.tableWidget_Contacts.doubleClicked.connect(self.editContacts)

        self.AddProjects.dateEdit.setCalendarPopup(True)
        dt = datetime.date.today()
        self.AddProjects.dateEdit.setDate(QDate(dt.year, dt.month, dt.day))

        self.AddProjects.Button_Dates_Update_Table.hide()
        self.AddProjects.Button_Contacts_Update_Table.hide()

        self.AddProjects.Button_Cancel.clicked.connect(self.cancelButton)


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

    def editContacts(self):

        row = self.AddProjects.tableWidget_Contacts.currentItem().row()

        ContactName = self.AddProjects.tableWidget_Contacts.item(row,0).text()
        ContactNumber = self.AddProjects.tableWidget_Contacts.item(row,1).text()
        ContactTitle = self.AddProjects.tableWidget_Contacts.item(row,2).text()
        ContactCompany = self.AddProjects.tableWidget_Contacts.item(row,3).text()
        ContactEmail = self.AddProjects.tableWidget_Contacts.item(row,4).text()
        mainContact = self.AddProjects.tableWidget_Contacts.item(row,5).text()
        self.AddProjects.Button_Contacts_Update_Table.show()
        self.AddProjects.Button_Add_To_Table_Contacts.hide()

        self.AddProjects.UserInput_Main_Contact_Name.setText(ContactName)
        self.AddProjects.UserInput_Main_Contact_PhoneNumber.setText(ContactNumber)
        self.AddProjects.UserInput_Company.setText(ContactCompany)
        self.AddProjects.UserInput_Title.setText(ContactTitle)
        self.AddProjects.UserInput_Email.setText(ContactEmail)

        #When you get back from Peru, make a cancel button for the update where it will just deselect and clear all the fields
        #Also if 'mainContact' is Yes then allow the box to be checked and have it checked. Then if it is checked de-enable the check box
        # if it is not then enable the check box. This way the main contact can be switched.

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
            db_filename = '.\DB\ProgramManagerDB.sqlite'
            with sqlite3.connect(db_filename) as conn:
                cursorProject = conn.cursor()
                if self.AddProjects.Button_Add_Project.text() == 'Update Project':
                    print('The Project was updated')

                    #fill in later once I get the Add fully working then we can do the edit, but this section is only for edit
                else:
                    PName = self.AddProjects.UserInput_Project_Name.text()
                    PNumber = self.AddProjects.UserInput_Project_Number.text()
                    PFolder = self.AddProjects.UserInput_Project_Folder.text()
                    addComments = self.AddProjects.textEdit_Additional_Comments.toPlainText()
                    icon = None
                    cursorProject.execute(""" INSERT INTO  Projects(Project_Name,Project_Number,Project_Folder,Add_Comments,Icon,status) VALUES (?,?,?,?,?,?)""",(PName,PNumber,PFolder,addComments,icon,0))
                    key = cursorProject.lastrowid
                    #This is for the contacts section.

                    for i in range(0,self.AddProjects.tableWidget_Contacts.rowCount()):
                        contactName = self.AddProjects.tableWidget_Contacts.item(i,0).text()
                        contactNumber = self.AddProjects.tableWidget_Contacts.item(i,1).text()
                        title = self.AddProjects.tableWidget_Contacts.item(i,2).text()
                        company = self.AddProjects.tableWidget_Contacts.item(i,3).text()
                        email = self.AddProjects.tableWidget_Contacts.item(i,4).text()
                        if self.AddProjects.tableWidget_Contacts.item(i,5).text() == 'Yes':
                            mainContact = 1
                        else:
                            mainContact = 0
                        cursorProject.execute(""" INSERT INTO  Contacts(Project,Contact_Name,Contact_PhoneNumber,Title,Main_Contact,company,email) VALUES (?,?,?,?,?,?,?)""",(key,contactName,contactNumber,title,mainContact,company,email))
                        #I wanted to make a script that would generate SQL code so it wouldn't be running a quary everytime, but i have an old version of sqlite, its not worth it at the moment

                    for i in range(0,self.AddProjects.tableWidget_Dates.rowCount()):
                        Desc = self.AddProjects.tableWidget_Dates.item(i,0).text()
                        date = self.AddProjects.tableWidget_Dates.item(i,1).text()
                        strDate =datetime.datetime.strptime(date, '%m/%d/%Y').strftime('%Y-%m-%d')
                        cursorProject.execute(""" INSERT INTO  DueDates(Project,Description,Due_Date) VALUES (?,?,?)""",(key,Desc,strDate))

            self.close()
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

    def cancelButton(self):
        self.close()

    def setProjectNumber(self,projectNumber):
        self.AddProjects.UserInput_Project_Number.setText(projectNumber)

    def setProjectName(self,projectName):
        self.AddProjects.UserInput_Project_Name.setText(projectName)

    def setContacts(self,SelectedProjectsContacts,MainContact):
        for i in range(0,len(SelectedProjectsContacts['contactName'])):
            self.AddProjects.tableWidget_Contacts.insertRow(i)
            self.AddProjects.tableWidget_Contacts.setItem(i, 0, QTableWidgetItem(SelectedProjectsContacts['contactName'][i]))
            self.AddProjects.tableWidget_Contacts.setItem(i, 1, QTableWidgetItem(SelectedProjectsContacts['contactNumber'][i]))
            self.AddProjects.tableWidget_Contacts.setItem(i, 2, QTableWidgetItem(SelectedProjectsContacts['title'][i]))
            self.AddProjects.tableWidget_Contacts.setItem(i, 3, QTableWidgetItem(SelectedProjectsContacts['company'][i]))
            self.AddProjects.tableWidget_Contacts.setItem(i, 4, QTableWidgetItem(SelectedProjectsContacts['email'][i]))

            if SelectedProjectsContacts['contactName'][i] == MainContact:
                self.AddProjects.tableWidget_Contacts.setItem(i,5, QTableWidgetItem('Yes'))
                self.AddProjects.checkBox.setEnabled(False)
                self.AddProjects.checkBox.setChecked(False)
            else:
                self.AddProjects.tableWidget_Contacts.setItem(i,5, QTableWidgetItem('No'))


    def setDueDates(self,SelectedProjectDates):
        for i in range(0,len(SelectedProjectDates['Dates'])):
            self.AddProjects.tableWidget_Dates.insertRow(i)
            self.AddProjects.tableWidget_Dates.setItem(i,0,QTableWidgetItem(SelectedProjectDates['Description'][i]))
            dateStr = SelectedProjectDates['Dates'][i].strftime("%m/%d/%Y")
            self.AddProjects.tableWidget_Dates.setItem(i,1, QTableWidgetItem(dateStr))

    def setProjectFolder(self,projectFolder):
        self.AddProjects.UserInput_Project_Folder.setText(projectFolder)

    def setComments(self,SelectedProjectComments):
        self.AddProjects.textEdit_Additional_Comments.setText(SelectedProjectComments)

    def setButton(self):
        self.AddProjects.Button_Add_Project.setText('Update Project')
