from PyQt5 import QtCore, QtWidgets
import datetime
import hashlib
import re

class helper_function_class:

    # helper function
    def encode_password(self, password):
        hash_md5 = hashlib.md5()
        hash_md5.update(password.encode("utf-8"))
        return hash_md5.hexdigest()

    def get_time(self):
        return datetime.datetime.now()

    def lock_the_Column(self, display_table, lock_column):
        rows = display_table.rowCount()
        for i in range(rows):
            item = display_table.item(i, lock_column)
            item.setFlags(QtCore.Qt.ItemIsEnabled)

    def has_capital_letters(self, password):

        for letters in password:
            # checking for uppercase character and flagging
            if letters.isupper():
                return True
        return False

    def has_lower_letters(self, password):
        for letters in password:
            # checking for uppercase character and flagging
            if letters.islower():
                return True
        return False

    def has_numbers(self, password):
        return any(letters.isdigit() for letters in password)

    def has_invalid_character(self, password):
            # Make own character set and pass
            # this as argument in compile method
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            # Pass the string in search
            # method of regex object.
            if (re.search("[^a-zA-Z0-9s]", password) or (' ' in password) is True):
                return True
            else:
                return False

    def check_password_availability(self, password):
        if (len(password) >= 6 and self.has_capital_letters(password) is True and self.has_numbers(password) and self.has_lower_letters(password) is True and (self.has_invalid_character(password) is False)):
            return True
        return False

    def insert_data_into_table(self, display_table, data, function_class):
        display_table.setRowCount(0)
        row_count = 0
        function_class.check_button_array = []
        function_class.initial_data = []
        for row in data:
            initial_row = []            
            display_table.insertRow(row_count)
            for column in range(display_table.columnCount()):
                display_table.setItem(row_count, column, QtWidgets.QTableWidgetItem(str(row[column])))
                initial_row.append(row[column])
            function_class.initial_data.append(initial_row)
            # print(data_list)
            row_count = row_count + 1

    def insert_checkbox(self, function_class, display_table, data):
        for check_box_row in range(len(data)):
            # set a button to table
            check_box = QtWidgets.QCheckBox()
            display_table.setCellWidget(
                check_box_row, 0, check_box)
            function_class.check_button_array.append(check_box)

    def set_current_search_type(self, function_class, type):
        function_class.current_search_type = type

    def get_userid_on_table_list(self, display_table):
        userid_on_table_list = []
        for row in range(display_table.rowCount()):
            userid_on_table_list.append(display_table.item(row, 1).text())  
        return userid_on_table_list
    
    def get_current_edited_row(self, display_table, row):
        current_edited_row = []
        for column in range(display_table.columnCount()):
            if(display_table.item(row, column) == None):
                current_edited_row.append("")
            else:
                current_edited_row.append(display_table.item(row, column).text())
        return current_edited_row

    def compare_row_with_user(self, row , user, logger_class, current_user):
        if(row[2] != "************"):
                logger_class.logger.info(
                    current_user.userid + " has edited " + "USER ID: '" + user.userid + "'s password.")        
        if(row[3] != user.permission):
                logger_class.logger.info(
                    current_user.userid + " has edited " + "USER ID: '" + user.userid + "'s permission from '" + user.permission + "' to '" + row[3] + "'.")
        if(row[4] != user.name):
                logger_class.logger.info(
                    current_user.userid + " has edited " + "USER ID: '" + user.userid + "'s name from '" + user.name + "' to '" + row[4] + "'.")                       
        if(row[5] != user.gender):
                logger_class.logger.info(
                    current_user.userid + " has edited " + "USER ID: '" + user.userid + "'s gender from '" + user.gender + "' to '" + row[5] + "'.")

    def check_if_table_has_valid_data_only(self, display_table, function_class):
        fit_list = []
        Permission_fit = True
        Gender_fit = True
        Password_fit = True
        # go through entire table row by row
        for row in range(display_table.rowCount()):
            current_table = []
            for column in range(display_table.columnCount()):
                if (display_table.item(row, column) != None):
                    current_table.append(
                        display_table.item(row, column).text())

            # check if check box is checked (防呆機制)
            if (function_class.check_button_array[row].isChecked()):
                if (not (current_table[3] == "USER" or current_table[3] == "ADMIN")):
                    Permission_fit = False
                if (not (current_table[5] == "MALE" or current_table[5] == "FEMALE" or current_table[5] == "OTHERS")):
                    Gender_fit = False
                if (not (current_table[2] == "************")):
                    if (not (helper_function_class().check_password_availability(current_table[2]))):
                        Password_fit = False

        fit_list.append(Permission_fit)
        fit_list.append(Gender_fit)
        fit_list.append(Password_fit)
        return fit_list       
    
