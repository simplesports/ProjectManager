import sys
import os
import sqlite3
import datetime

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Main_GUI import *
from Custom_List import *
from Add_Projects import *

import pdb



Projects = {}
class MainWindow(QMainWindow):


    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        QWidget.__init__(self,parent)
        self.MainUi = Ui_MainWindow()
        self.MainUi.setupUi(self)
        self.setUpMainUiFunction()
        self.LoadCurrentProjects()
        self.loadCustomWidgets()
        self.MainUi.mouseReleaseEvent=self.mousePressEvent



    def setUpMainUiFunction(self):
        self.MainUi.groupBox_More_Details.hide()
        self.MainUi.Button_Mark_As_Finish.setEnabled(False)
        self.MainUi.Button_See_More_Details.setEnabled(False)
        self.MainUi.list_Current_Projects.itemClicked.connect(self.item_click)
        self.MainUi.Button_See_More_Details.clicked.connect(self.ShowMoreDetails)
        self.MainUi.Button_Hide_Details.clicked.connect(self.HideDetails)
        self.MainUi.Button_Add_Project.clicked.connect(self.AddProjectsShow)



    def LoadCurrentProjects(self):
        global Projects
        db_filename = '.\DB\ProgramManagerDB.sqlite'
        with sqlite3.connect(db_filename) as conn:
            cursorProject = conn.cursor()
#****************************************************************************************************************************************************************************************************************
            cursorProject.execute(""" select Project, Due_Date from DueDates ORDER BY date(Due_Date) """)

            curentAllDates = cursorProject.fetchall()
            now = datetime.datetime.now()
            dcheck = []
            for i in curentAllDates:
                dcheck.append(datetime.datetime.strptime(i[1], '%Y-%m-%d'))

            soonestDeliverable = min(dt for dt in dcheck if dt >= now)
            Startindex = dcheck.index(soonestDeliverable)

            currentOrderkey = []
            for i in range(Startindex, len(dcheck)):
                currentOrderkey.append(curentAllDates[i][0])

            currentfinalKeyOrder = []
            for i in range(0, len(currentOrderkey)):
                if currentOrderkey[i] in currentfinalKeyOrder:
                    pass
                else:
                    currentfinalKeyOrder.append(currentOrderkey[i])
            #pdb.set_trace()
