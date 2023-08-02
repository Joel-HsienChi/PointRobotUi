from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit
import sys
import logging
from Logger import logger_class
from User import user
from helper_function import helper_function_class
from MySQL_function import MySQL_function_class

# UI class
class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(305, 240)
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.Login_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Login_Button.setGeometry(QtCore.QRect(40, 110, 113, 32))
        self.Login_Button.setObjectName("Login_Button")
        self.UserID_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.UserID_Input.setGeometry(QtCore.QRect(130, 30, 113, 21))
        self.UserID_Input.setText("")
        self.UserID_Input.setObjectName("UserID_Input")
        self.UserID_Label = QtWidgets.QLabel(self.centralwidget)
        self.UserID_Label.setGeometry(QtCore.QRect(50, 30, 60, 16))
        self.UserID_Label.setObjectName("UserID_Label")
        self.Password_Label = QtWidgets.QLabel(self.centralwidget)
        self.Password_Label.setGeometry(QtCore.QRect(50, 70, 60, 16))
        self.Password_Label.setObjectName("Password_Label")
        self.Password_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.Password_Input.setGeometry(QtCore.QRect(130, 70, 113, 21))
        self.Password_Input.setText("")
        self.Password_Input.setObjectName("Password_Input")
        self.Error_Message_for_password = QtWidgets.QLabel(self.centralwidget)
        self.Error_Message_for_password.setGeometry(
            QtCore.QRect(50, 150, 241, 21))
        self.Error_Message_for_password.setObjectName(
            "Error_Message_for_password")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(180, 110, 111, 31))
        self.checkBox.setObjectName("checkBox")
        self.Error_Message_for_permission = QtWidgets.QLabel(
            self.centralwidget)
        self.Error_Message_for_permission.setGeometry(
            QtCore.QRect(100, 150, 141, 21))
        self.Error_Message_for_permission.setObjectName(
            "Error_Message_for_permission")
        self.Error_Message_for_ID = QtWidgets.QLabel(self.centralwidget)
        self.Error_Message_for_ID.setGeometry(QtCore.QRect(120, 150, 141, 21))
        self.Error_Message_for_ID.setObjectName("Error_Message_for_ID")
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

        self.modding()

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.Login_Button.setText(_translate("Login", "Login"))
        self.Login_Button.setShortcut(_translate("Login", "Return"))
        self.UserID_Label.setText(_translate("Login", "UserID"))
        self.Password_Label.setText(_translate("Login", "Password"))
        self.Error_Message_for_password.setText(
            _translate("Login", "Wrong Password! Please try again!"))
        self.checkBox.setText(_translate("Login", "Admin mode"))
        self.Error_Message_for_permission.setText(
            _translate("Login", "You are not an Admin!"))
        self.Error_Message_for_ID.setText(
            _translate("Login", "ID doesn\'t exist!"))

    def modding(self):
        # hide the error message
        self.Error_Message_for_password.setHidden(True)
        self.Error_Message_for_permission.setHidden(True)
        self.Error_Message_for_ID.setHidden(True)

        # connect button to function
        self.Login_Button.clicked.connect(lambda: Login_function.login(
            self.UserID_Input.text(), self.Password_Input.text()))

        # mask the password
        self.Password_Input.setEchoMode(QLineEdit.Password)

class Ui_Info_Editor(object):
    current_user = user(None)
    def setupUi(self, Info_Editor):
        Info_Editor.setObjectName("Info_Editor")
        Info_Editor.resize(820, 180)
        self.Save_change_button = QtWidgets.QPushButton(Info_Editor)
        self.Save_change_button.setGeometry(QtCore.QRect(320, 140, 161, 32))
        self.Save_change_button.setMinimumSize(QtCore.QSize(161, 32))
        self.Save_change_button.setObjectName("Save_change_button")
        self.Display_table = QtWidgets.QTableWidget(Info_Editor)
        self.Display_table.setGeometry(QtCore.QRect(40, 30, 741, 71))
        self.Display_table.setMinimumSize(QtCore.QSize(0, 0))
        self.Display_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Display_table.setObjectName("Display_table")
        self.Display_table.setColumnCount(7)
        self.Display_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(6, item)
        self.Display_table.horizontalHeader().setVisible(True)
        self.Display_table.horizontalHeader().setCascadingSectionResizes(False)
        self.Display_table.horizontalHeader().setDefaultSectionSize(100)
        self.Display_table.horizontalHeader().setMinimumSectionSize(20)
        self.Display_table.horizontalHeader().setSortIndicatorShown(False)
        self.Display_table.horizontalHeader().setStretchLastSection(True)
        self.Password_Invalid = QtWidgets.QLabel(Info_Editor)
        self.Password_Invalid.setGeometry(QtCore.QRect(150, 110, 111, 31))
        self.Password_Invalid.setObjectName("Password_Invalid")
        self.Permission_Invalid = QtWidgets.QLabel(Info_Editor)
        self.Permission_Invalid.setGeometry(QtCore.QRect(330, 110, 121, 31))
        self.Permission_Invalid.setObjectName("Permission_Invalid")
        self.Gender_Invalid = QtWidgets.QLabel(Info_Editor)
        self.Gender_Invalid.setGeometry(QtCore.QRect(540, 110, 121, 31))
        self.Gender_Invalid.setObjectName("Gender_Invalid")

        self.retranslateUi(Info_Editor)
        QtCore.QMetaObject.connectSlotsByName(Info_Editor)

        self.modding()

    def retranslateUi(self, Info_Editor):
        _translate = QtCore.QCoreApplication.translate
        Info_Editor.setWindowTitle(_translate("Info_Editor", "Info_Editor"))
        self.Save_change_button.setText(_translate("Info_Editor", "Save change"))
        item = self.Display_table.horizontalHeaderItem(0)
        item.setText(_translate("Info_Editor", "Checkbox"))
        item = self.Display_table.horizontalHeaderItem(1)
        item.setText(_translate("Info_Editor", "ID"))
        item = self.Display_table.horizontalHeaderItem(2)
        item.setText(_translate("Info_Editor", "Password"))
        item = self.Display_table.horizontalHeaderItem(3)
        item.setText(_translate("Info_Editor", "Permission"))
        item = self.Display_table.horizontalHeaderItem(4)
        item.setText(_translate("Info_Editor", "Name"))
        item = self.Display_table.horizontalHeaderItem(5)
        item.setText(_translate("Info_Editor", "Gender"))
        item = self.Display_table.horizontalHeaderItem(6)
        item.setText(_translate("Info_Editor", "Plate amount"))
        self.Password_Invalid.setText(_translate("Info_Editor", "Password_Invalid"))
        self.Permission_Invalid.setText(_translate("Info_Editor", "Permission_Invalid"))
        self.Gender_Invalid.setText(_translate("Info_Editor", "Gender_Invalid"))

    def modding(self):

        # hide the error message
        self.Gender_Invalid.setHidden(True)
        self.Permission_Invalid.setHidden(True)
        self.Password_Invalid.setHidden(True)

        # connect button to function
        self.Save_change_button.clicked.connect(lambda: Login_function.Info_Editor_ui.Permission_Invalid.setHidden(True))
        self.Save_change_button.clicked.connect(lambda: Login_function.Info_Editor_ui.Gender_Invalid.setHidden(True))
        self.Save_change_button.clicked.connect(lambda: Login_function.Info_Editor_ui.Password_Invalid.setHidden(True))

        self.Save_change_button.clicked.connect(
            lambda: Info_Editor_function.press_save())

