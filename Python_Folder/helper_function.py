from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit
import datetime
import hashlib
import re
import User

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

    def data_comparison(self, edited_data, initial_data, logger_class):
        for row in zip(edited_data, initial_data):
            if (row[0][1] != "************"):
                logger_class.logger.info(
                    "USER ID: '" + row[0][0] + "'s password has been edited.")
            if (row[0][2] != row[1][2]):
                logger_class.logger.info(
                    "USER ID: '" + row[0][0] + "'s permission has been edited from '" + row[1][2] + "' to '" + row[0][2] + "'.")
            if (row[0][3] != row[1][3]):
                logger_class.logger.info(
                    "USER ID: '" + row[0][0] + "'s name has been edited from '" + row[1][3] + "' to '" + row[0][3] + "'.")
            if (row[0][4] != row[1][4]):
                logger_class.logger.info(
                    "USER ID: '" + row[0][0] + "'s gender has been edited from '" + row[1][4] + "' to '" + row[0][4] + "'.")

    def insert_data_into_table(self, display_table, data, function_class):
        display_table.setRowCount(0)
        row_count = 0
        function_class.check_button_array = []
        function_class.initial_data = []
        data_list = []
        for row in data:
            display_table.insertRow(row_count)
            for column in range(display_table.columnCount()):
                display_table.setItem(row_count, column, QtWidgets.QTableWidgetItem(str(row[column])))
                data_list.append(row[column])
            function_class.initial_data.append(data_list)
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

