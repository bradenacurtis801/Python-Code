Employee database

Navigate to: cs2450-project-main > emp_data_project >
emp_data

To open the UVU employee database, 
you can either run the main.py file, 
or run python3 main.py from the command line.

For admin access:
User ID: 0
Password: 0 

For employee access:
User ID: 1
Password: 1

There are several other admins/employees 
you can login as but those were set up for simplicity.

You will be able to log in to any employee or admin
you create.

Admin Page Window:
- To access any employee you simply need to double click on the one you wish to view/edit.
- There are also headers at the top that you can click on to sort the employees (click one to sort from typical top-to-bottom, click a second time it sorts in reverse. )
- To search employee via the search bar at the bottom, simply type in the letters of the employee name and it will search dynamically as you type each letter. 
- The search button's default filter is search by 'Last Name' if you want to change that to search by 'ID' just click on the filter dropdown menu, and select 'ID'.
- If you want to export database click on the 'Generate Report' button. It will bring up a window with options on what databases you want to export, as well as where you want the file stored.
- If you want to add new employee, click on 'add new employee' and it will bring you to a new window with an empty employee to fill in each data fields. 
- Note - you must enter in all data fields including dropdown menu's for new employee, with the exception of leaving entry field 'End Date' blank. 
- all dropdown menu's are key sensitive so for instance if you are selecting the state 'Utah' for the employee, all you need to do is click the letter 'U' and it will automatically select 'UT' for you.
- Note that Employee status say's 'active', this will reflect the fact that when the employee is submitted into the database, it will state employee is currently active. 
    When the employee gets archived, then their status will say 'inactive' in the database.
- At the top left corner of the employee table, there is a button that will switch between employee and archived employee databases.
    - If the button says 'Switch to Archived Employees' Then the current table you are viewing shows only active employees.
    - If the button says 'Switch to 'Active Employees' Then the current table you are viewing shows only archived employees.
    - If you click the button it will change the table's viewable employees with the other database. 
- If admin user's want to archive an employee, double click employee and click 'Archive Employee' (if admin is not seeing this option, then go back and click 'Switch To Active Employees')
- If admin user's want to re-activate an employee, double click employee and click 'Activate Employee' (if admin is not seeing this option, then go back and click 'Switch To Archived Employees')
    


Employee Page Window:
- To edit employee, simply press 'Edit Employee'

All employee records that include their login and password will be on the employees.csv file.
!!!IMPORTANT!!! - DO NOT EDIT ANY OF THE CSV FILES IN THE ROOT DIRECTORY. IF USER DOES SO, THEN IT COULD POSSIBLY CAUSE FUNCTIONALITY ISSUES.



