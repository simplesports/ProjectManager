# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add_Project_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Add_Projects(object):
    def setupUi(self, Add_Projects):
        Add_Projects.setObjectName("Add_Projects")
        Add_Projects.resize(592, 724)
        self.gridLayout = QtWidgets.QGridLayout(Add_Projects)
        self.gridLayout.setObjectName("gridLayout")
        self.text_Additional_Comments = QtWidgets.QLabel(Add_Projects)
        self.text_Additional_Comments.setObjectName("text_Additional_Comments")
        self.gridLayout.addWidget(self.text_Additional_Comments, 7, 1, 1, 1)
        self.textEdit_Additional_Comments = QtWidgets.QTextEdit(Add_Projects)
        self.textEdit_Additional_Comments.setObjectName("textEdit_Additional_Comments")
        self.gridLayout.addWidget(self.textEdit_Additional_Comments, 8, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.text_Project_Number = QtWidgets.QLabel(Add_Projects)
        self.text_Project_Number.setObjectName("text_Project_Number")
        self.horizontalLayout.addWidget(self.text_Project_Number)
        self.UserInput_Project_Number = QtWidgets.QLineEdit(Add_Projects)
        self.UserInput_Project_Number.setObjectName("UserInput_Project_Number")
        self.horizontalLayout.addWidget(self.UserInput_Project_Number)
        self.text_Project_Name = QtWidgets.QLabel(Add_Projects)
        self.text_Project_Name.setObjectName("text_Project_Name")
        self.horizontalLayout.addWidget(self.text_Project_Name)
        self.UserInput_Project_Name = QtWidgets.QLineEdit(Add_Projects)
        self.UserInput_Project_Name.setObjectName("UserInput_Project_Name")
        self.horizontalLayout.addWidget(self.UserInput_Project_Name)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.Button_Add_Project = QtWidgets.QPushButton(Add_Projects)
        self.Button_Add_Project.setObjectName("Button_Add_Project")
        self.horizontalLayout_5.addWidget(self.Button_Add_Project)
        self.gridLayout.addLayout(self.horizontalLayout_5, 10, 1, 1, 1)
        self.groupBox_DueDates = QtWidgets.QGroupBox(Add_Projects)
        self.groupBox_DueDates.setObjectName("groupBox_DueDates")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_DueDates)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.UserInput_Description = QtWidgets.QLineEdit(self.groupBox_DueDates)
        self.UserInput_Description.setObjectName("UserInput_Description")
        self.gridLayout_2.addWidget(self.UserInput_Description, 1, 1, 1, 1)
        self.text_Description = QtWidgets.QLabel(self.groupBox_DueDates)
        self.text_Description.setObjectName("text_Description")
        self.gridLayout_2.addWidget(self.text_Description, 1, 0, 1, 1)
        self.text_date = QtWidgets.QLabel(self.groupBox_DueDates)
        self.text_date.setObjectName("text_date")
        self.gridLayout_2.addWidget(self.text_date, 1, 2, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox_DueDates)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_2.addWidget(self.dateEdit, 1, 3, 1, 1)
        self.Button_Add_To_Table_Due_Dates = QtWidgets.QPushButton(self.groupBox_DueDates)
        self.Button_Add_To_Table_Due_Dates.setObjectName("Button_Add_To_Table_Due_Dates")
        self.gridLayout_2.addWidget(self.Button_Add_To_Table_Due_Dates, 2, 3, 1, 1)
        self.tableWidget_Dates = QtWidgets.QTableWidget(self.groupBox_DueDates)
        self.tableWidget_Dates.setObjectName("tableWidget_Dates")
        self.tableWidget_Dates.setColumnCount(2)
        self.tableWidget_Dates.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Dates.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Dates.setHorizontalHeaderItem(1, item)
        self.gridLayout_2.addWidget(self.tableWidget_Dates, 3, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_DueDates, 5, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Add_Projects)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.text_Contact_name = QtWidgets.QLabel(self.groupBox)
        self.text_Contact_name.setObjectName("text_Contact_name")
        self.gridLayout_4.addWidget(self.text_Contact_name, 0, 0, 1, 1)
        self.UserInput_Main_Contact_Name = QtWidgets.QLineEdit(self.groupBox)
        self.UserInput_Main_Contact_Name.setObjectName("UserInput_Main_Contact_Name")
        self.gridLayout_4.addWidget(self.UserInput_Main_Contact_Name, 0, 1, 1, 1)
        self.UserInput_Main_Contact_PhoneNumber = QtWidgets.QLineEdit(self.groupBox)
        self.UserInput_Main_Contact_PhoneNumber.setObjectName("UserInput_Main_Contact_PhoneNumber")
        self.gridLayout_4.addWidget(self.UserInput_Main_Contact_PhoneNumber, 0, 3, 1, 1)
        self.text_Contact_PhoneNumber = QtWidgets.QLabel(self.groupBox)
        self.text_Contact_PhoneNumber.setObjectName("text_Contact_PhoneNumber")
        self.gridLayout_4.addWidget(self.text_Contact_PhoneNumber, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 4, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 0, 5, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_4.addWidget(self.checkBox, 0, 6, 1, 1)
        self.Button_Add_To_Table_Contacts = QtWidgets.QPushButton(self.groupBox)
        self.Button_Add_To_Table_Contacts.setObjectName("Button_Add_To_Table_Contacts")
        self.gridLayout_4.addWidget(self.Button_Add_To_Table_Contacts, 1, 6, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.gridLayout_4.addWidget(self.tableWidget, 2, 1, 1, 5)
        self.gridLayout.addWidget(self.groupBox, 4, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.text_Project_Folder = QtWidgets.QLabel(Add_Projects)
        self.text_Project_Folder.setObjectName("text_Project_Folder")
        self.horizontalLayout_3.addWidget(self.text_Project_Folder)
        self.UserInput_Project_Folder = QtWidgets.QLineEdit(Add_Projects)
        self.UserInput_Project_Folder.setObjectName("UserInput_Project_Folder")
        self.horizontalLayout_3.addWidget(self.UserInput_Project_Folder)
        self.Button_Browse = QtWidgets.QPushButton(Add_Projects)
        self.Button_Browse.setObjectName("Button_Browse")
        self.horizontalLayout_3.addWidget(self.Button_Browse)
        self.gridLayout.addLayout(self.horizontalLayout_3, 6, 1, 1, 1)

        self.retranslateUi(Add_Projects)
        QtCore.QMetaObject.connectSlotsByName(Add_Projects)

    def retranslateUi(self, Add_Projects):
        _translate = QtCore.QCoreApplication.translate
        Add_Projects.setWindowTitle(_translate("Add_Projects", "Form"))
        self.text_Additional_Comments.setText(_translate("Add_Projects", "Addtional Comments:"))
        self.text_Project_Number.setText(_translate("Add_Projects", "Project Number"))
        self.text_Project_Name.setText(_translate("Add_Projects", "Project Name"))
        self.Button_Add_Project.setText(_translate("Add_Projects", "Add Project"))
        self.groupBox_DueDates.setTitle(_translate("Add_Projects", "Due Dates"))
        self.text_Description.setText(_translate("Add_Projects", "Description:"))
        self.text_date.setText(_translate("Add_Projects", "Date:"))
        self.Button_Add_To_Table_Due_Dates.setText(_translate("Add_Projects", "Add to Table"))
        item = self.tableWidget_Dates.horizontalHeaderItem(0)
        item.setText(_translate("Add_Projects", "Description"))
        item = self.tableWidget_Dates.horizontalHeaderItem(1)
        item.setText(_translate("Add_Projects", "Due Date"))
        self.groupBox.setTitle(_translate("Add_Projects", "Contacts"))
        self.text_Contact_name.setText(_translate("Add_Projects", "Contact Name:"))
        self.text_Contact_PhoneNumber.setText(_translate("Add_Projects", "Contact Phone Number"))
        self.label.setText(_translate("Add_Projects", "Title:"))
        self.checkBox.setText(_translate("Add_Projects", "Main?"))
        self.Button_Add_To_Table_Contacts.setText(_translate("Add_Projects", "Add to Table"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Add_Projects", "Contact Name:"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Add_Projects", "Contact Phone Number:"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Add_Projects", "Title:"))
        self.text_Project_Folder.setText(_translate("Add_Projects", "Project Folder:"))
        self.Button_Browse.setText(_translate("Add_Projects", "Browse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Add_Projects = QtWidgets.QWidget()
    ui = Ui_Add_Projects()
    ui.setupUi(Add_Projects)
    Add_Projects.show()
    sys.exit(app.exec_())

