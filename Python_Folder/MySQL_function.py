import mysql.connector
from Helper_function import helper_function_class

class MySQL_function_class:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        # table in database's name
        self.user_info_table = "User_Information"
        self.login_record_table = "Login_record"
        self.plate_info_table = "Plate_Information"

    def connect_to_database(self):
        mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return mydb

    def create_table_first(self, cursor):
        # CREATE TABLE just in case
        cursor.execute("CREATE TABLE if not exists " + self.user_info_table +
                       " (USER_INFORMATION_KEY INT PRIMARY KEY AUTO_INCREMENT, ID VARCHAR(500) UNIQUE, PASSWORD VARCHAR(500), PERMISSION VARCHAR(20), REAL_NAME VARCHAR(50), GENDER VARCHAR(20), PLATE_NUM INT)")
        cursor.execute("CREATE TABLE if not exists " + self.login_record_table +
                       " (LOGIN_RECORD_KEY INT PRIMARY KEY AUTO_INCREMENT, ID VARCHAR(500), LOGIN_TIME VARCHAR(500), LOGIN_STATE VARCHAR(500), SPECIFIC_TYPE VARCHAR(500))")
        cursor.execute("CREATE TABLE if not exists " + self.plate_info_table +
                       "(PLATE_INFORMATION_KEY INT PRIMARY KEY AUTO_INCREMENT, PLATE_ID VARCHAR(500) UNIQUE, LAST_ASSIGNED_USER_ID VARCHAR(500), AVAILABLE_FOR_ASSIGN VARCHAR(20), LAST_ASSIGN_TIME VARCHAR(500), LAST_DEASSIGN_TIME VARCHAR(500))")

    def check_if_user_info_is_empty(self):

        # Connect to database
        mydb = self.connect_to_database()
        mycursor = mydb.cursor()
        self.create_table_first(mycursor)

        mycursor.execute(
            "SELECT EXISTS (SELECT 1 FROM `User_Information`)")
        data = mycursor.fetchone()
        user_amount = data[0]
        if (user_amount == 0):
            sql = (
                "INSERT INTO User_Information(ID, PASSWORD, PERMISSION, REAL_NAME, GENDER, PLATE_NUM) VALUES ('ADMIN', %s, 'ADMIN','name', 'OTHERS', '0')")
            val = (helper_function_class().encode_password('Point1'), )
            mycursor.execute(sql, val)
            mydb.commit()

    # mode 0 ID_password matching or not
    # mode 1 ID is ADMIN or not
    # mode 2 ID exist already or not
    def check_ID_action(self, mode, userid, password, table):
        # Connect to database
        mydb = self.connect_to_database()
        mycursor = mydb.cursor()
        # Create table if not exist
        self.create_table_first(mycursor)
        mycursor.execute("SELECT * FROM " + table)
        for User_record in mycursor:
            # compare the id
            if (User_record[1] == userid):
                if (mode == 0):
                    # compare the password
                    if (User_record[2] == password):
                        return True
                elif (mode == 1):
                    # check the permission
                    if (User_record[3] == "ADMIN"):
                        return True
                elif (mode == 2):
                    return True
        return False

    def add_user(self, userid, password, permission, real_name, gender):
        # Connect to database
        mydb = self.connect_to_database()
        mycursor = mydb.cursor()
        # Create table if not exist
        self.create_table_first(mycursor)
        sql = ("INSERT INTO User_Information(ID, PASSWORD, PERMISSION, REAL_NAME, GENDER, PLATE_NUM) VALUES (%s, %s, %s, %s, %s, %s)")
        val = (userid, password, permission, real_name, gender, 0)
        mycursor.execute(sql, val)
        mydb.commit()

    def remove_user(self, userid):
        # Connect to database
        mydb = self.connect_to_database()
        mycursor = mydb.cursor()
        # Create table if not exist
        self.create_table_first(mycursor)
        sql = ("DELETE FROM User_Information WHERE ID=%s")
        val = (userid, )
        mycursor.execute(sql, val)
        mydb.commit()

    def add_login_record(self, userid, login_state, type):
        # Connect to database
        mydb = self.connect_to_database()
        mycursor = mydb.cursor()
        # Create table if not exist
        self.create_table_first(mycursor)
        sql = (
            "INSERT INTO Login_record(ID, LOGIN_TIME, LOGIN_STATE, SPECIFIC_TYPE) VALUES (%s, %s, %s, %s)")
        val = (userid, helper_function_class().get_time(), login_state, type)
        mycursor.execute(sql, val)
        mydb.commit()

    def update_data_to_user_info(self, userid, password, permission, real_name, gender, plate_amount):
        # Connect to database
        mydb = self.connect_to_database()
        mycursor = mydb.cursor()
        # Create table if not exist
        self.create_table_first(mycursor)
        if (password != None):
            sql = (
                "UPDATE User_Information SET PASSWORD=%s, PERMISSION=%s, REAL_NAME=%s, GENDER=%s, PLATE_NUM=%s WHERE ID=%s")
            val = (password, permission, real_name,
                   gender, plate_amount, userid)
            mycursor.execute(sql, val)
        else:
            sql = (
                "UPDATE User_Information SET PERMISSION=%s, REAL_NAME=%s, GENDER=%s, PLATE_NUM=%s WHERE ID=%s")
            val = (permission, real_name, gender, plate_amount, userid)
            mycursor.execute(sql, val)
        mydb.commit()

    def add_new_plate(self, plateid):
        # Connect to databaseb
        mydb = self.connect_to_database()
        mycursor = mydb.cursor()
        # Create table if not exist
        self.create_table_first(mycursor)

        # Actually insert plate into table
        sql = "INSERT INTO Plate_Information(PLATE_ID, LAST_ASSIGNED_USER_ID, AVAILABLE_FOR_ASSIGN, LAST_ASSIGN_TIME, LAST_DEASSIGN_TIME) VALUES (%s, %s, %s, %s, %s)"
        val = (plateid, "NONE", "TRUE", "NONE", "NONE")
        mycursor.execute(sql, val)
        mydb.commit()

    def remove_plate(self, plateid):
        # Connect to database
        mydb = self.connect_to_database()
        mycursor = mydb.cursor()
        # Create table if not exist
        self.create_table_first(mycursor)

        sql = ("DELETE FROM Plate_Information WHERE PLATE_ID=%s")
        val = (plateid,)
        mycursor.execute(sql, val)
        mydb.commit()

    # mode = 0 for deassign
    # mode = 1 for assign
    def deassign_assign_plate_to_user(self, mode, plateid, userid):
        # Connect to database
        mydb = self.connect_to_database()
        mycursor = mydb.cursor()
        # Create table if not exist
        self.create_table_first(mycursor)
        if (mode == 1):
            # Assign plate to user
            sql = (
                "UPDATE Plate_Information SET LAST_ASSIGNED_USER_ID=%s, AVAILABLE_FOR_ASSIGN='FALSE', LAST_ASSIGN_TIME=%s WHERE PLATE_ID=%s")
            val = (userid, helper_function_class().get_time(), plateid)
        elif (mode == 0):
            # Deassign plate to user
            sql = (
                "UPDATE Plate_Information SET AVAILABLE_FOR_ASSIGN='TRUE', LAST_DEASSIGN_TIME=%s WHERE PLATE_ID=%s")
            val = (helper_function_class().get_time(), plateid)
        mycursor.execute(sql, val)
        mydb.commit()
        self.update_plate_user_have(userid)

    def update_plate_user_have(self, userid):
        # Connect to database
        mydb = self.connect_to_database()
        mycursor = mydb.cursor()
        # Create table if not exist
        self.create_table_first(mycursor)

        sql = ("UPDATE User_Information SET PLATE_NUM = ( SELECT count(*) FROM Plate_Information WHERE LAST_ASSIGNED_USER_ID=%s AND AVAILABLE_FOR_ASSIGN = 'FALSE') WHERE ID=%s")
        val = (userid, userid)
        mycursor.execute(sql, val)
        mydb.commit()

    def get_data_from_database(self, table, type, value, pages):
        # Connect to database
        mydb = self.connect_to_database()
        mycursor = mydb.cursor()
        # Create table if not exist
        self.create_table_first(mycursor)
        if (table == "Login_record"):
            if (type == "all"):
                sql = ("SELECT * FROM Login_record LIMIT %s OFFSET %s")
                val = (20, 20*pages)
            if (type == "id"):
                sql = (
                    "SELECT * FROM Login_record WHERE ID=%s LIMIT %s OFFSET %s")
                val = (value, 20, 20*pages)
            if (type == "status"):
                sql = (
                    "SELECT * FROM Login_record WHERE LOGIN_STATE=%s LIMIT %s OFFSET %s")
                val = (value, 20, 20*pages)
            if (type == "specific_type_fail" or type == "specific_type_success"):
                sql = (
                    "SELECT * FROM Login_record WHERE SPECIFIC_TYPE=%s LIMIT %s OFFSET %s")
                val = (value, 20, 20*pages)
        elif (table == "User_Information"):
            if (type == "all"):
                sql = (
                    "SELECT * FROM User_Information ORDER BY ID ASC LIMIT %s OFFSET %s")
                val = (20, 20*pages)
            if (type == "id_strict"):
                sql = (
                    "SELECT * FROM User_Information WHERE ID=%s ORDER BY ID ASC")
                val = (value,)
            if (type == "id"):
                sql = (
                    "SELECT * FROM User_Information WHERE ID LIKE %s ORDER BY ID ASC LIMIT %s OFFSET %s")
                val = ('%'+value+'%', 20, 20*pages)
            if (type == "name"):
                sql = (
                    "SELECT * FROM User_Information WHERE REAL_NAME LIKE %s ORDER BY REAL_NAME ASC LIMIT %s OFFSET %s")
                val = ('%'+value+'%', 20, 20*pages)
            if (type == "permission"):
                sql = (
                    "SELECT * FROM User_Information WHERE PERMISSION=%s ORDER BY ID ASC LIMIT %s OFFSET %s")
                val = (value, 20, 20*pages)
            if (type == "gender"):
                sql = (
                    "SELECT * FROM User_Information WHERE GENDER=%s ORDER BY ID ASC LIMIT %s OFFSET %s")
                val = (value, 20, 20*pages)
        elif (table == "Plate_Information"):
            if (type == "all"):
                sql = ("SELECT * FROM Plate_Information LIMIT %s OFFSET %s")
                val = (20, 20*pages)
            if (type == "plate_id"):
                sql = (
                    "SELECT * FROM Plate_Information WHERE PLATE_ID LIKE %s ORDER BY PLATE_ID ASC LIMIT %s OFFSET %s")
                val = ('%'+value+'%', 20, 20*pages)
            if (type == "user_id"):
                sql = (
                    "SELECT * FROM Plate_Information WHERE LAST_ASSIGNED_USER_ID LIKE %s ORDER BY LAST_ASSIGNED_USER_ID ASC LIMIT %s OFFSET %s")
                val = ('%'+value+'%', 20, 20*pages)
            if (type == "availability"):
                sql = (
                    "SELECT * FROM Plate_Information WHERE AVAILABLE_FOR_ASSIGN=%s LIMIT %s OFFSET %s")
                val = (value, 20, 20*pages)
        mycursor.execute(sql, val)
        data = mycursor.fetchall()
        return data

    def get_row_number_from_database(self, table, type, value):
        # Connect to database
        mydb = self.connect_to_database()
        mycursor = mydb.cursor()
        # Create table if not exist
        self.create_table_first(mycursor)
        if (table == "Login_record"):
            if (type == "all"):
                sql = ("SELECT count(*) FROM Login_record")
                val = ()
            if (type == "id"):
                sql = (
                    "SELECT count(*) FROM Login_record WHERE ID=%s ORDER BY ID ASC")
                val = (value,)
            if (type == "status"):
                sql = (
                    "SELECT count(*) FROM Login_record WHERE LOGIN_STATE=%s ORDER BY ID ASC ")
                val = (value,)
            if (type == "specific_type_fail" or type == "specific_type_success"):
                sql = (
                    "SELECT count(*) FROM Login_record WHERE SPECIFIC_TYPE=%s ORDER BY ID ASC ")
                val = (value,)
        elif (table == "User_Information"):
            if (type == "all"):
                sql = ("SELECT count(*) FROM User_Information")
                val = ()
            if (type == "id_strict"):
                sql = (
                    "SELECT count(*) FROM User_Information WHERE ID=%s ORDER BY ID ASC")
                val = (value,)
            if (type == "id"):
                sql = (
                    "SELECT count(*) FROM User_Information WHERE ID LIKE %s ORDER BY ID ASC ")
                val = ('%'+value+'%',)
            if (type == "name"):
                sql = (
                    "SELECT count(*) FROM User_Information WHERE REAL_NAME LIKE %s ORDER BY REAL_NAME ASC ")
                val = ('%'+value+'%',)
            if (type == "permission"):
                sql = (
                    "SELECT count(*) FROM User_Information WHERE PERMISSION=%s ORDER BY ID ASC ")
                val = (value,)
            if (type == "gender"):
                sql = (
                    "SELECT count(*) FROM User_Information WHERE GENDER=%s ORDER BY ID ASC ")
                val = (value,)
        elif (table == "Plate_Information"):
            if (type == "all"):
                sql = ("SELECT count(*) FROM Plate_Information")
                val = ()
            if (type == "user_id"):
                sql = (
                    "SELECT count(*) FROM Plate_Information WHERE LAST_ASSIGNED_USER_ID=%s ORDER BY LAST_ASSIGNED_USER_ID ASC")
                val = (value,)
            if (type == "plate_id"):
                sql = (
                    "SELECT count(*) FROM Plate_Information WHERE PLATE_ID=%s ORDER BY LAST_ASSIGNED_USER_ID ASC ")
                val = (value,)
            if (type == "availability"):
                sql = (
                    "SELECT count(*) FROM Plate_Information WHERE AVAILABLE_FOR_ASSIGN=%s ORDER BY LAST_ASSIGNED_USER_ID ASC ")
                val = (value,)

        mycursor.execute(sql, val)
        data = mycursor.fetchone()
        page_number = data[0]
        return page_number

    def get_pages_maximum(self, function_class, value, table):
        if (self.get_row_number_from_database(table, function_class.current_search_type, value) % 20 == 0
                and self.get_row_number_from_database(table, function_class.current_search_type, value) > 20):
            return self.get_row_number_from_database(table, function_class.current_search_type, value) // 20 - 1
        return self.get_row_number_from_database(table, function_class.current_search_type, value) // 20

    def update_row_to_database(self, row):
        if(row[2]== "************"):
            self.update_data_to_user_info(row[1], None, row[3], row[4], row[5], row[6])            
        else:
            self.update_data_to_user_info(row[1], helper_function_class().encode_password(row[2]), row[3], row[4], row[5], row[6])
