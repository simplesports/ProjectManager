import sys
import os
import sqlite3
import datetime

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Main_GUI import *
from Custom_List import *
from Add_Projects import *

import pdb



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        QWidget.__init__(self,parent)
        self.MainUi = Ui_MainWindow()
        self.MainUi.setupUi(self)
        self.setUpMainUiFunction()
        self.LoadProjects()
        self.MainUi.mouseReleaseEvent=self.mousePressEvent
        



    def setUpMainUiFunction(self):
        self.MainUi.groupBox_More_Details.hide()
        self.MainUi.Button_Mark_As_Finish.hide()
        self.MainUi.Button_See_More_Details.hide()
        self.MainUi.list_Current_Projects.itemClicked.connect(self.item_click)
        self.MainUi.Button_See_More_Details.clicked.connect(self.ShowMoreDetails)
        self.MainUi.Button_Hide_Details.clicked.connect(self.HideDetails)
        self.MainUi.Button_Add_Project.clicked.connect(self.AddProjectsShow)


    def LoadProjects(self):
        Projects = {}
        db_filename = '.\DB\ProgramManagerDB.sqlite'
        with sqlite3.connect(db_filename) as conn:
            cursorProject = conn.cursor()
            cursorProject.execute(""" select key,Project_Name, Project_Number, Project_Folder,Add_Comments, Icon from Projects """)

            for row in cursorProject.fetchall():
                Project = {'Project_Name':[],'Project_Number':[],'Project_Folder':[],'Comments':[],'icon':[]}
                dueDates = {'Description':[],'Dates':[]}
                key,projectName,ProjectNumber,ProjectFolder,Comments,Icon = row
                Project['Project_Name'].append(projectName)
                Project['Project_Number'].append(ProjectNumber)
                Project['Project_Folder'].append(ProjectFolder)
                Project['Comments'].append(Comments)
                Project['icon'].append(Icon)

                CustomWidget = CustomList()
                CustomWidget.setUpProjectNumber(str(ProjectNumber))
                CustomWidget.setUpProjectName(projectName)
                CustomWidget.setupProjectFoler('<a href='+ProjectFolder+'>Open Project Folder</a>')

                cursorProject.execute(""" select Contact_Name, Contact_PhoneNumber from Contacts where Main_Contact = 1 and Project = ?""", (key,))
                contactName,contactNumber = cursorProject.fetchone()
                CustomWidget.setUpMainName(contactName)
                CustomWidget.setUpMainNumber(contactNumber)

                cursorProject.execute(""" select Description, Due_Date from DueDates where Project = ?""", (key,))
                for dateRow in cursorProject.fetchall():
                    Desc,DueDate = dateRow
                    dueDates['Description'].append(Desc)
                    dAll = datetime.datetime.strptime(DueDate, '%m/%d/%Y')
                    dueDates['Dates'].append(dAll)

                #now = datetime.datetime.now().date()
                #closest = self.nearest(dueDates,now)

                #d = datetime.datetime.strptime(DueDate, '%m/%d/%Y')
                #test = datetime.date(int(splitDate[2]),int(splitDate[0]),int(splitDate[1]))
                now = datetime.datetime.now()
                NextDeliverableCheck = min(dt for dt in dueDates['Dates'] if dt > now)
                NextDeliverableSTR = NextDeliverableCheck.strftime("%m/%d/%Y")
                oldest = max(dueDates['Dates'])
                FinalDueDate = oldest.strftime("%m/%d/%Y")
                #pdb.set_trace()
                CustomWidget.setupNextDate(NextDeliverableSTR)
                CustomWidget.setupDate(FinalDueDate)


                myQListWidgetItem = QListWidgetItem(self.MainUi.list_Current_Projects)
                myQListWidgetItem.setSizeHint(CustomWidget.sizeHint())
                self.MainUi.list_Current_Projects.addItem(myQListWidgetItem)
                self.MainUi.list_Current_Projects.setItemWidget(myQListWidgetItem, CustomWidget)

                Projects.update({ProjectNumber:Project,'Due_Dates':dueDates})
                pdb.set_trace()

            #INSERT INTO "main"."Projects" ("Project_Name","Project_Number","Project_Folder","Add_Comments") VALUES (?1,?2,?3,?4)


    def item_click(self):
        self.MainUi.Button_Mark_As_Finish.show()
        self.MainUi.Button_See_More_Details.show()

    def ShowMoreDetails(self):
        self.MainUi.groupBox_More_Details.show()

    def HideDetails(self):
        self.MainUi.groupBox_More_Details.hide()

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
            self.MainUi.Button_Mark_As_Finish.hide()
            self.MainUi.Button_See_More_Details.hide()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
