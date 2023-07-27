# Readme

<br/>

## Critical!

Before start using this UI program, please read following information:

1. The python file is located at:
   ```bash
   /Project_Folder/UI_MySQL.py
   ```

2. Edit the database information located in:
   ```python
   class MySQL_function() >> def connect_to_database(self)
   ```
3. Run the program and check the "Admin mode" checkbox, then Login with following id 
and password:
   ```bash
   ID:         ADMIN
   PASSWORD:   Point1 
   ```
4. While adding a new users, the default password will be set as "Point1", which the user can edit it after logging in.

5. In the editing window/tabs, the checkboxes infront of each rows are for mistake-proofing purpose, the change will be applied only when the checkbox of the row is checked, including deletion and edit.

6. In Advance UI, the table display 20 row of data per pages.

7. All the format relating information can be founded in Readme.md

8. Logger.py is a helper class that can easily generate a logger object for logging purpose, and manual regarding it is locate at end of this document.

<br/><br/>

## UI_MySQL.py file contains four Ui classes and eight function classes:


## UI classes:

1. There're four Ui classes for Login (Ui_Login()), Register (Ui_Register()), normal user Info Editor (Ui_Info_Editor()), and Admin user info editor interface. 

2. All the UI classes are generated by Qt Designer, including in-class function: setUpUI() and retranslateUi(). 

3. Asside from the generated function, there's a modding() function added for modding specific behavier, if there's any need to mod any Ui classes, please mod it in modding() function, and make sure to call the modding() in the end of setUpUI(). 

4. Similarly, when regernating the Ui function, please copy and overwrite classes setUpUI() and retranslateUi(), then call the modding() in the end of setUpUI(). Sample code is shown below:
   ```python
           class Ui_sample(object):
           # generated code
           def setupUi(self, sample):
               ...
               self.modding()  # always add this line in to imply the mod
           
           # generated code
           def retranslateUi(self, sample):
               ...
           
           # function for all the modding, e.g. connecting button to function, hiding the 
           # labels, and etc.
           def modding(self):
               ...
   ```


2. Function classes:

   - Each UI class has its own function class to handle all the action, and the only exception is UI_Concentrate_Advance since it has three tabs, therefore there's three individual funcitons for each of them.
   
   - There're two extra function classes, MySQL_function and helper_function that handles some general action, and MySQL relating action.
   
   - Whenever any function encountered exception, it will return -1 and log the message into "Error.log".
   
   - There are many variables that share the same name in different function, that is for convenience purpose. Therefore some of the function can simply use function's name as a parameter, and handle multiple function's action by just itself.

<br/><br/>

   1.  UI_Login_function class:

      1. `check_ID_password_function(self, userid, password):`
        
         This function is connected to the login button in login_Ui, which will take the context that user types in textbox "UserID_Input" as userid and "password_Input"
         as password, checking the availability of them, and determine the login type to be recorded.
            
         No matter whether user's success or failed the login action, the record will be added into database's Login_record table.
            
         However, if the login action failed, the error message will be displayed.
            
         Regardless the type of failure, whenever login action failed, function will return a boolean value of False. 
            
         On the other hand, whenever login action success, function will return boolean value of True.
            
         Finally, regardless user login in Admin or Normal user mode, as long as the login is successful,this window (Loginui) will be closed.
         
         P.S. both parameters userid and password are string.
<br/>
   - `open_Concentrate_Advance_window(self),  open_Info_Editor_window(self):`
         
      These two functions are used for displaying the windows when user input the correct userid 
      and password.
         
      Only one of these windows will be displayed, which depends on whether user had checked the 
      admin mode checkbox. 
         
      No return values for both of these function.
<br/>
   - `display_normal_welcome_message():`

      This function will only be called when user logins in normal mode, it will capture the userid
      and display a popup windows that ask whether user want to display the personal information 
      editing window.
         
      No return values for this function.
<br/>
<br/>
   2. UI_Info_Editor_function class:

   - `Global variable:`

      initial_data:
      List variable to store data that just captured from database.
      
      edited_data:
      List variable to store edited data that was captured from table.  


2.      show_user(self, pages):

This function will capture user's information from database, then insert checkbox and user 
information into table.

Meanwhile, the raw data that just got captured from database will be stored into the  
list "self.initial_data".

This function does has one unused parameter "pages", which is completely normal. Since there
will be another function named exactly same as this function in other class, and for the
purpose of making code more compact, these two function that shares the same name will be 
called in other function at the same line. 

Therefore I make these two function having the same parameter, despite it's not used. 

No return values for this function.


III.UI_Search_Edit_function class:

1.      Global variable:

initial_data:
List to store data that just captured from database.

edited_data:
List to store edited data that was captured from table.  

user_info_pages_maximum:
Integer that represent the maximum pages that can be displayed in table, to
prevent user access the pages that doesn't contains data.

current_search_type:
String that represent current searching type, including "all", "id", etc. 
Initially set to "all". 

check_button_array_search_edit:
List to store the index of row that mistake_proofing checkbox is checked. 


2.      show_user(self, pages):

This function will capture user's information from database according to the current 
searching type and the interger "page" parameter, which represent the page number, then 
insert checkbox and user information into table.