class Ui_Concentrate_Advance(object):
    current_user = user(None)
    def setupUi(self, Concentrate_Advance):
        Concentrate_Advance.setObjectName("Concentrate_Advance")
        Concentrate_Advance.resize(1350, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Concentrate_Advance.sizePolicy().hasHeightForWidth())
        Concentrate_Advance.setSizePolicy(sizePolicy)
        self.Search_Edit_Tab = QtWidgets.QWidget()
        self.Search_Edit_Tab.setObjectName("Search_Edit_Tab")
        self.Delete_User_button = QtWidgets.QPushButton(self.Search_Edit_Tab)
        self.Delete_User_button.setGeometry(QtCore.QRect(20, 580, 161, 32))
        self.Delete_User_button.setMinimumSize(QtCore.QSize(161, 32))
        self.Delete_User_button.setObjectName("Delete_User_button")
        self.Gender_label = QtWidgets.QLabel(self.Search_Edit_Tab)
        self.Gender_label.setGeometry(QtCore.QRect(50, 380, 81, 20))
        self.Gender_label.setMinimumSize(QtCore.QSize(81, 20))
        self.Gender_label.setObjectName("Gender_label")
        self.Show_all_button = QtWidgets.QPushButton(self.Search_Edit_Tab)
        self.Show_all_button.setGeometry(QtCore.QRect(20, 540, 161, 32))
        self.Show_all_button.setMinimumSize(QtCore.QSize(161, 32))
        self.Show_all_button.setObjectName("Show_all_button")
        self.Add_User_button = QtWidgets.QPushButton(self.Search_Edit_Tab)
        self.Add_User_button.setGeometry(QtCore.QRect(20, 620, 161, 32))
        self.Add_User_button.setMinimumSize(QtCore.QSize(161, 32))
        self.Add_User_button.setObjectName("Add_User_button")
        self.line_3 = QtWidgets.QFrame(self.Search_Edit_Tab)
        self.line_3.setGeometry(QtCore.QRect(60, 350, 201, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.Name_label = QtWidgets.QLabel(self.Search_Edit_Tab)
        self.Name_label.setGeometry(QtCore.QRect(50, 140, 61, 16))
        self.Name_label.setMinimumSize(QtCore.QSize(61, 16))
        self.Name_label.setObjectName("Name_label")
        self.Female_button = QtWidgets.QRadioButton(self.Search_Edit_Tab)
        self.Female_button.setGeometry(QtCore.QRect(140, 410, 100, 20))
        self.Female_button.setMinimumSize(QtCore.QSize(100, 20))
        self.Female_button.setObjectName("Female_button")
        self.buttongroup_gender = QtWidgets.QButtonGroup(Concentrate_Advance)
        self.buttongroup_gender.setObjectName("buttongroup_gender")
        self.buttongroup_gender.addButton(self.Female_button)
        self.line_2 = QtWidgets.QFrame(self.Search_Edit_Tab)
        self.line_2.setGeometry(QtCore.QRect(60, 220, 201, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.Permission_button = QtWidgets.QPushButton(self.Search_Edit_Tab)
        self.Permission_button.setGeometry(QtCore.QRect(100, 310, 160, 30))
        self.Permission_button.setMinimumSize(QtCore.QSize(140, 30))
        self.Permission_button.setObjectName("Permission_button")
        self.ID_input = QtWidgets.QLineEdit(self.Search_Edit_Tab)
        self.ID_input.setGeometry(QtCore.QRect(120, 20, 141, 21))
        self.ID_input.setMinimumSize(QtCore.QSize(141, 21))
        self.ID_input.setText("")
        self.ID_input.setObjectName("ID_input")
        self.line_4 = QtWidgets.QFrame(self.Search_Edit_Tab)
        self.line_4.setGeometry(QtCore.QRect(60, 500, 201, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.Name_search_button = QtWidgets.QPushButton(self.Search_Edit_Tab)
        self.Name_search_button.setGeometry(QtCore.QRect(120, 180, 140, 30))
        self.Name_search_button.setMinimumSize(QtCore.QSize(140, 30))
        self.Name_search_button.setObjectName("Name_search_button")
        self.Others_button = QtWidgets.QRadioButton(self.Search_Edit_Tab)
        self.Others_button.setGeometry(QtCore.QRect(140, 440, 100, 20))
        self.Others_button.setMinimumSize(QtCore.QSize(100, 20))
        self.Others_button.setObjectName("Others_button")
        self.buttongroup_gender.addButton(self.Others_button)
        self.ID_search_button = QtWidgets.QPushButton(self.Search_Edit_Tab)
        self.ID_search_button.setGeometry(QtCore.QRect(120, 60, 140, 30))
        self.ID_search_button.setMinimumSize(QtCore.QSize(0, 0))
        self.ID_search_button.setObjectName("ID_search_button")
        self.line = QtWidgets.QFrame(self.Search_Edit_Tab)
        self.line.setGeometry(QtCore.QRect(60, 100, 200, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Admin_button = QtWidgets.QRadioButton(self.Search_Edit_Tab)
        self.Admin_button.setGeometry(QtCore.QRect(140, 280, 100, 20))
        self.Admin_button.setMinimumSize(QtCore.QSize(100, 20))
        self.Admin_button.setObjectName("Admin_button")
        self.buttongroup_permission = QtWidgets.QButtonGroup(Concentrate_Advance)
        self.buttongroup_permission.setObjectName("buttongroup_permission")
        self.buttongroup_permission.addButton(self.Admin_button)
        self.Edit_error_message = QtWidgets.QLabel(self.Search_Edit_Tab)
        self.Edit_error_message.setGeometry(QtCore.QRect(200, 665, 81, 21))
        self.Edit_error_message.setMinimumSize(QtCore.QSize(71, 16))
        self.Edit_error_message.setObjectName("Edit_error_message")
        self.ID_label = QtWidgets.QLabel(self.Search_Edit_Tab)
        self.ID_label.setGeometry(QtCore.QRect(50, 20, 61, 16))
        self.ID_label.setMinimumSize(QtCore.QSize(61, 16))
        self.ID_label.setObjectName("ID_label")
        self.Gender_button = QtWidgets.QPushButton(self.Search_Edit_Tab)
        self.Gender_button.setGeometry(QtCore.QRect(100, 460, 160, 30))
        self.Gender_button.setMinimumSize(QtCore.QSize(160, 30))
        self.Gender_button.setObjectName("Gender_button")
        self.Male_button = QtWidgets.QRadioButton(self.Search_Edit_Tab)
        self.Male_button.setGeometry(QtCore.QRect(140, 380, 100, 20))
        self.Male_button.setMinimumSize(QtCore.QSize(100, 20))
        self.Male_button.setObjectName("Male_button")
        self.buttongroup_gender.addButton(self.Male_button)
        self.Permission_label = QtWidgets.QLabel(self.Search_Edit_Tab)
        self.Permission_label.setGeometry(QtCore.QRect(50, 250, 81, 20))
        self.Permission_label.setMinimumSize(QtCore.QSize(81, 20))
        self.Permission_label.setObjectName("Permission_label")
        self.User_button = QtWidgets.QRadioButton(self.Search_Edit_Tab)
        self.User_button.setGeometry(QtCore.QRect(140, 250, 100, 20))
        self.User_button.setMinimumSize(QtCore.QSize(100, 20))
        self.User_button.setObjectName("User_button")
        self.buttongroup_permission.addButton(self.User_button)
        self.Save_change_button = QtWidgets.QPushButton(self.Search_Edit_Tab)
        self.Save_change_button.setGeometry(QtCore.QRect(20, 660, 161, 32))
        self.Save_change_button.setMinimumSize(QtCore.QSize(161, 32))
        self.Save_change_button.setObjectName("Save_change_button")
        self.Name_input = QtWidgets.QLineEdit(self.Search_Edit_Tab)
        self.Name_input.setGeometry(QtCore.QRect(120, 140, 141, 21))
        self.Name_input.setMinimumSize(QtCore.QSize(141, 21))
        self.Name_input.setText("")
        self.Name_input.setObjectName("Name_input")
        self.User_info_pages = QtWidgets.QSpinBox(self.Search_Edit_Tab)
        self.User_info_pages.setGeometry(QtCore.QRect(700, 660, 81, 24))
        self.User_info_pages.setKeyboardTracking(False)
        self.User_info_pages.setObjectName("User_info_pages")
        self.Display_table = QtWidgets.QTableWidget(self.Search_Edit_Tab)
        self.Display_table.setGeometry(QtCore.QRect(320, 10, 1000, 623))
        self.Display_table.setMinimumSize(QtCore.QSize(800, 361))
        self.Display_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Display_table.setObjectName("Display_table")
        self.Display_table.setColumnCount(7)
        self.Display_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_table.setHorizontalHeaderItem(6, item)
        self.Display_table.horizontalHeader().setVisible(True)
        self.Display_table.horizontalHeader().setCascadingSectionResizes(False)
        self.Display_table.horizontalHeader().setDefaultSectionSize(100)
        self.Display_table.horizontalHeader().setMinimumSectionSize(20)
        self.Display_table.horizontalHeader().setSortIndicatorShown(False)
        self.Display_table.horizontalHeader().setStretchLastSection(True)
        self.ID_input.raise_()
        self.Delete_User_button.raise_()
        self.Gender_label.raise_()
        self.Show_all_button.raise_()
        self.Add_User_button.raise_()
        self.line_3.raise_()
        self.Name_label.raise_()
        self.Female_button.raise_()
        self.line_2.raise_()
        self.Permission_button.raise_()
        self.line_4.raise_()
        self.Name_search_button.raise_()
        self.Others_button.raise_()
        self.ID_search_button.raise_()
        self.line.raise_()
        self.Admin_button.raise_()
        self.Edit_error_message.raise_()
        self.ID_label.raise_()
        self.Gender_button.raise_()
        self.Male_button.raise_()
        self.Permission_label.raise_()
        self.User_button.raise_()
        self.Save_change_button.raise_()
        self.Name_input.raise_()
        self.User_info_pages.raise_()
        self.Display_table.raise_()
        Concentrate_Advance.addTab(self.Search_Edit_Tab, "")
        self.Login_History_Tab = QtWidgets.QWidget()
        self.Login_History_Tab.setObjectName("Login_History_Tab")
        self.ID_input_login_history = QtWidgets.QLineEdit(self.Login_History_Tab)
        self.ID_input_login_history.setGeometry(QtCore.QRect(120, 20, 141, 21))
        self.ID_input_login_history.setMinimumSize(QtCore.QSize(141, 21))
        self.ID_input_login_history.setText("")
        self.ID_input_login_history.setObjectName("ID_input_login_history")
        self.Password_doesnt_match_ID_button = QtWidgets.QRadioButton(self.Login_History_Tab)
        self.Password_doesnt_match_ID_button.setGeometry(QtCore.QRect(50, 290, 211, 20))
        self.Password_doesnt_match_ID_button.setMinimumSize(QtCore.QSize(100, 20))
        self.Password_doesnt_match_ID_button.setObjectName("Password_doesnt_match_ID_button")
        self.buttonGroup_fail_type = QtWidgets.QButtonGroup(Concentrate_Advance)
        self.buttonGroup_fail_type.setObjectName("buttonGroup_fail_type")
        self.buttonGroup_fail_type.addButton(self.Password_doesnt_match_ID_button)
        self.Success_button = QtWidgets.QRadioButton(self.Login_History_Tab)
        self.Success_button.setGeometry(QtCore.QRect(50, 140, 100, 20))
        self.Success_button.setMinimumSize(QtCore.QSize(100, 20))
        self.Success_button.setObjectName("Success_button")
        self.ID_label_login_history = QtWidgets.QLabel(self.Login_History_Tab)
        self.ID_label_login_history.setGeometry(QtCore.QRect(50, 20, 61, 16))
        self.ID_label_login_history.setMinimumSize(QtCore.QSize(61, 16))
        self.ID_label_login_history.setObjectName("ID_label_login_history")
        self.ID_doesnt_exist_button = QtWidgets.QRadioButton(self.Login_History_Tab)
        self.ID_doesnt_exist_button.setGeometry(QtCore.QRect(50, 260, 121, 20))
        self.ID_doesnt_exist_button.setMinimumSize(QtCore.QSize(100, 20))
        self.ID_doesnt_exist_button.setObjectName("ID_doesnt_exist_button")
        self.buttonGroup_fail_type.addButton(self.ID_doesnt_exist_button)
        self.ID_search_button_login_history = QtWidgets.QPushButton(self.Login_History_Tab)
        self.ID_search_button_login_history.setGeometry(QtCore.QRect(120, 60, 140, 30))
        self.ID_search_button_login_history.setMinimumSize(QtCore.QSize(0, 0))
        self.ID_search_button_login_history.setObjectName("ID_search_button_login_history")
        self.Display_Login_info = QtWidgets.QTableWidget(self.Login_History_Tab)
        self.Display_Login_info.setGeometry(QtCore.QRect(320, 10, 1000, 623))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Display_Login_info.sizePolicy().hasHeightForWidth())
        self.Display_Login_info.setSizePolicy(sizePolicy)
        self.Display_Login_info.setMinimumSize(QtCore.QSize(800, 360))
        self.Display_Login_info.setObjectName("Display_Login_info")
        self.Display_Login_info.setColumnCount(5)
        self.Display_Login_info.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Display_Login_info.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_Login_info.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_Login_info.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_Login_info.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_Login_info.setHorizontalHeaderItem(4, item)
        self.Display_Login_info.horizontalHeader().setCascadingSectionResizes(False)
        self.Display_Login_info.horizontalHeader().setDefaultSectionSize(100)
        self.Display_Login_info.horizontalHeader().setStretchLastSection(True)
        self.Fail_button = QtWidgets.QRadioButton(self.Login_History_Tab)
        self.Fail_button.setGeometry(QtCore.QRect(150, 140, 100, 20))
        self.Fail_button.setMinimumSize(QtCore.QSize(100, 20))
        self.Fail_button.setObjectName("Fail_button")
        self.Fail_type_button = QtWidgets.QPushButton(self.Login_History_Tab)
        self.Fail_type_button.setGeometry(QtCore.QRect(120, 350, 140, 30))
        self.Fail_type_button.setMinimumSize(QtCore.QSize(140, 30))
        self.Fail_type_button.setObjectName("Fail_type_button")
        self.Status_show_button = QtWidgets.QPushButton(self.Login_History_Tab)
        self.Status_show_button.setGeometry(QtCore.QRect(120, 180, 140, 30))
        self.Status_show_button.setMinimumSize(QtCore.QSize(140, 30))
        self.Status_show_button.setObjectName("Status_show_button")
        self.Show_all_button_login_history = QtWidgets.QPushButton(self.Login_History_Tab)
        self.Show_all_button_login_history.setGeometry(QtCore.QRect(120, 530, 140, 30))
        self.Show_all_button_login_history.setMinimumSize(QtCore.QSize(140, 30))
        self.Show_all_button_login_history.setObjectName("Show_all_button_login_history")
        self.line_5 = QtWidgets.QFrame(self.Login_History_Tab)
        self.line_5.setGeometry(QtCore.QRect(60, 100, 200, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.Login_History_Tab)
        self.line_6.setGeometry(QtCore.QRect(60, 220, 200, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.Login_History_Tab)
        self.line_7.setGeometry(QtCore.QRect(60, 380, 200, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.User_enter_advance_button = QtWidgets.QRadioButton(self.Login_History_Tab)
        self.User_enter_advance_button.setGeometry(QtCore.QRect(50, 320, 241, 20))
        self.User_enter_advance_button.setMinimumSize(QtCore.QSize(100, 20))
        self.User_enter_advance_button.setObjectName("User_enter_advance_button")
        self.buttonGroup_fail_type.addButton(self.User_enter_advance_button)
        self.Success_type_button = QtWidgets.QPushButton(self.Login_History_Tab)
        self.Success_type_button.setGeometry(QtCore.QRect(120, 470, 161, 32))
        self.Success_type_button.setMinimumSize(QtCore.QSize(141, 32))
        self.Success_type_button.setObjectName("Success_type_button")
        self.Normal_login_button = QtWidgets.QRadioButton(self.Login_History_Tab)
        self.Normal_login_button.setGeometry(QtCore.QRect(50, 410, 121, 20))
        self.Normal_login_button.setMinimumSize(QtCore.QSize(100, 20))
        self.Normal_login_button.setObjectName("Normal_login_button")
        self.buttongroup_success_type = QtWidgets.QButtonGroup(Concentrate_Advance)
        self.buttongroup_success_type.setObjectName("buttongroup_success_type")
        self.buttongroup_success_type.addButton(self.Normal_login_button)
        self.Advance_login_button = QtWidgets.QRadioButton(self.Login_History_Tab)
        self.Advance_login_button.setGeometry(QtCore.QRect(50, 440, 121, 20))
        self.Advance_login_button.setMinimumSize(QtCore.QSize(100, 20))
        self.Advance_login_button.setObjectName("Advance_login_button")
        self.buttongroup_success_type.addButton(self.Advance_login_button)
        self.line_8 = QtWidgets.QFrame(self.Login_History_Tab)
        self.line_8.setGeometry(QtCore.QRect(60, 500, 200, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.Login_History_Pages = QtWidgets.QSpinBox(self.Login_History_Tab)
        self.Login_History_Pages.setGeometry(QtCore.QRect(700, 660, 81, 24))
        self.Login_History_Pages.setKeyboardTracking(False)
        self.Login_History_Pages.setObjectName("Login_History_Pages")
        self.ID_input_login_history.raise_()
        self.Password_doesnt_match_ID_button.raise_()
        self.Success_button.raise_()
        self.ID_label_login_history.raise_()
        self.ID_doesnt_exist_button.raise_()
        self.ID_search_button_login_history.raise_()
        self.Fail_button.raise_()
        self.Fail_type_button.raise_()
        self.Status_show_button.raise_()
        self.Show_all_button_login_history.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.line_7.raise_()
        self.User_enter_advance_button.raise_()
        self.Success_type_button.raise_()
        self.Normal_login_button.raise_()
        self.Advance_login_button.raise_()
        self.line_8.raise_()
        self.Login_History_Pages.raise_()
        self.Display_Login_info.raise_()
        Concentrate_Advance.addTab(self.Login_History_Tab, "")
        self.Plate_Scan_Tab = QtWidgets.QWidget()
        self.Plate_Scan_Tab.setObjectName("Plate_Scan_Tab")
        self.Display_Plate_Info = QtWidgets.QTableWidget(self.Plate_Scan_Tab)
        self.Display_Plate_Info.setGeometry(QtCore.QRect(320, 10, 1000, 623))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Display_Plate_Info.sizePolicy().hasHeightForWidth())
        self.Display_Plate_Info.setSizePolicy(sizePolicy)
        self.Display_Plate_Info.setMinimumSize(QtCore.QSize(800, 360))
        self.Display_Plate_Info.setObjectName("Display_Plate_Info")
        self.Display_Plate_Info.setColumnCount(6)
        self.Display_Plate_Info.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Display_Plate_Info.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_Plate_Info.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_Plate_Info.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_Plate_Info.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_Plate_Info.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Display_Plate_Info.setHorizontalHeaderItem(5, item)
        self.Display_Plate_Info.horizontalHeader().setCascadingSectionResizes(False)
        self.Display_Plate_Info.horizontalHeader().setDefaultSectionSize(10)
        self.Display_Plate_Info.horizontalHeader().setStretchLastSection(True)
        self.Show_all_button_Plate_Info = QtWidgets.QPushButton(self.Plate_Scan_Tab)
        self.Show_all_button_Plate_Info.setGeometry(QtCore.QRect(20, 370, 180, 30))
        self.Show_all_button_Plate_Info.setMinimumSize(QtCore.QSize(150, 30))
        self.Show_all_button_Plate_Info.setObjectName("Show_all_button_Plate_Info")
        self.Plate_ID_label_Plate_Info = QtWidgets.QLabel(self.Plate_Scan_Tab)
        self.Plate_ID_label_Plate_Info.setGeometry(QtCore.QRect(50, 140, 61, 16))
        self.Plate_ID_label_Plate_Info.setMinimumSize(QtCore.QSize(61, 16))
        self.Plate_ID_label_Plate_Info.setObjectName("Plate_ID_label_Plate_Info")
        self.ID_search_button_Plate_Info = QtWidgets.QPushButton(self.Plate_Scan_Tab)
        self.ID_search_button_Plate_Info.setGeometry(QtCore.QRect(120, 60, 140, 30))
        self.ID_search_button_Plate_Info.setMinimumSize(QtCore.QSize(0, 0))
        self.ID_search_button_Plate_Info.setObjectName("ID_search_button_Plate_Info")
        self.Plate_ID_search_button_Plate_Info = QtWidgets.QPushButton(self.Plate_Scan_Tab)
        self.Plate_ID_search_button_Plate_Info.setGeometry(QtCore.QRect(120, 180, 140, 30))
        self.Plate_ID_search_button_Plate_Info.setMinimumSize(QtCore.QSize(140, 30))
        self.Plate_ID_search_button_Plate_Info.setObjectName("Plate_ID_search_button_Plate_Info")
        self.ID_label_Plate_Info = QtWidgets.QLabel(self.Plate_Scan_Tab)
        self.ID_label_Plate_Info.setGeometry(QtCore.QRect(50, 20, 61, 16))
        self.ID_label_Plate_Info.setMinimumSize(QtCore.QSize(61, 16))
        self.ID_label_Plate_Info.setObjectName("ID_label_Plate_Info")
        self.line_9 = QtWidgets.QFrame(self.Plate_Scan_Tab)
        self.line_9.setGeometry(QtCore.QRect(60, 220, 201, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.ID_input_Plate_Info = QtWidgets.QLineEdit(self.Plate_Scan_Tab)
        self.ID_input_Plate_Info.setGeometry(QtCore.QRect(120, 20, 141, 21))
        self.ID_input_Plate_Info.setMinimumSize(QtCore.QSize(141, 21))
        self.ID_input_Plate_Info.setText("")
        self.ID_input_Plate_Info.setObjectName("ID_input_Plate_Info")
        self.line_10 = QtWidgets.QFrame(self.Plate_Scan_Tab)
        self.line_10.setGeometry(QtCore.QRect(60, 100, 200, 20))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.Plate_ID_input_Plate_Info = QtWidgets.QLineEdit(self.Plate_Scan_Tab)
        self.Plate_ID_input_Plate_Info.setGeometry(QtCore.QRect(120, 140, 141, 21))
        self.Plate_ID_input_Plate_Info.setMinimumSize(QtCore.QSize(141, 21))
        self.Plate_ID_input_Plate_Info.setText("")
        self.Plate_ID_input_Plate_Info.setObjectName("Plate_ID_input_Plate_Info")
        self.Availability_button = QtWidgets.QPushButton(self.Plate_Scan_Tab)
        self.Availability_button.setGeometry(QtCore.QRect(110, 310, 151, 30))
        self.Availability_button.setMinimumSize(QtCore.QSize(140, 30))
        self.Availability_button.setObjectName("Availability_button")
        self.Available_FALSE = QtWidgets.QRadioButton(self.Plate_Scan_Tab)
        self.Available_FALSE.setGeometry(QtCore.QRect(110, 250, 100, 20))
        self.Available_FALSE.setMinimumSize(QtCore.QSize(100, 20))
        self.Available_FALSE.setObjectName("Available_FALSE")
        self.Available_TRUE = QtWidgets.QRadioButton(self.Plate_Scan_Tab)
        self.Available_TRUE.setGeometry(QtCore.QRect(110, 280, 100, 20))
        self.Available_TRUE.setMinimumSize(QtCore.QSize(100, 20))
        self.Available_TRUE.setObjectName("Available_TRUE")
        self.line_11 = QtWidgets.QFrame(self.Plate_Scan_Tab)
        self.line_11.setGeometry(QtCore.QRect(60, 340, 180, 30))
        self.line_11.setMinimumSize(QtCore.QSize(150, 30))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.Assign_plate_to_user = QtWidgets.QPushButton(self.Plate_Scan_Tab)
        self.Assign_plate_to_user.setGeometry(QtCore.QRect(20, 450, 180, 30))
        self.Assign_plate_to_user.setMinimumSize(QtCore.QSize(150, 30))
        self.Assign_plate_to_user.setObjectName("Assign_plate_to_user")
        self.Deassign_plate_from_user = QtWidgets.QPushButton(self.Plate_Scan_Tab)
        self.Deassign_plate_from_user.setGeometry(QtCore.QRect(20, 410, 180, 30))
        self.Deassign_plate_from_user.setMinimumSize(QtCore.QSize(150, 30))
        self.Deassign_plate_from_user.setObjectName("Deassign_plate_from_user")
        self.Add_new_plate = QtWidgets.QPushButton(self.Plate_Scan_Tab)
        self.Add_new_plate.setGeometry(QtCore.QRect(20, 490, 180, 30))
        self.Add_new_plate.setMinimumSize(QtCore.QSize(150, 30))
        self.Add_new_plate.setObjectName("Add_new_plate")
        self.Remove_plate = QtWidgets.QPushButton(self.Plate_Scan_Tab)
        self.Remove_plate.setGeometry(QtCore.QRect(20, 530, 180, 30))
        self.Remove_plate.setMinimumSize(QtCore.QSize(150, 30))
        self.Remove_plate.setObjectName("Remove_plate")
        self.Assign_fail_label = QtWidgets.QLabel(self.Plate_Scan_Tab)
        self.Assign_fail_label.setGeometry(QtCore.QRect(220, 450, 91, 31))
        self.Assign_fail_label.setMinimumSize(QtCore.QSize(61, 16))
        self.Assign_fail_label.setObjectName("Assign_fail_label")
        self.Assign_success_label = QtWidgets.QLabel(self.Plate_Scan_Tab)
        self.Assign_success_label.setGeometry(QtCore.QRect(220, 450, 91, 31))
        self.Assign_success_label.setMinimumSize(QtCore.QSize(61, 16))
        self.Assign_success_label.setObjectName("Assign_success_label")
        self.Plate_info_pages = QtWidgets.QSpinBox(self.Plate_Scan_Tab)
        self.Plate_info_pages.setGeometry(QtCore.QRect(700, 660, 81, 24))
        self.Plate_info_pages.setKeyboardTracking(False)
        self.Plate_info_pages.setObjectName("Plate_info_pages")
        self.ID_input_Plate_Info.raise_()
        self.Show_all_button_Plate_Info.raise_()
        self.Plate_ID_label_Plate_Info.raise_()
        self.ID_search_button_Plate_Info.raise_()
        self.Plate_ID_search_button_Plate_Info.raise_()
        self.ID_label_Plate_Info.raise_()
        self.line_9.raise_()
        self.line_10.raise_()
        self.Plate_ID_input_Plate_Info.raise_()
        self.Availability_button.raise_()
        self.Available_FALSE.raise_()
        self.Available_TRUE.raise_()
        self.line_11.raise_()
        self.Assign_plate_to_user.raise_()
        self.Deassign_plate_from_user.raise_()
        self.Add_new_plate.raise_()
        self.Remove_plate.raise_()
        self.Assign_fail_label.raise_()
        self.Assign_success_label.raise_()
        self.Plate_info_pages.raise_()
        self.Display_Plate_Info.raise_()
        Concentrate_Advance.addTab(self.Plate_Scan_Tab, "")

        self.retranslateUi(Concentrate_Advance)
        Concentrate_Advance.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Concentrate_Advance)

        self.modding()

    def retranslateUi(self, Concentrate_Advance):
        _translate = QtCore.QCoreApplication.translate
        Concentrate_Advance.setWindowTitle(_translate("Concentrate_Advance", "Concentrate_Advance"))
        self.Delete_User_button.setText(_translate("Concentrate_Advance", "Delete a User"))
        self.Gender_label.setText(_translate("Concentrate_Advance", "Gender"))
        self.Show_all_button.setText(_translate("Concentrate_Advance", "Show All Users"))
        self.Add_User_button.setText(_translate("Concentrate_Advance", "Add a User"))
        self.Name_label.setText(_translate("Concentrate_Advance", "Name"))
        self.Female_button.setText(_translate("Concentrate_Advance", "Female"))
        self.Permission_button.setText(_translate("Concentrate_Advance", "Search by Permission"))
        self.Name_search_button.setText(_translate("Concentrate_Advance", "Search by Name"))
        self.Others_button.setText(_translate("Concentrate_Advance", "Others"))
        self.ID_search_button.setText(_translate("Concentrate_Advance", "Search by ID"))
        self.Admin_button.setText(_translate("Concentrate_Advance", "Admin"))
        self.Edit_error_message.setText(_translate("Concentrate_Advance", "Invalid input!"))
        self.ID_label.setText(_translate("Concentrate_Advance", "ID"))
        self.Gender_button.setText(_translate("Concentrate_Advance", "Search by Gender"))
        self.Male_button.setText(_translate("Concentrate_Advance", "Male"))
        self.Permission_label.setText(_translate("Concentrate_Advance", "Permission"))
        self.User_button.setText(_translate("Concentrate_Advance", "User"))
        self.Save_change_button.setText(_translate("Concentrate_Advance", "Save change"))
        item = self.Display_table.horizontalHeaderItem(0)
        item.setText(_translate("Concentrate_Advance", "Checkbox"))
        item = self.Display_table.horizontalHeaderItem(1)
        item.setText(_translate("Concentrate_Advance", "ID"))
        item = self.Display_table.horizontalHeaderItem(2)
        item.setText(_translate("Concentrate_Advance", "Password"))
        item = self.Display_table.horizontalHeaderItem(3)
        item.setText(_translate("Concentrate_Advance", "Permission"))
        item = self.Display_table.horizontalHeaderItem(4)
        item.setText(_translate("Concentrate_Advance", "Name"))
        item = self.Display_table.horizontalHeaderItem(5)
        item.setText(_translate("Concentrate_Advance", "Gender"))
        item = self.Display_table.horizontalHeaderItem(6)
        item.setText(_translate("Concentrate_Advance", "Plate amount"))
        Concentrate_Advance.setTabText(Concentrate_Advance.indexOf(self.Search_Edit_Tab), _translate("Concentrate_Advance", "User info"))
        self.Password_doesnt_match_ID_button.setText(_translate("Concentrate_Advance", "Password doesn\'t match ID"))
        self.Success_button.setText(_translate("Concentrate_Advance", "Success"))
        self.ID_label_login_history.setText(_translate("Concentrate_Advance", "ID"))
        self.ID_doesnt_exist_button.setText(_translate("Concentrate_Advance", "ID doesn\'t exist"))
        self.ID_search_button_login_history.setText(_translate("Concentrate_Advance", "Search by ID"))
        item = self.Display_Login_info.horizontalHeaderItem(0)
        item.setText(_translate("Concentrate_Advance", "Record_number"))
        item = self.Display_Login_info.horizontalHeaderItem(1)
        item.setText(_translate("Concentrate_Advance", "Login_ID"))
        item = self.Display_Login_info.horizontalHeaderItem(2)
        item.setText(_translate("Concentrate_Advance", "Login_Time"))
        item = self.Display_Login_info.horizontalHeaderItem(3)
        item.setText(_translate("Concentrate_Advance", "Login_Status"))
        item = self.Display_Login_info.horizontalHeaderItem(4)
        item.setText(_translate("Concentrate_Advance", "Fail_Type"))
        self.Fail_button.setText(_translate("Concentrate_Advance", "Fail "))
        self.Fail_type_button.setText(_translate("Concentrate_Advance", "Show by Fail type"))
        self.Status_show_button.setText(_translate("Concentrate_Advance", "Show by Status"))
        self.Show_all_button_login_history.setText(_translate("Concentrate_Advance", "Show All"))
        self.User_enter_advance_button.setText(_translate("Concentrate_Advance", "Normal user entered Advance mode"))
        self.Success_type_button.setText(_translate("Concentrate_Advance", "Show by Success type"))
        self.Normal_login_button.setText(_translate("Concentrate_Advance", "Normal login"))
        self.Advance_login_button.setText(_translate("Concentrate_Advance", "Advance login"))
        Concentrate_Advance.setTabText(Concentrate_Advance.indexOf(self.Login_History_Tab), _translate("Concentrate_Advance", "Login History"))
        item = self.Display_Plate_Info.horizontalHeaderItem(0)
        item.setText(_translate("Concentrate_Advance", "Checkbox"))
        item = self.Display_Plate_Info.horizontalHeaderItem(1)
        item.setText(_translate("Concentrate_Advance", "Plate_ID"))
        item = self.Display_Plate_Info.horizontalHeaderItem(2)
        item.setText(_translate("Concentrate_Advance", "Last_Assigned_User_ID"))
        item = self.Display_Plate_Info.horizontalHeaderItem(3)
        item.setText(_translate("Concentrate_Advance", "Avaliable_for_assign"))
        item = self.Display_Plate_Info.horizontalHeaderItem(4)
        item.setText(_translate("Concentrate_Advance", "Last_Assign_Time"))
        item = self.Display_Plate_Info.horizontalHeaderItem(5)
        item.setText(_translate("Concentrate_Advance", "Last_Deassign_Time"))
        self.Show_all_button_Plate_Info.setText(_translate("Concentrate_Advance", "Show All"))
        self.Plate_ID_label_Plate_Info.setText(_translate("Concentrate_Advance", "Plate ID"))
        self.ID_search_button_Plate_Info.setText(_translate("Concentrate_Advance", "Search by ID"))
        self.Plate_ID_search_button_Plate_Info.setText(_translate("Concentrate_Advance", "Search by Plate ID"))
        self.ID_label_Plate_Info.setText(_translate("Concentrate_Advance", "ID"))
        self.Availability_button.setText(_translate("Concentrate_Advance", "Show by Availability"))
        self.Available_FALSE.setText(_translate("Concentrate_Advance", "FALSE"))
        self.Available_TRUE.setText(_translate("Concentrate_Advance", "TRUE"))
        self.Assign_plate_to_user.setText(_translate("Concentrate_Advance", "Assign plate to user"))
        self.Deassign_plate_from_user.setText(_translate("Concentrate_Advance", "Deassign plate"))
        self.Add_new_plate.setText(_translate("Concentrate_Advance", "Add new plate"))
        self.Remove_plate.setText(_translate("Concentrate_Advance", "Remove plate"))
        self.Assign_fail_label.setText(_translate("Concentrate_Advance", "Failed!"))
        self.Assign_success_label.setText(_translate("Concentrate_Advance", "Success"))
        Concentrate_Advance.setTabText(Concentrate_Advance.indexOf(self.Plate_Scan_Tab), _translate("Concentrate_Advance", "Plate Scan"))

    def modding(self):
        # Modding for Search/Edit

        # adjust column size
        header = self.Display_table.horizontalHeader()
        for i in range(5):
            header.setSectionResizeMode(
                i, QtWidgets.QHeaderView.ResizeToContents)

        # hide the error message
        self.Edit_error_message.setHidden(True)

        # connect button to function
        self.Show_all_button.clicked.connect(
            lambda: helper.set_current_search_type(Search_Edit_function, "all"))
        self.Show_all_button.clicked.connect(
            lambda: Search_Edit_function.show_user(0))
        self.ID_search_button.clicked.connect(
            lambda: helper.set_current_search_type(Search_Edit_function, "id"))
        self.ID_search_button.clicked.connect(
            lambda: Search_Edit_function.show_user(0))
        self.Name_search_button.clicked.connect(
            lambda: helper.set_current_search_type(Search_Edit_function, "name"))
        self.Name_search_button.clicked.connect(
            lambda: Search_Edit_function.show_user(0))
        self.Gender_button.clicked.connect(
            lambda: helper.set_current_search_type(Search_Edit_function, "gender"))
        self.Gender_button.clicked.connect(
            lambda: Search_Edit_function.show_user(0))
        self.Permission_button.clicked.connect(
            lambda: helper.set_current_search_type(Search_Edit_function, "permission"))
        self.Permission_button.clicked.connect(
            lambda: Search_Edit_function.show_user(0))
        self.Save_change_button.clicked.connect(
            lambda: Search_Edit_function.press_save())
        self.Delete_User_button.clicked.connect(
            lambda: Search_Edit_function.show_delete_confirm())
        self.Add_User_button.clicked.connect(
            lambda: Search_Edit_function.open_Register_window())

        self.User_info_pages.valueChanged.connect(
            lambda: Search_Edit_function.show_user(self.User_info_pages.value()))

        # get the maximum page number
        Search_Edit_function.user_info_pages_maximum = MySQL_func.get_pages_maximum(
            Search_Edit_function, None, user_info_table)

        # set the maximum number for spinbox
        self.User_info_pages.setMaximum(2147483647)

        # show all info initially
        Search_Edit_function.show_user(0)

    # Modding for Login History
        # adjust column size
        header = self.Display_Login_info.horizontalHeader()
        for i in range(3):
            header.setSectionResizeMode(
                i, QtWidgets.QHeaderView.ResizeToContents)

        # connect button to function
        self.Show_all_button_login_history.clicked.connect(
            lambda: helper.set_current_search_type(Login_History_function, "all"))
        self.Show_all_button_login_history.clicked.connect(
            lambda: Login_History_function.show_login_history(0))
        self.ID_search_button_login_history.clicked.connect(
            lambda: helper.set_current_search_type(Login_History_function, "id"))
        self.ID_search_button_login_history.clicked.connect(
            lambda: Login_History_function.show_login_history(0))
        self.Status_show_button.clicked.connect(
            lambda: helper.set_current_search_type(Login_History_function, "status"))
        self.Status_show_button.clicked.connect(
            lambda: Login_History_function.show_login_history(0))
        self.Fail_type_button.clicked.connect(
            lambda: helper.set_current_search_type(Login_History_function, "specific_type_fail"))
        self.Fail_type_button.clicked.connect(
            lambda: Login_History_function.show_login_history(0))
        self.Success_type_button.clicked.connect(
            lambda: helper.set_current_search_type(Login_History_function, "specific_type_success"))
        self.Success_type_button.clicked.connect(
            lambda: Login_History_function.show_login_history(0))

        self.Login_History_Pages.valueChanged.connect(
            lambda: Login_History_function.show_login_history(self.Login_History_Pages.value()))

        # get the maximum page number
        Login_History_function.login_history_pages_maximum = MySQL_func.get_pages_maximum(
            Login_History_function, None, login_record_table)

        # set the maximum number for spinbox
        self.Login_History_Pages.setMaximum(2147483647)

        # show all info initially
        Login_History_function.show_login_history(0)

        # let table be read only
        self.Display_Login_info.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)


    # Modding for plate info
        # adjust column size
        header = self.Display_Plate_Info.horizontalHeader()
        for i in range(5):
            header.setSectionResizeMode(
                i, QtWidgets.QHeaderView.ResizeToContents)

        # connect button to function

        self.Show_all_button_Plate_Info.clicked.connect(
            lambda: helper.set_current_search_type(Plate_Info_function, "all"))
        self.Show_all_button_Plate_Info.clicked.connect(
            lambda: Plate_Info_function.show_plate_info(0))
        self.ID_search_button_Plate_Info.clicked.connect(
            lambda: helper.set_current_search_type(Plate_Info_function, "user_id"))
        self.ID_search_button_Plate_Info.clicked.connect(
            lambda: Plate_Info_function.show_plate_info(0))
        self.Plate_ID_search_button_Plate_Info.clicked.connect(
            lambda: helper.set_current_search_type(Plate_Info_function, "plate_id"))
        self.Plate_ID_search_button_Plate_Info.clicked.connect(
            lambda: Plate_Info_function.show_plate_info(0))
        self.Availability_button.clicked.connect(
            lambda: helper.set_current_search_type(Plate_Info_function, "availability"))
        self.Availability_button.clicked.connect(
            lambda: Plate_Info_function.show_plate_info(0))

        self.Add_new_plate.clicked.connect(
            lambda: Plate_Info_function.show_add_new_plate_window())
        self.Assign_plate_to_user.clicked.connect(
            lambda: Plate_Info_function.show_assign_plate_to_user_window())
        self.Deassign_plate_from_user.clicked.connect(
            lambda: Plate_Info_function.show_deassign_plate_to_user_window())
        self.Remove_plate.clicked.connect(
            lambda: Plate_Info_function.show_delete_plate_confirm())

        self.Plate_info_pages.valueChanged.connect(
            lambda: Plate_Info_function.show_plate_info(self.Plate_info_pages.value()))

        # let table be read only
        self.Display_Plate_Info.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)

        # hide the message
        self.Assign_fail_label.setHidden(True)
        self.Assign_success_label.setHidden(True)

        # set the maximum number for spinbox
        self.Plate_info_pages.setMaximum(2147483647)

        # show all info initially
        Plate_Info_function.show_plate_info(0)

        # get the maximum page number
        Plate_Info_function.plate_info_pages_maximum = MySQL_func.get_pages_maximum(
            Plate_Info_function, None, plate_info_table)

class Ui_Register(object):
    # global variable
    default_password = "Point1"
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(312, 402)
        self.ID_input = QtWidgets.QLineEdit(Register)
        self.ID_input.setGeometry(QtCore.QRect(112, 20, 141, 21))
        self.ID_input.setText("")
        self.ID_input.setObjectName("ID_input")
        self.Add_a_user_button = QtWidgets.QPushButton(Register)
        self.Add_a_user_button.setGeometry(QtCore.QRect(100, 320, 113, 32))
        self.Add_a_user_button.setObjectName("Add_a_user_button")
        self.Name_input = QtWidgets.QLineEdit(Register)
        self.Name_input.setGeometry(QtCore.QRect(112, 100, 141, 21))
        self.Name_input.setText("")
        self.Name_input.setObjectName("Name_input")
        self.Gender_label = QtWidgets.QLabel(Register)
        self.Gender_label.setGeometry(QtCore.QRect(30, 150, 81, 16))
        self.Gender_label.setObjectName("Gender_label")
        self.Name_label = QtWidgets.QLabel(Register)
        self.Name_label.setGeometry(QtCore.QRect(30, 100, 81, 16))
        self.Name_label.setObjectName("Name_label")
        self.ID_label = QtWidgets.QLabel(Register)
        self.ID_label.setGeometry(QtCore.QRect(30, 20, 81, 16))
        self.ID_label.setObjectName("ID_label")
        self.Male_button = QtWidgets.QRadioButton(Register)
        self.Male_button.setGeometry(QtCore.QRect(110, 150, 100, 20))
        self.Male_button.setObjectName("Male_button")
        self.Button_group_gender = QtWidgets.QButtonGroup(Register)
        self.Button_group_gender.setObjectName("Button_group_gender")
        self.Button_group_gender.addButton(self.Male_button)
        self.Female_button = QtWidgets.QRadioButton(Register)
        self.Female_button.setGeometry(QtCore.QRect(110, 180, 100, 20))
        self.Female_button.setObjectName("Female_button")
        self.Button_group_gender.addButton(self.Female_button)
        self.Permission_label = QtWidgets.QLabel(Register)
        self.Permission_label.setGeometry(QtCore.QRect(30, 250, 81, 16))
        self.Permission_label.setObjectName("Permission_label")
        self.Admin_button = QtWidgets.QRadioButton(Register)
        self.Admin_button.setGeometry(QtCore.QRect(110, 250, 100, 20))
        self.Admin_button.setObjectName("Admin_button")
        self.Button_group_permission = QtWidgets.QButtonGroup(Register)
        self.Button_group_permission.setObjectName("Button_group_permission")
        self.Button_group_permission.addButton(self.Admin_button)
        self.Normal_button = QtWidgets.QRadioButton(Register)
        self.Normal_button.setGeometry(QtCore.QRect(110, 280, 100, 20))
        self.Normal_button.setObjectName("Normal_button")
        self.Button_group_permission.addButton(self.Normal_button)
        self.ID_error_message = QtWidgets.QLabel(Register)
        self.ID_error_message.setGeometry(QtCore.QRect(150, 50, 101, 16))
        self.ID_error_message.setObjectName("ID_error_message")
        self.Register_error_message = QtWidgets.QLabel(Register)
        self.Register_error_message.setGeometry(QtCore.QRect(120, 360, 80, 20))
        self.Register_error_message.setObjectName("Register_error_message")
        self.Register_success_message = QtWidgets.QLabel(Register)
        self.Register_success_message.setGeometry(
            QtCore.QRect(70, 360, 211, 20))
        self.Register_success_message.setObjectName("Register_success_message")
        self.Other_button = QtWidgets.QRadioButton(Register)
        self.Other_button.setGeometry(QtCore.QRect(110, 210, 100, 20))
        self.Other_button.setObjectName("Other_button")
        self.line = QtWidgets.QFrame(Register)
        self.line.setGeometry(QtCore.QRect(30, 70, 251, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Register)
        self.line_2.setGeometry(QtCore.QRect(30, 130, 251, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Register)
        self.line_3.setGeometry(QtCore.QRect(30, 230, 251, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Register)
        self.line_4.setGeometry(QtCore.QRect(30, 300, 251, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Register"))
        self.Add_a_user_button.setText(_translate("Register", "Add a user"))
        self.Gender_label.setText(_translate("Register", "Gender"))
        self.Name_label.setText(_translate("Register", "Name"))
        self.ID_label.setText(_translate("Register", "ID"))
        self.Male_button.setText(_translate("Register", "Male"))
        self.Female_button.setText(_translate("Register", "Female"))
        self.Permission_label.setText(_translate("Register", "Permission"))
        self.Admin_button.setText(_translate("Register", "Admin"))
        self.Normal_button.setText(_translate("Register", "Normal"))
        self.ID_error_message.setText(_translate("Register", "Invalid ID!"))
        self.Register_error_message.setText(
            _translate("Register", "Action failed!"))
        self.Register_success_message.setText(
            _translate("Register", "Successfully added the user!"))
        self.Other_button.setText(_translate("Register", "Others"))

        self.modding()

    def modding(self):
        # connect button to function
        self.Add_a_user_button.clicked.connect(lambda: Register_function.press_register(
            self.ID_input.text(), self.default_password, self.Name_input.text()))

        # hide the error message initially
        self.ID_error_message.setHidden(True)
        self.Register_error_message.setHidden(True)
        self.Register_success_message.setHidden(True)


# Function classƒ√
class UI_Login_function:
    def open_Concentrate_Advance_window(self):
        self.Concentrate_Advance = QtWidgets.QTabWidget()
        self.Concentrate_Advance_ui = Ui_Concentrate_Advance()
        self.Concentrate_Advance_ui.current_user = user(Loginui.UserID_Input.text())
        self.Concentrate_Advance_ui.setupUi(self.Concentrate_Advance)
        self.Concentrate_Advance.show()

    def open_Info_Editor_window(self):
        self.Info_Editor = QtWidgets.QWidget()
        self.Info_Editor_ui = Ui_Info_Editor()
        self.Info_Editor_ui.current_user = user(Loginui.UserID_Input.text())
        self.Info_Editor_ui.setupUi(self.Info_Editor)
        self.Info_Editor.show()

    def open_normal_welcome_message(self):
        confirm = QMessageBox()
        confirm.setWindowTitle("Welcome window")
        confirm.setText(
            "Welcome! " + Loginui.UserID_Input.text() + "! Display edit window?")
        confirm.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        confirm.setDefaultButton(QMessageBox.Cancel)
        confirm.accepted.connect(lambda: self.open_Info_Editor_window())
        confirm.accepted.connect(
            lambda: Info_Editor_function.show_user(0))
        x = confirm.exec_()

    def login(self, userid, password):
        MySQL_func.check_if_user_info_is_empty()
        # initialize
        current_user = user(userid)

        ID_password_match = (helper.encode_password(password) == current_user.password)
        ID_is_admin = (current_user.permission == "ADMIN")
        ID_exist = (current_user.GetUserInfo != -1)

        if (ID_password_match is True):
            # enter Advance mode
            if (ID_is_admin is True and Loginui.checkBox.isChecked()):
                MySQL_func.add_login_record(
                    current_user.userid, "SUCCESS", "Login with Advance mode")
                self.open_Concentrate_Advance_window()
                Login.close()
                return True
            # Fail: Not admin but try to entering advance mode
            elif (ID_is_admin is False and Loginui.checkBox.isChecked()):
                MySQL_func.add_login_record(
                    current_user.userid, "FAIL", "A normal user tries to enter Advance mode")
                Loginui.Error_Message_for_permission.setHidden(False)
                Loginui.Error_Message_for_password.setHidden(True)
                Loginui.Error_Message_for_ID.setHidden(True)
                return False
            # enter Normal user mode
            else:
                self.open_normal_welcome_message()
                Login.close()
                MySQL_func.add_login_record(
                    current_user.userid, "SUCCESS", "Login with normal user mode")
                return True
        # Fail: ID doesn't exist
        elif (ID_exist is False):
            MySQL_func.add_login_record(
                current_user.userid, "FAIL", "ID doesn't exist")
            # display the error message
            Loginui.Error_Message_for_permission.setHidden(True)
            Loginui.Error_Message_for_password.setHidden(True)
            Loginui.Error_Message_for_ID.setHidden(False)
            return False
        # Fail: ID doesn't match password
        elif (ID_password_match is False):
            MySQL_func.add_login_record(
                current_user.userid, "FAIL", "ID and Password doesn't match")
            # display the error message
            Loginui.Error_Message_for_password.setHidden(False)
            Loginui.Error_Message_for_permission.setHidden(True)
            Loginui.Error_Message_for_ID.setHidden(True)
            return False

class UI_Info_Editor_function:
    initial_data = []
    edited_data = []
    check_button_array = []
    current_user = user(None)

    def show_user(self, pages):
        self.current_user = Login_function.Info_Editor_ui.current_user
        self.table = Login_function.Info_Editor_ui.Display_table
        data = MySQL_func.get_data_from_database("User_Information",
                                                    "id_strict", self.current_user.userid, pages)
        helper.insert_data_into_table(
            self.table, data, self)
        
        for i in range(self.table.rowCount()):
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(None))
            self.table.setItem(i, 2, QtWidgets.QTableWidgetItem("************"))   
                 
        helper.insert_checkbox(
            self, self.table, data)
                         
        helper.lock_the_Column(
            self.table, 1)
        helper.lock_the_Column(
            self.table, 3)
        helper.lock_the_Column(
            self.table, 6)                

    def press_save(self):
        fit_list = MySQL_func.get_data_from_table(self.table, self)
        Login_function.Info_Editor_ui.Permission_Invalid.setHidden(fit_list[0])
        Login_function.Info_Editor_ui.Gender_Invalid.setHidden(fit_list[1])
        Login_function.Info_Editor_ui.Password_Invalid.setHidden(fit_list[2])        

class UI_Search_Edit_function:
    initial_data = []
    edited_data = []
    user_info_pages_maximum = 0
    current_search_type = "all"
    check_button_array = []
    current_user = user(None)      
    # Function for Search/Edit
    def show_user(self, pages):
        self.current_user = Login_function.Concentrate_Advance_ui.current_user
        self.table = Login_function.Concentrate_Advance_ui.Display_table       

        if (self.current_search_type == "id"):
            if (Login_function.Concentrate_Advance_ui.ID_input.text() == None):
                value = ""
            value = Login_function.Concentrate_Advance_ui.ID_input.text()
        elif (self.current_search_type == "name"):
            if (Login_function.Concentrate_Advance_ui.Name_input.text() == None):
                value = ""
            value = Login_function.Concentrate_Advance_ui.Name_input.text()
        elif (self.current_search_type == "all"):
            value = None
        elif (self.current_search_type == "permission"):
            if (Login_function.Concentrate_Advance_ui.User_button.isChecked()):
                value = "USER"
            elif (Login_function.Concentrate_Advance_ui.Admin_button.isChecked()):
                value = "ADMIN"
            else:
                value = ""
        elif (self.current_search_type == "gender"):
            if (Login_function.Concentrate_Advance_ui.Male_button.isChecked()):
                value = "MALE"
            elif (Login_function.Concentrate_Advance_ui.Female_button.isChecked()):
                value = "FEMALE"
            elif (Login_function.Concentrate_Advance_ui.Others_button.isChecked()):
                value = "OTHERS"
            else:
                value = ""

        self.user_info_pages_maximum = MySQL_func.get_pages_maximum(
            Search_Edit_function, value, user_info_table)
        if (self.user_info_pages_maximum <= pages):
            Login_function.Concentrate_Advance_ui.User_info_pages.setValue(
                self.user_info_pages_maximum)
            pages = self.user_info_pages_maximum

        data = MySQL_func.get_data_from_database("User_Information",
                                                    self.current_search_type, value, pages)
        helper.insert_data_into_table(
            self.table, data, self)
        # remove text in checkbox column 
        for i in range(self.table.rowCount()):
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(None))
            self.table.setItem(i, 2, QtWidgets.QTableWidgetItem("************"))

        helper.insert_checkbox(
            self, self.table, data)
        # lock the column
        helper.lock_the_Column(
            self.table, 1)
        helper.lock_the_Column(
            self.table, 6)        

    def press_save(self):
        fit_list = MySQL_func.get_data_from_table(self.table, self)
        Login_function.Concentrate_Advance_ui.Edit_error_message.setHidden(fit_list[0] and fit_list[1] and fit_list[2])
   
    def open_Register_window(self):
        self.Register = QtWidgets.QWidget()
        self.Register_ui = Ui_Register()
        self.Register_ui.setupUi(self.Register)
        self.Register.show()

    def show_delete_confirm(self):
        confirm = QMessageBox()
        confirm.setWindowTitle("Delete Confirm")
        confirm.setText(
            "Remove users will automatically deassign plates that had been assigned to these users.\nStill want to remove users?")
        confirm.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        confirm.setDefaultButton(QMessageBox.Cancel)
        confirm.accepted.connect(lambda: self.delete_users())
        x = confirm.exec_()

    def delete_users(self):
        # go through entire table row by row
        for row in range(self.table.rowCount()):
            data = []
            for column in range(self.table.columnCount()):
                if (self.table.item(row, column) != None):
                    data.append(self.table.item(
                        row, column).text())
            if (self.check_button_array[row].isChecked()):
                plate_list = user(data[1]).get_plate_id_user_have()
                for plate in plate_list:
                    MySQL_func.deassign_assign_plate_to_user(0, plate[0], None)
                MySQL_func.remove_user(data[1])
        helper.set_current_search_type(Search_Edit_function, "all")
        Search_Edit_function.show_user(0)
        Plate_Info_function.show_plate_info(0)


class UI_Register_function:
    def press_register(self, userid, password, real_name):
        return_flag = False
        gender_flag = False
        admin_flag = False
        name_flag = False
        # handle invalid input
        if (MySQL_func.check_ID_action(2, userid, None, user_info_table) is True or userid == "" or len(userid) < 4 or (helper.has_invalid_character(userid))):
            Search_Edit_function.Register_ui.ID_error_message.setHidden(
                False)
            return_flag = True
        else:
            Search_Edit_function.Register_ui.ID_error_message.setHidden(
                True)

        if (Search_Edit_function.Register_ui.Male_button.isChecked() or Search_Edit_function.Register_ui.Female_button.isChecked() or Search_Edit_function.Register_ui.Other_button.isChecked()):
            gender_flag = True
        if (Search_Edit_function.Register_ui.Admin_button.isChecked() or Search_Edit_function.Register_ui.Normal_button.isChecked()):
            admin_flag = True
        if (real_name == ""):
            name_flag = True

        if (return_flag is True or name_flag is True or gender_flag is False or admin_flag is False):
            Search_Edit_function.Register_ui.Register_error_message.setHidden(
                False)
            Search_Edit_function.Register_ui.Register_success_message.setHidden(
                True)
            return False

        # transfer radio button information to string
        if (Search_Edit_function.Register_ui.Male_button.isChecked()):
            gender = "MALE"
        elif (Search_Edit_function.Register_ui.Female_button.isChecked()):
            gender = "FEMALE"
        elif (Search_Edit_function.Register_ui.Other_button.isChecked()):
            gender = "OTHERS"
        if (Search_Edit_function.Register_ui.Admin_button.isChecked()):
            permission = "ADMIN"
        elif (Search_Edit_function.Register_ui.Normal_button.isChecked()):
            permission = "USER"

        # add the user
        MySQL_func.add_user(userid, helper.encode_password(
            password), permission, real_name, gender)
        helper.set_current_search_type(Search_Edit_function, "all")
        Search_Edit_function.show_user(0)
        Search_Edit_function.Register_ui.Register_error_message.setHidden(
            True)
        Search_Edit_function.Register_ui.Register_success_message.setHidden(
            False)
        return True

class UI_Login_History_function:
    login_history_pages_maximum = 0
    current_search_type = "all"
    # Function for Login History
    def show_login_history(self, pages):
        if (self.current_search_type == "id"):
            if (Login_function.Concentrate_Advance_ui.ID_input_login_history.text() == None):
                value = ""
            value = Login_function.Concentrate_Advance_ui.ID_input_login_history.text()
        elif (self.current_search_type == "all"):
            value = None
        elif (self.current_search_type == "status"):
            if (Login_function.Concentrate_Advance_ui.Success_button.isChecked()):
                value = "SUCCESS"
            elif (Login_function.Concentrate_Advance_ui.Fail_button.isChecked()):
                value = "FAIL"
            else:
                value = ""
        elif (self.current_search_type == "specific_type_fail"):
            if (Login_function.Concentrate_Advance_ui.ID_doesnt_exist_button.isChecked()):
                value = "ID doesn't exist"
            elif (Login_function.Concentrate_Advance_ui.Password_doesnt_match_ID_button.isChecked()):
                value = "ID and Password doesn't match"
            elif (Login_function.Concentrate_Advance_ui.User_enter_advance_button.isChecked()):
                value = "A normal user tries to enter Advance mode"
            else:
                value = ""
        elif (self.current_search_type == "specific_type_success"):
            if (Login_function.Concentrate_Advance_ui.Normal_login_button.isChecked()):
                value = "Login with normal user mode"
            elif (Login_function.Concentrate_Advance_ui.Advance_login_button.isChecked()):
                value = "Login with Advance mode"
            else:
                value = ""

        self.login_history_pages_maximum = MySQL_func.get_pages_maximum(
            self, value, login_record_table)
        if (self.login_history_pages_maximum <= pages):
            Login_function.Concentrate_Advance_ui.Login_History_Pages.setValue(
                self.login_history_pages_maximum)
            pages = self.login_history_pages_maximum
        data = MySQL_func.get_data_from_database("Login_record",
                                                    self.current_search_type, value, pages)
        helper.insert_data_into_table(
            Login_function.Concentrate_Advance_ui.Display_Login_info, data, self)

class UI_Plate_info_function:
    plate_info_pages_maximum = 0
    current_search_type = "all"
    check_button_array = []
    current_user = user(None)      

    # Function for Plate Scan
    def show_plate_info(self, pages):
        self.current_user = Login_function.Concentrate_Advance_ui.current_user
        self.table = Login_function.Concentrate_Advance_ui.Display_Plate_Info       
        if (self.current_search_type == "all"):
            value = None
        elif (self.current_search_type == "user_id"):
            if (Login_function.Concentrate_Advance_ui.ID_input_Plate_Info.text() == None):
                value = ""
            value = Login_function.Concentrate_Advance_ui.ID_input_Plate_Info.text()
        elif (self.current_search_type == "plate_id"):
            if (Login_function.Concentrate_Advance_ui.Plate_ID_input_Plate_Info.text() == None):
                value = ""
            value = Login_function.Concentrate_Advance_ui.Plate_ID_input_Plate_Info.text()
        elif (self.current_search_type == "availability"):
            if (Login_function.Concentrate_Advance_ui.Available_FALSE.isChecked()):
                value = "FALSE"
            elif (Login_function.Concentrate_Advance_ui.Available_TRUE.isChecked()):
                value = "TRUE"
            else:
                value = ""

        self.plate_info_pages_maximum = MySQL_func.get_pages_maximum(
            self, value, plate_info_table)
        if (self.plate_info_pages_maximum <= pages):
            Login_function.Concentrate_Advance_ui.Plate_info_pages.setValue(
                self.plate_info_pages_maximum)
            pages = self.plate_info_pages_maximum

        data = MySQL_func.get_data_from_database("Plate_Information",
                                                    self.current_search_type, value, pages)
        helper.insert_data_into_table(
            self.table, data, self)
        for i in range(self.table.rowCount()):
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(None))
        helper.insert_checkbox(
            self, self.table, data)

    def show_add_new_plate_window(self):
        plateid, read_next_plate = QtWidgets.QInputDialog().getText(
            Login_function.Concentrate_Advance_ui.Plate_Scan_Tab, '', 'Please scan the bar code on the plate.')
        if (read_next_plate is True and plateid != ''):
            MySQL_func.add_new_plate(plateid)
            self.show_plate_info(0)
            self.show_add_new_plate_window()

    def show_delete_plate_confirm(self):
        confirm = QMessageBox()
        confirm.setWindowTitle("Remove confirm")
        confirm.setText("Remove these plates from database?")
        confirm.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        confirm.setDefaultButton(QMessageBox.Cancel)
        confirm.accepted.connect(lambda: self.plate_action(1, None))
        x = confirm.exec_()

    # mode 0 for deassign
    # mdoe 1 for remove
    # mode 2 for assign
    def plate_action(self, mode, userid):
        for row in range(self.table.rowCount()):
            data = []
            for column in range(self.table.columnCount()):
                data.append(self.table.item(row, column).text())
            if (self.check_button_array[row].isChecked()):
                if (mode == 0):
                    if (data[3] == "FALSE"):
                        MySQL_func.deassign_assign_plate_to_user(0, data[1], None)
                elif (mode == 1):
                    MySQL_func.remove_plate(data[1])
                elif (mode == 2):
                    if (MySQL_func.check_ID_action(2, userid, None,  user_info_table) is True):
                        MySQL_func.deassign_assign_plate_to_user(1, data[1], userid)
                        Login_function.Concentrate_Advance_ui.Assign_success_label.setHidden(
                            False)
                        Login_function.Concentrate_Advance_ui.Assign_fail_label.setHidden(
                            True)
                    else:
                        Login_function.Concentrate_Advance_ui.Assign_success_label.setHidden(
                            True)
                        Login_function.Concentrate_Advance_ui.Assign_fail_label.setHidden(
                            False)
                MySQL_func.update_plate_user_have(data[2])
        self.show_plate_info(0)
        Search_Edit_function.show_user(0)

    def show_assign_plate_to_user_window(self):
        # create a dialog widgets
        userid, ok = QtWidgets.QInputDialog().getText(Login_function.Concentrate_Advance_ui.Plate_Scan_Tab,
                                                        '', 'Please enter the user id that you like to assign to.')
        if (ok):
            self.plate_action(2, userid)

    def show_deassign_plate_to_user_window(self):
        confirm = QMessageBox()
        confirm.setWindowTitle("Deassign confirm")
        confirm.setText("Deassign these plates from Users?")
        confirm.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        confirm.setDefaultButton(QMessageBox.Cancel)
        confirm.accepted.connect(lambda: self.plate_action(0, None))
        x = confirm.exec_()



# main
if __name__ == "__main__":
    Login_function = UI_Login_function()
    Info_Editor_function = UI_Info_Editor_function()
    Search_Edit_function = UI_Search_Edit_function()
    Register_function = UI_Register_function()
    Login_History_function = UI_Login_History_function()
    Plate_Info_function = UI_Plate_info_function()
    MySQL_func = MySQL_function_class("localhost", "root", "password", "UI_database")
    helper = helper_function_class()

    # table in database's name
    user_info_table = "User_Information"
    login_record_table = "Login_record"
    plate_info_table = "Plate_Information"

    # logger
    ErrorLogger = logger_class(
        "Error_Logger", logging.ERROR, "Log_Folder/Error.log")
    AdminEditorLogger = logger_class(
        "Admin_Editor_logger", logging.INFO, "Log_Folder/Admin_editor.log")
    PlateInfoLogger = logger_class(
        "Plate_Infor_logger", logging.INFO, "Log_Folder/Plate_Info.log")

    # open login UI
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    Loginui = Ui_Login()
    Loginui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
