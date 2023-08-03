from MySQL_function import MySQL_function_class

class object:
    def connect_database(self):
        return MySQL_function_class("localhost", "root", "password", "UI_database")

class user(object):
    def __init__(self, userid):
        self.userid = userid
        self.password = None
        self.permission = None
        self.name = None
        self.gender = None
        self.plate = []
        self.plate_num = None

        self.connect_database()
        self.exist = self.SetUserInfo()

    def SetUserInfo(self):
        # Connect to database
        mydb = self.connect_database().connect_to_database()
        mycursor = mydb.cursor()
        # Create table if not exist        
        sql = (
            "SELECT * FROM User_Information WHERE ID = %s ORDER BY ID ASC")
        val = (self.userid,)
        mycursor.execute(sql, val)
        data = mycursor.fetchone()
        if(data is None):
            return False
        else:
            self.password = data[2]
            self.permission = data[3]
            self.name = data[4]
            self.gender = data[5]
            self.plate_num = len(self.get_plate_id_user_have())
            return True

    def get_plate_id_user_have(self):
        # Connect to database
        mydb = self.connect_database().connect_to_database()
        mycursor = mydb.cursor()

        sql = "SELECT `PLATE_ID` FROM `Plate_Information`WHERE `LAST_ASSIGNED_USER_ID` = %s AND `AVAILABLE_FOR_ASSIGN` = 'FALSE'"
        val = (self.userid, )

        mycursor.execute(sql, val)
        data = mycursor.fetchall()
        for num in range(len(data)):
            plate_id = data[num][0]
            self.plate.append(plate_id)
        return data

class plate(object):
    def __init__(self, plateid):
        self.plateid = plateid
        self.LastAssignedUserID = None
        self.availability = None
        self.LastAssignedTime = None
        self.LastDeassignedTime = None
        self.exist = self.SetPlateInfo()

    def SetPlateInfo(self):
        # Connect to database
        mydb = self.connect_database().connect_to_database()
        mycursor = mydb.cursor()
        sql = (
            "SELECT * FROM Plate_Information WHERE PLATE_ID = %s")
        val = (self.plateid,)
        mycursor.execute(sql, val)
        data = mycursor.fetchone()
        # example:  data = 
        if(data is None):
            return False
        else:
            self.plateid = data[1]
            self.LastAssignedUserID = data[2]
            self.availability = data[3]
            self.LastAssignedTime = data[4]
            self.LastDeassignedTime = data[5]     
            return True

