Critical!! Before start using this UI program, please read following information:

        1.      The python file is located at "/Project_Folder/UI_MySQL.py", please run it with python.

        2.      Edit the database information located in: 
                        class MySQL_function() --> def connect_to_database(self)
        
        3.      Run the program and check the "Admin mode" checkbox, then Login with following id 
                and password:
                        ID:         "ADMIN"
                        PASSWORD:   "Point1" 
                
        4.      While adding a new users, the default password will be set as "Point1", which the user can 
                edit it after logging in.
        
        5.      In the editing window/tabs, the checkboxes infront of each rows are for mistake-proofing 
                purpose, the change will be applied only when the checkbox of the row is checked, including 
                deletion and edit.

        6.      In Advance UI, the table display 20 row of data per pages.

        7.      All the format relating information can be founded in Readme.md

        8.      Logger.py is a helper class that can easily generate a logger object for logging purpose, and
                manual regarding it is locate at end of this document.


Please follow the following format while editing user info:

    Edit User info:

        Manual: 
            1. Please check the checkbox at the row that you like to edit, users at rows that aren't checked 
            will not be edited.
            2. After editing, press the "Save change" button.
            3. The change will be applied immediately, please double check if the edit is successful. 

        ID:
            1. Should not be less than 4 characters.
            2. Do not contains special character (e.g.!@#$*) and white space.
            3. Every ID is unique, inputing existing ID is not allowed.
        Password:  
            1. Should not be less than 6 characters.
            2. Do not contains special character (e.g.!@#$*) and white space.
            3. Should be the combination of numbers and alphabets, which should including atleast one upper and 
            lower letter each.
        
        Permission: 
            1. Only accept "ADMIN" and "USER".
            2. Please beware that the editor is capital sensitive.

        Gender:
            1. Only accept "MALE", "FEMALE", and "OTHERS".
            2. Please beware that the editor is capital sensitive.

    Add a User:
        1. When inputing user id, please follow the format mentioned above.
        2. All the information should be filled or checked.
    
    Delete a User:
        1. Please check the checkbox at the row that you like to delete, users at rows that aren't checked 
        will not be deleted.
        2. Deletion will be applied immediately after pressing the OK button in popup window.
        3. If the user desired to delete still has plates, those plates will automatically be deassigned.


Please follow the following format while editing plate info:

    Add new plate:
        1. Please press the "Add new plate" button, after the popup window appears, then scan the barcode on 
        the plate.
        2. The windows will automatically close and re-open for next scanning.
        3. After the scanning is done, press the "cancel" button.

    Remove plate:
        1. Please check the checkbox at the row that you like to remove, plates at rows that aren't checked 
        will not be removed.
        2. Deletion will be applied immediately after pressing the OK button in popup window.
    
    Assign plate to user:
        1. Only the plate that display "TRUE" at "Avaliable_for_assign" column can be assigned.
        2. Please check the checkbox at the row that you like to assign, plates at rows that aren't checked 
        will not be assigned.
        3. Please input the correct user ID, it's capital sensitive.

    Deassign plate from user:
        1. Please check the checkbox at the row that you like to deassign, plates at rows that aren't checked 
        will not be deassigned.
        