No return value for this function.


3.      open_Register_window(self):

This functions are used for opening the register windows when user press the "add a 
user" button.

No return value for this function.


4.      show_delete_confirm(self):

This function will display a popup windows with confirm message, Pressing OK button will 
call the delete_user() function below, while pressing Cancel will cancel the action.  

No return value for this function.


5.      delete_user(self):

This function will only be called when user confirm the deletion in delete_confirm window, 
then will delete users from database (only when the mistake-proofing at its row are checked).

Besides, if the users that are going to be deleted has assigned plates, this function will 
automatically deassign those plates.

No return value for this function.



IV. UI_Register_function class:

1.      press_register(self, userid, password, real_name):

This function will check if inputs in register window is valid. If so, then the user with 
inputted information will be added into the database.

userid, password, and real_name are given by parameter, while gender and permission are 
captured by checking whether the button is checked.

If the user is added successfully, this function will return a boolean value True, and 
will return False elsewise.

P.S. All parameters are string.


V.  UI_Login_History_function class:

1.      Global variable:

login_history_pages_maximum:
Integer that represent the maximum pages that can be displayed in table, to
prevent user access the pages that doesn't contains data.

current_search_type:
String that represent current searching type, including "all", "id", etc. 
Initially set to "all"


2.      show_login_history(self, pages):
This function will capture user's information from database according to the current 
searching type and the interger "page" parameter, which represent the page number.

No return value for this function.                



V.  UI_Plate_info_function class:

1.      Global variable:

login_history_pages_maximum:
Integer that represent the maximum pages that can be displayed in table, to
prevent user access the pages that doesn't contains data.

current_search_type:
String that represent current searching type, including "all", "user_id", etc. 
Initially set to "all"

check_button_array_search_edit:
List to store the index of row that mistake_proofing checkbox is checked. 


2.      show_plate_info(self, pages):

This function will capture plate information from database according to the current searching
type and the integer "page" parameter, which represent the page number, then insert checkbox
row by row.

No return value for this function. 

3.      show_add_new_plate_window(self):

This function will display a popup windows with text edit box, user can either typing the 
plate id and press "OK" button (or press return key on keyboard), or scan the barcode on plate
with barcode scanner. 

Both actions above will add the plate with given id into the database, with default 
values: 

(Available_for_assign == TRUE, Last_Assign_Time == NONE, Last_Deassign_Time == NONE)

This function performed a recursion, until user press "Cancel" button, or press "OK" button 
without input. 


4.      show_delete_plate_confirm(self):

This function will display a popup windows with confirm message, Pressing OK button will 
call the remove_plate() function below, while pressing Cancel will cancel the action.  

No return value for this function. 


5.      plate_action(self, mode, userid):

This function handle all the plate regarding action, and the integer parameter "mode" 
tells which action this function should perform:

mode = 0 for deassign the plate from user.
mode = 1 for remove the plate.
mode = 2 for assign the plate to user.

No return value for this function. 


6.      show_assign_plate_to_user_window(self):

This function will display a popup windows with text edit box, which user can type the userid 
in.

After the "OK" button is pressed, the plates that its row's mistake-proofing checkbox is 
checked, and "Available_for_assign" of that plate is "TRUE", will be assigned to the user. 
Then update user's plate number in database.

If the userid doesn't exist, then the action will fail and display the error message.

No return value for this function. 


7.      show_deassign_plate_to_user_window(self):

This function will display a popup windows with confirm message, Pressing OK button will 
call the deassign_plate() function below, while pressing Cancel will cancel the action.  

No return value for this function. 


VI. helper_function class:

1.      encode_password(self, password):

This function will encode the parameter "password" in md5, then return the encoded string.

P.S. Parameter "password" is a string desired to be encoded.


2.      get_time(self):

This function returns current time.


3.      lock_the_Column(self, display_table, lock_column):

This function makes the "display_table"'s "lock_column" read only.

P.S. Patameter "display_table" is a Qtablewidget that like to mod, while "lock_column" is an
Integer that stands for the number of column to be locked.

No return value for this function. 


4.      has_capital_letters(self, password), 
has_lower_letters(self, password), 
has_numbers(self, password), 
has_invalid_hcaracter(self, password):

These function are used to check each properties that a valid password or userid should have,
will be used in the following check_password_availability() function, and returns a boolean 
values.

P.S. Parameter "password" is a String to be checked if it contains all the above properties.


5.      check_password_availability(self, password):

This function will check if the password is availability by calling the "has......" function 
above, and returns a boolean value.

P.S. Parameter "password" is a String to be checked if it's valid.


6.      data_comparison(self, edited_data, initial_data):

This function compare two list parameters, edited_data and initial_data, then log the message
that record the changes that had been made into the logging file.

No return value for this function. 


7.      insert_data_into_table(self, display_table, data):

Depends on the display_table (QTableWidget object) parameter that get passed into this 
function, it will insert list object "data" and checkboxes corresponding to passed 
display_table.

No return value for this function. 


8.      insert-checkbox(self, function_class, display_table, data):