#**************************************************************************************************************************************************************************************************************


            for key in currentfinalKeyOrder:
                cursorProject.execute(""" select Project_Name, Project_Number, Project_Folder,Add_Comments, Icon from Projects where key = ? and status = 0 """,(key,))
                for row in cursorProject.fetchall():
                    Project = {'Project_Name':[],'Project_Number':[],'Project_Folder':[],'Comments':[],'icon':[]}
                    dueDates = {'Description':[],'Dates':[]}
                    allContacts = {'contactName':[],'contactNumber':[],'title':[]}
                    projectName,ProjectNumber,ProjectFolder,Comments,Icon = row
                    Project['Project_Name'].append(projectName)
                    Project['Project_Number'].append(ProjectNumber)
                    Project['Project_Folder'].append(ProjectFolder)
                    Project['Comments'].append(Comments)
                    Project['icon'].append(Icon)

                    cursorProject.execute(""" select Contact_Name, Contact_PhoneNumber from Contacts where Main_Contact = 1 and Project = ?""", (key,))
                    MaincontactName,MaincontactNumber = cursorProject.fetchone()

                    cursorProject.execute(""" select Contact_Name, Contact_PhoneNumber,Title from Contacts where Project = ?""", (key,))
                    for contacts in cursorProject.fetchall():
                        contactName,contactNumber,title = contacts
                        allContacts['contactName'].append(contactName)
                        allContacts['contactNumber'].append(contactNumber)
                        allContacts['title'].append(title)

                    cursorProject.execute(""" select Description, Due_Date from DueDates where Project = ?""", (key,))
                    for dateRow in cursorProject.fetchall():
                        Desc,DueDate = dateRow
                        dueDates['Description'].append(Desc)
                        dAll = datetime.datetime.strptime(DueDate, '%Y-%m-%d')
                        dueDates['Dates'].append(dAll)

                    Project.update({'MaincontactName':MaincontactName,'MaincontactNumber':MaincontactNumber,'Contacts':allContacts,'Due_Dates':dueDates})

                    Projects.update({ProjectNumber:Project})


            #INSERT INTO "main"."Projects" ("Project_Name","Project_Number","Project_Folder","Add_Comments") VALUES (?1,?2,?3,?4)

    def loadCustomWidgets(self):
        global project_list
        project_list =[]
        for i in Projects:

            projectName = Projects[i]['Project_Name'][0]
            ProjectNumber = Projects[i]['Project_Number'][0]
            ProjectFolder = Projects[i]['Project_Folder'][0]
            Comments = Projects[i]['Comments'][0]
            icon = Projects[i]['icon'][0]
            contactName = Projects[i]['MaincontactName']
            contactNumber = Projects[i]['MaincontactNumber']

            now = datetime.datetime.now()
            NextDeliverableCheck = min(dt for dt in Projects[i]['Due_Dates']['Dates'] if dt > now)
            NextDeliverableSTR = NextDeliverableCheck.strftime("%m/%d/%Y")
            oldest = max(Projects[i]['Due_Dates']['Dates'])
            FinalDueDate = oldest.strftime("%m/%d/%Y")
            #pdb.set_trace()
            project_list.append(ProjectNumber)

            CustomWidget = CustomList()

            CustomWidget.setUpProjectNumber(str(ProjectNumber))
            CustomWidget.setUpProjectName(projectName)
            CustomWidget.setupProjectFoler('<a href=file:///'+ProjectFolder+'>Open Project Folder</a>')
            #remember to replace all spaces with %20 and all \ with / for the project folder and then it will work

            CustomWidget.setUpMainName(contactName)
            CustomWidget.setUpMainNumber(contactNumber)

            CustomWidget.setupNextDate(NextDeliverableSTR)
            CustomWidget.setupDate(FinalDueDate)

            myQListWidgetItem = QListWidgetItem(self.MainUi.list_Current_Projects)
            #pdb.set_trace()
            myQListWidgetItem.setSizeHint(CustomWidget.sizeHint())
            self.MainUi.list_Current_Projects.addItem(myQListWidgetItem)
            self.MainUi.list_Current_Projects.setItemWidget(myQListWidgetItem, CustomWidget)
            self._width = self.MainUi.list_Current_Projects.width()+5
            #self.adjustSize()


    def item_click(self, message):

        try:
            while self.MainUi.tableWidget_Contacts.rowCount() > 0:
                self.MainUi.tableWidget_Contacts.removeRow(0);
        except:
            pass

        try:
            while self.MainUi.tableWidget_DueDates.rowCount() > 0:
                self.MainUi.tableWidget_DueDates.removeRow(0);
        except:
            pass

        row = self.MainUi.list_Current_Projects.row(self.MainUi.list_Current_Projects.currentItem())
        project = project_list[row]

        projectName = Projects[project]['Project_Name'][0]
        ProjectNumber = Projects[project]['Project_Number'][0]
        ProjectFolder = Projects[project]['Project_Folder'][0]
        Comments = Projects[project]['Comments'][0]
        icon = Projects[project]['icon'][0]
        contactName = Projects[project]['MaincontactName']
        contactNumber = Projects[project]['MaincontactNumber']

        self.MainUi.text_ProjectName_CHANGE.setText(projectName)
        self.MainUi.text_ProjectFolder_CHANGE.setText('<a href=file:///'+ProjectFolder+'>Open Project Folder</a>')
        self.MainUi.text_ProjectFolder_CHANGE.setOpenExternalLinks(True)
        self.MainUi.textEdit.setText(Comments)

        for i in range(0,len(Projects[project]['Contacts']['contactName'])):
            self.MainUi.tableWidget_Contacts.insertRow(i)
            self.MainUi.tableWidget_Contacts.setItem(i, 0, QTableWidgetItem(Projects[project]['Contacts']['contactName'][i]))
            self.MainUi.tableWidget_Contacts.setItem(i, 1, QTableWidgetItem(Projects[project]['Contacts']['contactNumber'][i]))
            self.MainUi.tableWidget_Contacts.setItem(i, 2, QTableWidgetItem(Projects[project]['Contacts']['title'][i]))

        for i in range(0,len(Projects[project]['Due_Dates']['Dates'])):
            self.MainUi.tableWidget_DueDates.insertRow(i)
            self.MainUi.tableWidget_DueDates.setItem(i, 0, QTableWidgetItem(Projects[project]['Due_Dates']['Description'][i]))
            dateStr = Projects[project]['Due_Dates']['Dates'][i].strftime("%m/%d/%Y")
            self.MainUi.tableWidget_DueDates.setItem(i, 1, QTableWidgetItem(dateStr))


        self.MainUi.tableWidget_Contacts.resizeColumnsToContents()
        self.MainUi.tableWidget_DueDates.resizeColumnsToContents()
        self.MainUi.Button_Mark_As_Finish.setEnabled(True)
        self.MainUi.Button_See_More_Details.setEnabled(True)

    def ShowMoreDetails(self):
        self.MainUi.groupBox_More_Details.show()
        self.setFixedSize(width*2,height)

    def HideDetails(self):
        self.MainUi.groupBox_More_Details.hide()
        self.setFixedSize(width,height)

    def AddProjectsShow(self):
        global NewProjects
        NewProjects = AddProjects()
        NewProjects.show()
        #return NewProjects

    def nearest(self,items, pivot):
        return min(items, key=lambda x: abs(x - pivot))


    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.MainUi.list_Current_Projects.clearSelection()
            self.MainUi.groupBox_More_Details.hide()
            self.MainUi.Button_Mark_As_Finish.setEnabled(False)
            self.MainUi.Button_See_More_Details.setEnabled(False)
            self.setFixedSize(width,height)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    screen_resolution = app.desktop().screenGeometry()
    width, height = screen_resolution.width()/5, screen_resolution.height()/2
    MainWindow = MainWindow()
    MainWindow.resize(width,height)
    MainWindow.show()
    sys.exit(app.exec_())
