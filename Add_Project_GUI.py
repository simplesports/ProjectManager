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
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.text_Description = QtWidgets.QLabel(self.groupBox_DueDates)
        self.text_Description.setObjectName("text_Description")
        self.horizontalLayout_4.addWidget(self.text_Description)
        self.UserInput_Description = QtWidgets.QLineEdit(self.groupBox_DueDates)
        self.UserInput_Description.setObjectName("UserInput_Description")
        self.horizontalLayout_4.addWidget(self.UserInput_Description)
        self.text_date = QtWidgets.QLabel(self.groupBox_DueDates)
        self.text_date.setObjectName("text_date")
        self.horizontalLayout_4.addWidget(self.text_date)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox_DueDates)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_4.addWidget(self.dateEdit)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.Button_Add_To_Table_Due_Dates = QtWidgets.QPushButton(self.groupBox_DueDates)
        self.Button_Add_To_Table_Due_Dates.setObjectName("Button_Add_To_Table_Due_Dates")
        self.horizontalLayout_2.addWidget(self.Button_Add_To_Table_Due_Dates)
        self.Button_Dates_Update_Table = QtWidgets.QPushButton(self.groupBox_DueDates)
        self.Button_Dates_Update_Table.setObjectName("Button_Dates_Update_Table")
        self.horizontalLayout_2.addWidget(self.Button_Dates_Update_Table)
        self.Button_Dates_Remove = QtWidgets.QPushButton(self.groupBox_DueDates)
        self.Button_Dates_Remove.setObjectName("Button_Dates_Remove")
        self.horizontalLayout_2.addWidget(self.Button_Dates_Remove)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.tableWidget_Dates = QtWidgets.QTableWidget(self.groupBox_DueDates)
        self.tableWidget_Dates.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_Dates.setDragDropOverwriteMode(False)
        self.tableWidget_Dates.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget_Dates.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_Dates.setObjectName("tableWidget_Dates")
        self.tableWidget_Dates.setColumnCount(2)
        self.tableWidget_Dates.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Dates.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Dates.setHorizontalHeaderItem(1, item)
        self.gridLayout_3.addWidget(self.tableWidget_Dates, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_DueDates, 5, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Add_Projects)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.text_Contact_name = QtWidgets.QLabel(self.groupBox)
        self.text_Contact_name.setObjectName("text_Contact_name")
        self.gridLayout_4.addWidget(self.text_Contact_name, 0, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_4.addWidget(self.checkBox, 0, 7, 1, 1)
        self.text_Contact_PhoneNumber = QtWidgets.QLabel(self.groupBox)
        self.text_Contact_PhoneNumber.setObjectName("text_Contact_PhoneNumber")
        self.gridLayout_4.addWidget(self.text_Contact_PhoneNumber, 0, 2, 1, 1)
        self.UserInput_Main_Contact_Name = QtWidgets.QLineEdit(self.groupBox)
        self.UserInput_Main_Contact_Name.setObjectName("UserInput_Main_Contact_Name")
        self.gridLayout_4.addWidget(self.UserInput_Main_Contact_Name, 0, 1, 1, 1)
        self.text_Email = QtWidgets.QLabel(self.groupBox)
        self.text_Email.setObjectName("text_Email")
        self.gridLayout_4.addWidget(self.text_Email, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 2, 1, 1)
        self.UserInput_Title = QtWidgets.QLineEdit(self.groupBox)
        self.UserInput_Title.setObjectName("UserInput_Title")
        self.gridLayout_4.addWidget(self.UserInput_Title, 1, 1, 1, 1)
        self.tableWidget_Contacts = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget_Contacts.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_Contacts.setDragDropOverwriteMode(False)
        self.tableWidget_Contacts.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget_Contacts.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_Contacts.setObjectName("tableWidget_Contacts")
        self.tableWidget_Contacts.setColumnCount(6)
        self.tableWidget_Contacts.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Contacts.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Contacts.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Contacts.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Contacts.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Contacts.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Contacts.setHorizontalHeaderItem(5, item)
        self.gridLayout_4.addWidget(self.tableWidget_Contacts, 7, 1, 1, 6)
        self.UserInput_Company = QtWidgets.QLineEdit(self.groupBox)
        self.UserInput_Company.setObjectName("UserInput_Company")
        self.gridLayout_4.addWidget(self.UserInput_Company, 1, 3, 1, 4)
        self.UserInput_Email = QtWidgets.QLineEdit(self.groupBox)
        self.UserInput_Email.setObjectName("UserInput_Email")
        self.gridLayout_4.addWidget(self.UserInput_Email, 3, 1, 1, 6)
        self.UserInput_Main_Contact_PhoneNumber = QtWidgets.QLineEdit(self.groupBox)
        self.UserInput_Main_Contact_PhoneNumber.setObjectName("UserInput_Main_Contact_PhoneNumber")
        self.gridLayout_4.addWidget(self.UserInput_Main_Contact_PhoneNumber, 0, 3, 1, 4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.Button_Add_To_Table_Contacts = QtWidgets.QPushButton(self.groupBox)
        self.Button_Add_To_Table_Contacts.setObjectName("Button_Add_To_Table_Contacts")
        self.horizontalLayout_6.addWidget(self.Button_Add_To_Table_Contacts)
        self.Button_Contacts_Update_Table = QtWidgets.QPushButton(self.groupBox)
        self.Button_Contacts_Update_Table.setObjectName("Button_Contacts_Update_Table")
        self.horizontalLayout_6.addWidget(self.Button_Contacts_Update_Table)
        self.Button_Contacts_Remove = QtWidgets.QPushButton(self.groupBox)
        self.Button_Contacts_Remove.setObjectName("Button_Contacts_Remove")
        self.horizontalLayout_6.addWidget(self.Button_Contacts_Remove)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 6, 0, 1, 8)
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
        Add_Projects.setWindowTitle(_translate("Add_Projects", "Add a New Project :-)"))
        self.text_Additional_Comments.setText(_translate("Add_Projects", "Addtional Comments:"))
        self.text_Project_Number.setText(_translate("Add_Projects", "Project Number"))
        self.text_Project_Name.setText(_translate("Add_Projects", "Project Name"))
        self.Button_Add_Project.setText(_translate("Add_Projects", "Add Project"))
        self.groupBox_DueDates.setTitle(_translate("Add_Projects", "Due Dates"))
        self.text_Description.setText(_translate("Add_Projects", "Description:"))
        self.text_date.setText(_translate("Add_Projects", "Date:"))
        self.Button_Add_To_Table_Due_Dates.setText(_translate("Add_Projects", "Add to Table"))
        self.Button_Dates_Update_Table.setText(_translate("Add_Projects", "Update Table"))
        self.Button_Dates_Remove.setText(_translate("Add_Projects", "Remove"))
        item = self.tableWidget_Dates.horizontalHeaderItem(0)
        item.setText(_translate("Add_Projects", "Description"))
        item = self.tableWidget_Dates.horizontalHeaderItem(1)
        item.setText(_translate("Add_Projects", "Due Date"))
        self.groupBox.setTitle(_translate("Add_Projects", "Contacts"))
        self.text_Contact_name.setText(_translate("Add_Projects", "Contact Name:"))
        self.checkBox.setText(_translate("Add_Projects", "Main?"))
        self.text_Contact_PhoneNumber.setText(_translate("Add_Projects", "Contact Phone Number:"))
        self.text_Email.setText(_translate("Add_Projects", "Email:"))
        self.label.setText(_translate("Add_Projects", "Title:"))
        self.label_2.setText(_translate("Add_Projects", "Company:"))
        item = self.tableWidget_Contacts.horizontalHeaderItem(0)
        item.setText(_translate("Add_Projects", "Contact Name:"))
        item = self.tableWidget_Contacts.horizontalHeaderItem(1)
        item.setText(_translate("Add_Projects", "Contact Phone Number:"))
        item = self.tableWidget_Contacts.horizontalHeaderItem(2)
        item.setText(_translate("Add_Projects", "Title:"))
        item = self.tableWidget_Contacts.horizontalHeaderItem(3)
        item.setText(_translate("Add_Projects", "Company"))
        item = self.tableWidget_Contacts.horizontalHeaderItem(4)
        item.setText(_translate("Add_Projects", "Email"))
        item = self.tableWidget_Contacts.horizontalHeaderItem(5)
        item.setText(_translate("Add_Projects", "Main Contact"))
        self.Button_Add_To_Table_Contacts.setText(_translate("Add_Projects", "Add to Table"))
        self.Button_Contacts_Update_Table.setText(_translate("Add_Projects", "Update Table"))
        self.Button_Contacts_Remove.setText(_translate("Add_Projects", "Remove"))
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