This function is a helper function for insert_data_into_table() function, which will insert
checkbox into the given display_table (QTableWidget object) in given 
function_class (function object). 

Then, store the checkbox into the list ".check_button_array" that all the function class that
needed checkbox has. 

No return value for this function. 


9.      get-pages_maximum(self, function_class, table):

This function get the number of data that database's table have according to the 
current_search_type of given function_class, then divides them by 20 to get the 
page number (Integer) and return it.

The "table" variable is a String, which will be used by passing the tables name that were 
declared in __main__. 


10.      set_current_search_type(self, function_class, type):

This function is a setter for ".current_search_type" in other function class, which will 
set the ".current_search_type" in "function_class" to the "type"

No return value for this function. 


11.      get_data_from_table(self, display_table, function_class):

This function will capture the data in the display table, and store it into the list 
".edited_data" in "function_class". 

Then compare it with "function_class.initial_data".

Finally, refresh the display_table.

No return value for this function. 



VII.MySQL_function class:

This function class contains all the function that contains SQL statements.


1.      connect_to_database(self):

Connect to the target database, and returns a MySQLConnection (mydb).

No return value for this function. 


2.      create_table_first(self, cursor):

create three table: User_Information, Login_record, and Plate_Information if not exist.

The paramater "cursor" is a MySQLcursor, which can be defined by mydb.cursor() before calling
the function.

No return value for this function. 


3.      check_if_user_info_is_emtpy(self):

create a user with default values (userid = "ADMIN", password = "Point1", and 
permission = "ADMIN") if there's no user exists in User_information table.

No return value for this function. 


4.      check_ID_action(self, mode, userid, password, table):

These functions will check the properties of "userid" from database's "table" according to 
the integer parameter "mode".

mode = 0 for checking "userid" and "password" matches or not.
mode = 1 for checking "userid" is an ADMIN or not.
mode = 2 for checking "userid" exists or not.

Then the function will return the corresponding bool value.

P.S. Parameter "userid", "password", and "table" are all Strings. 


5.      add_user(self, userid, password, permission, real_name, gender):

Add a user with given properties into the database.

P.S. All parameters are strings, yet should follow the given format. And plate amount will be
setted to 0 by default.

No return value for this function. 


6.      remove_user(self, userid):

Remove the user with given userid from the database.

No return value for this function. 


7.      add_login_record(self, userid, login_state, type):

Add a record into the database with given userid, state, and specific type.

P.S. All parameters are strings, yet should follow the given format.

No return value for this function. 


8.      update_data_to_user_info(self, userid, password, permission, real_name, gender):

Update the user information in database that matches "userid" with given "password", 
"permission", "real_name" and "gender".

All parameters are strings, yet should follow the given format.

No return value for this function. 


9.      add_new_plate(self, plateid):

Add a plate with given string parameter "plateid", and default value of:

Last_Assigned_User_ID = "NONE"
Available_for_assign = "TRUE"
Last_Assign_Time = "NONE"
Last_Deassign_Time = "NONE"

into database.

No return value for this function. 


10.      remove_plate(self, plateid):

Drop the plate that plateid = "plateid" from the database.

No return value for this function. 


11.      deassign_assign_plate_to_user(self, mode, plateid, userid):

This function will deassign or assign plates from or to user, according to the integer 
parameter "mode".
mode = 0 form deassign plate from user.
mode = 1 from assign plate to user.

Deassign plate will update the plate's availability with given "plateid" to "TRUE", and 
update LAST_DEASSIGN_TIME to current time.

Assign plate will update the plate's availability with given "plateid" to "FALSE", and 
update LAST_ASSIGN_TIME to current time.

Finally, logs the message to the logging file.

No return value for this function. 


12.      update_plate_user_have(self, userid):

Update the number of plate that user's id = "userid" by checking the database. 

No return value for this function. 


13.      get_data_from_database(self, table, type, value, pages):

This function will get the data from given "table" in database according to the given string 
parameters "type", "value", and "pages", where "type" represents the searching type and 
"value" the specific value that can be search under the type. 

For instance, when "type" is "id", then value will be the actual id text that user input.

Finally, fetch the data into a list as a return value.


14.      get_row_number_from_database(self, table, type, value):

Get the number of row that each "table" in database has, fetching it to an Integer then 
returns.

The "type" and "value" are the same as get_data_from_database() function above, 

15.      get_plate_id_user_have(self, userid):

This function get the plate_id of the plate that user with "userid" had got assigned, 
which will be used for deassiging while deleting the user that still has plates assigned to. 

The return value is a list that contains all the plate_id of the plate that belongs to this 
user.


Logger.py's manual:

'''
This class is a simple logging class that provides easier logging experience. 
To use this loggin class, just create a logger object with desired parameter. 
For instance, to create a logger named: TestLogger with a level of INFO and located at "Log_Folder/Test.log",

You will have to declare a variable like following:

TestLogger = logger_class("test_logger", logging.INFO, "Log_Folder/Test.log")

Then, to log the message into log file, call the created logger with .logger, then you will be able to log the 
message with desired level.

For instance to log a message into log file at info level, you will have to do it like:

TestLogger.logger.info("This is a test info message )
'''
