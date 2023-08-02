from MySQL_function import MySQL_function_class

class user:
    def __init__(self, userid):
        self.userid = userid
        self.password = None
        self.permission = None
        self.name = None
        self.gender = None
        self.plate = []
        self.plate_num = None

        self.SQL_function = MySQL_function_class("localhost", "root", "Ar0340252", "UI_database")
        self.exist = self.GetUserInfo()

    def GetUserInfo(self):
        # Connect to database
        mydb = self.SQL_function.connect_to_database()
        mycursor = mydb.cursor()
        # Create table if not exist        
        sql = (
            "SELECT * FROM User_Information WHERE ID = %s ORDER BY ID ASC")
        val = (self.userid,)
        mycursor.execute(sql, val)
        data = mycursor.fetchone()
        # example:  data = (83, 'aaaa', '419c29938c8bdf72a7bd6035b2865c0f', 'ADMIN', 'name', 'MALE', 2)
        if(data is None):
            return -1
        else:
            self.password = data[2]
            self.permission = data[3]
            self.name = data[4]
            self.gender = data[5]
            self.plate_num = len(self.get_plate_id_user_have())
            return data

    def get_plate_id_user_have(self):
        # Connect to database
        mydb = self.SQL_function.connect_to_database()
        mycursor = mydb.cursor()
        # Create table if not exist
        self.SQL_function.create_table_first(mycursor)

        sql = "SELECT `PLATE_ID` FROM `Plate_Information`WHERE `LAST_ASSIGNED_USER_ID` = %s AND `AVAILABLE_FOR_ASSIGN` = 'FALSE'"
        val = (self.userid, )

        mycursor.execute(sql, val)
        data = mycursor.fetchall()
        for num in range(len(data)):
            plate_id = data[num][0]
            self.plate.append(plate_id)
        return data
