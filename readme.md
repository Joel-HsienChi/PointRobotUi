# Readme

## Critical!

## Before start using this UI program, please read following information:

- The python file is located at:
```bash
/Project_Folder/UI_MySQL.py
```

- Edit the database information located in:
```python
class MySQL_function() >> def connect_to_database(self)
```
- Run the program and check the "Admin mode" checkbox, then Login with following id 
and password:
```bash
ID:         ADMIN
PASSWORD:   Point1 
```
- While adding a new users, the default password will be set as "Point1", which the user can edit it after logging in.

- In the editing window/tabs, the checkboxes infront of each rows are for mistake-proofing purpose, the change will be applied only when the checkbox of the row is checked, including deletion and edit.

- In Advance UI, the table display 20 row of data per pages.

- All the format relating information can be founded in Readme.md

- Logger.py is a helper class that can easily generate a logger object for logging purpose, and manual regarding it is locate at end of this document.

- This program is currently running a local database, please mod the database information before running the program, which is located in `__main__`

     `SQL_function = MySQL_function("localhost", "root", "password", "UI_database")`

## Please follow the following format while editing user info:

1. Edit User info:

   1. Manual: 

        - Please check the checkbox at the row that you like to edit, users at rows that aren't checked will not be edited.
        - After editing, press the "Save change" button.
        - The change will be applied immediately, please double check if the edit is successful. 

    2. ID:

        - Should not be less than 4 characters.
        - Do not contains special character (e.g.!@#$*) and white space.
        - Every ID is unique, inputing existing ID is not allowed.

    3. Password:  

        - Should not be less than 6 characters.
        - Do not contains special character (e.g.!@#$*) and white space.
        - Should be the combination of numbers and alphabets, which should including atleast one upper and lower letter each.
    
    4. Permission: 

        - Only accept "ADMIN" and "USER".
        - Please beware that the editor is capital sensitive.

    5. gender:

        - Only accept "MALE", "FEMALE", and "OTHERS".
        - Please beware that the editor is capital sensitive.

2. Add a User:
    
    - When inputing user id, please follow the format mentioned above.
    - All the information should be filled or checked.

3. Delete a User:
    - Please check the checkbox at the row that you like to delete, users at rows that aren't checked will not be deleted.
    - Deletion will be applied immediately after pressing the OK button in popup window.
    - If the user desired to delete still has plates, those plates will automatically be deassigned.

## Please follow the following format while editing plate info:

1. Add new plate:
    - Please press the "Add new plate" button, after the popup window appears, then scan the barcode on the plate.
    - The windows will automatically close and re-open for next scanning.
    - After the scanning is done, press the "cancel" button.

2. Remove plate:
    - Please check the checkbox at the row that you like to remove, plates at rows that aren't checked will not be removed.
    - Deletion will be applied immediately after pressing the OK button in popup window.

3. Assign plate to user:
    - Only the plate that display "TRUE" at "Avaliable_for_assign" column can be assigned.
    - Please check the checkbox at the row that you like to assign, plates at rows that aren't checked will not be assigned.
    - Please input the correct user ID, it's capital sensitive.

4. Deassign plate from user:
    - Please check the checkbox at the row that you like to deassign, plates at rows that aren't checked will not be deassigned.
        

