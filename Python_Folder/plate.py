from MySQL_function import MySQL_function_class

class plate:
    def __init__(self, plateid):
        self.plateid = plateid
        self.LastAssignedUserID = None
        self.availability = None
        self.LastAssignedTime = None
        self.LastDeassignedTime = None



        self.SQL_function = MySQL_function_class("localhost", "root", "Ar0340252", "UI_database")
        self.exist = self.GetPlateInfo()

    def GetPlateInfo(self):
        # Connect to database
        mydb = self.SQL_function.connect_to_database()
        mycursor = mydb.cursor()
        sql = (
            "SELECT * FROM Plate_Information WHERE PLATE_ID = %s")
        val = (self.plateid,)
        mycursor.execute(sql, val)
        data = mycursor.fetchone()
        # example:  data = 
        if(data is None):
            return -1
        else:
            self.plateid = data[1]
            self.LastAssignedUserID = data[2]
            self.availability = data[3]
            self.LastAssignedTime = data[4]
            self.LastDeassignedTime = data[5]     
            return data

