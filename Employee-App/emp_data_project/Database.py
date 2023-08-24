''' TO DO: outline database class, attr, methods
Questions for meeting:
how to save between runs '''
# import Employee
import os
import csv
from utils.normalize_path import normalize_path
from classificationADT import *
import re


        
class Employee():
    """
    Main employee class
    Initialize it with Name SNN Phone email and its classification, after
    that use the three functions set_address, set_pay and set_job to fill
    in the rest of the info
    The reason it is split so weird is because you might not necessarily
    want to put in 100% of someones info at once so its split into three
    categories
    """

    def __init__(self, id_num=None, fname=None, lname=None, classification=None, birth_date=None, ssn=None, phone=None,
                 email=None, permission=None, password=None):
        """Initializes the employee object with basic data members.
        """
        # if not isinstance(id_num, int):
        #     raise ValueError("id_num must be of type int")
        
        # if not isinstance(fname, str):
        #     raise ValueError("name must be of type str")
        
        # if not isinstance(lname, str):
        #     raise ValueError("name must be of type str")
        
        # if not isinstance(classification, int):
        #     raise ValueError("classification must be of type int")
        
        # if not re.match(r"\d{2}-\d{2}-\d{4}", birth_date):
        #     raise ValueError("birth_date must be in the format MM-DD-YYYY")
        
        # if not re.match(r"\d{3}-\d{2}-\d{4}", ssn):
        #     raise ValueError("ssn must be in the format XXX-XX-XXXX")
        
        # if not re.match(r"\(\d{3}\)\d{3}-\d{4}", phone):
        #     raise ValueError("phone must be in the format (XXX)XXX-XXXX")
        
        # if not re.match(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email):
        #     raise ValueError("email must be a valid email address")
        
        # if not re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password):
        #     raise ValueError("password must contain at least 8 characters, including one uppercase letter, one lowercase letter, one digit, and one special character")
        
        self.id = id_num
        self.first_name = fname
        self.last_name = lname
        self.classification = classification
        self.birth_date = birth_date
        self.ssn = ssn
        self.phone = phone
        self.email = email
        self.permission = permission
        self.password = password
        self.start_date = 'MM/DD/YYYY'
        self.end_date = 'MM/DD/YYYY'
        # self.address = None
        # self.city = None
        # self.state = None
        # self.zip = None
        # self.pay_method = None
        # self.title = None
        # self.dept = None
        # self.job_status = None
        
    def set_classification(self, class_num: int, pay_val_1: float, pay_val_2=0.0):
        """Sets the self.classification member of the employee class
        properly to an Hourly, Salary or Commissioned object, and stores
        the appropriate payment info within it.
        This function can be used to set/change an employee's pay, as
        well.
        Input: The int 1, 2, or 3 for classification type of Hourly,
                Salary, or Commissioned, respectively.
                For Hourly, input just hourly pay rate (float).
                For Salaried, input just salary (float).
                For Commissioned, input salary first (float), then
                    commission pay rate (float).
        """
        if class_num == 1:
            self.classification = Hourly(pay_val_1)
        elif class_num == 2:
            self.classification = Salary(pay_val_1)
        elif class_num == 3:
            self.classification = Commissioned(pay_val_1, pay_val_2)
        else:
            raise Exception(f'Classification for emp: "{self.name}" invalid.')

    def set_pay_method(self, pay_method_num, route=0, account=0):
        """Sets the self.pay_method member of the employee class properly
        to a DirectMethod or MailedMethod object, and stores the route and
        account number if DirectMethod.
        """
        if pay_method_num == 1:
            self.pay_method = DirectMethod(self, route, account)
        elif pay_method_num == 2:
            self.pay_method = MailedMethod(self)
        else:
            raise Exception(f'Pay method for emp: "{self.name}" invalid.')

    def set_address(self, address, city, state, zipcode):
        """
        Sets address city state and zipcode for the employee
        """
        self.address = address
        self.city = city
        self.state = state
        self.zip = zipcode

    def set_job(self, start_date, title, dept):
        """
        Sets start date, title and department for the employee
        """
        self.start_date = start_date
        self.title = title
        self.dept = dept

    def terminate_employee(self, end_date):
        """
        Sets the end date for an employee
        """
        self.end_date = end_date

    def populate_from_row(self, row):
        """
        Sets all of an employees attributes from a dict of a row from a csv file
        """
        self.id = int(row["ID"])
        self.name = row["Name"]
        name = self.name.split(" ")
        self.first_name = name[0]
        self.last_name = name[-1]

        # Set the appropriate classification type:
        classification = int(row["Classification"])
        if classification == 1:
            self.classification = Hourly(float(row["Hourly"]))
        elif classification == 2:
            self.classification = Salary(float(row["Salary"]))
        elif classification == 3:
            self.classification = Commissioned(float(row["Salary"]),
                                               float(row["Commission"]))
        else:
            raise Exception(f'Classification for emp: "{self.name}" invalid.')

        self.ssn = row["SSN"]
        self.phone = row["Phone"]
        self.email = row["Email"]
        self.address = row["Address"]
        self.city = row["City"]
        self.state = row["State"]
        self.zip = row["Zip"]

        # Set the desired pay method:
        pay_method = int(row["Pay_Method"])
        if pay_method == 1:
            self.pay_method = DirectMethod(self, row["Route"], row["Account"])
        elif pay_method == 2:
            self.pay_method = MailedMethod(self)
        else:
            raise Exception(f'Pay method for emp: "{self.name}" invalid.')

        self.birth_date = row["Birth_Date"]
        self.start_date = row["Start_Date"]
        self.end_date = row["End_Date"]
        self.title = row["Title"]
        self.dept = row["Dept"]
        self.permission = row["Permission"]
        self.password = row["Password"]

    def payment_report(self):
        """Returns a message that states how much the employee will be
        paid, and in what method.
        """
        payment = self.classification.calculate_pay()

        return self.pay_method.payment_message(payment)

    def full_address(self):
        """Returns the employee's full address.
        """
        return f'{self.address}, {self.city}, {self.state} {self.zip}'

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return bool(self.id == other.id)
    def __repr__(self):
        return f"<Employee-name={self.name}>"

class EmployeeDB:
    def __init__(self):
        self.cur_user = ''
        self.USERNAME_INDEX = 0
        self.PASSWORD_INDEX = 1
        self.EMPLOYEE_TYPE_INDEX = 2
        self.ID_NUMBER_INDEX = 20
        
        if not os.path.exists(normalize_path(".//employees.csv")):
            with open(normalize_path(".//employees.csv"), 'x', encoding="utf8", ) as database:
                writer = csv.writer(database)
                writer.writerow(
                    "ID,Name,Address,City,State,Zip,Classification," \
                    "Pay_Method,Salary,Hourly,Commission,Route,Account," \
                    "Birth_Date,SSN,Phone,Email,Start_Date,End_Date," \
                    "Title,Dept,Permission,Password".split(','))
                self.database = open(".//employees.csv", encoding="utf8", )
                
        else:
            self.database = open(normalize_path(".//employees.csv"), encoding="utf8")

        # Make Admin csv file if it doesn't exist
        if not os.path.exists(normalize_path(".//admins.csv")):
            with open(normalize_path(".//admins.csv"), "x", encoding="utf8") as database:
                writer = csv.writer(database)
                writer.writerow("ID,Name".split(','))
                self.admins = open(normalize_path(".//admins.csv"), encoding="utf8")
        else:
            self.admins = open(normalize_path(".//admins.csv"), encoding="utf8")

        if not os.path.exists(normalize_path(".//.//archived.csv")):
            with open(normalize_path(".//archived.csv"), "x", encoding="utf8") as database:
                writer = csv.writer(database)
                writer.writerow(
                    "ID,Name,Address,City,State,Zip,Classification," \
                    "Pay_Method,Salary,Hourly,Commission,Route,Account," \
                    "Birth_Date,SSN,Phone,Email,Start_Date,End_Date," \
                    "Title,Dept,Permission,Password".split(','))
                self.archived = open(".//archived.csv", encoding="utf8")
                
        else:
            self.archived = open(normalize_path(".//archived.csv"), 'r', encoding="utf8")
        self.emp_list = []
        self.admin_list = []
        self.archived_list = []
        self.update_emp_list()
        
    def update_emp_list(self):
        """
        Pulls data from the CSV to the emp list and archived emp list.
        Returns 0 if the function ran successfully, and -1 if there was an error.
        """
        try:
            arch_dict = csv.DictReader(self.archived)
            for row in arch_dict:
                temp_emp = Employee()
                temp_emp.populate_from_row(row)
                temp_emp.job_status = 'unactive'
                self.archived_list.append(temp_emp)
            
            emp_dict = csv.DictReader(self.database)
            for row in emp_dict:
                temp_emp = Employee()
                temp_emp.populate_from_row(row)
                if temp_emp not in self.archived_list:
                    temp_emp.job_status = 'active'
                    if temp_emp.permission == 'admin':
                        self.admin_list.append(temp_emp)
                    self.emp_list.append(temp_emp)
            
            return 0  # Return 0 to indicate success
        except Exception as e:
            print("An error occurred:", str(e))
            return -1  # Return -1 to indicate an error
                
    def archive_employee(self, id_num):
        """Removes from emp list and adds them to the archived file.
        """
        employee = find_employee_by_id(id_num, self.emp_list)
        employee.job_status = 'unactive'
        self.emp_list.remove(employee)
        self.archived_list.append(employee)
        _add_row(employee, normalize_path(".//archived.csv"))
        
    def unarchive_employee(self, id_num):
        temp_list = []
        employee = find_employee_by_id(id_num, self.archived_list)
        employee.job_status = 'active'
        self.archived_list.remove(employee)
        self.emp_list.append(employee)
        with open(normalize_path(".//archived.csv"), "r", encoding="utf8") as database:
            reader = csv.reader(database)
            for line in reader:
                if line[0] != str(id_num):
                    temp_list.append(line)
        with open(normalize_path(".//archived.csv"), 'w', newline='', encoding="utf8") as database:
            writer = csv.writer(database, delimiter=',')                   
            for employee in temp_list:
                writer.writerow(employee)
                
            
            


    def add_employee(self, employee: Employee):
        """
        Adds an employee to the employee list and adds a row to the csv file
        """
        employee.job_status = 'active'
        self.emp_list.append(employee)
        _add_row(employee, normalize_path(".//.//employees.csv"))

    def edit_employee(self, id_num, fields: list, data: list):
        """
        Edits an existing employee given ID, the fields you want to edit,
        and the data for those fields.
        Be careful if you edit things it really edits them in the DB
        while you're testing I would
        open("temp//employees.csv", "w",newline='') in on line 616
        of open("employees.csv", "w",newline='')
        """
        with open(normalize_path(".//employees.csv"), encoding="utf8") as database:
            emp_dict = csv.DictReader(database)
            temp = []
            for row in emp_dict:
                temp_row = row
                if temp_row["ID"] == str(id_num):
                    for index in range(len(fields)):
                        # Try passing on IndexErrors, to see what is happening with the data when that error is thrown. Exit loop?
                        # Print out fields and data lists.
                        temp_row[fields[index]] = data[index]
                temp.append(temp_row)
        with open(normalize_path(".//employees.csv"), "w", newline='', encoding="utf8") as temp_db:
            fieldnames = "ID,Name,Address,City,State,Zip,Classification," \
                         "Pay_Method,Salary,Hourly,Commission,Route,Account," \
                         "Birth_Date,SSN,Phone,Email,Start_Date,End_Date," \
                         "Title,Dept,Permission,Password".split(',')
            writer = csv.DictWriter(temp_db, fieldnames, )
            writer.writeheader()
            writer.writerows(temp)
            self.database = temp_db

            for employee in self.emp_list:
                if employee.id == id_num:
                    if fields[0] == "Pay_Method" and data[0] == 1:
                        employee.pay_method = DirectMethod(employee, data[1], data[2])
                    elif fields[0] == "Pay_Method" and data[0] == 2:
                        employee.pay_method = MailedMethod(employee)
                    elif fields[0] == "Classification" and data[0] == 1:
                        employee.classification = Hourly(data[1])
                    elif fields[0] == "Classification" and data[0] == 2:
                        employee.classification = Salary(data[1])
                    elif fields[0] == "Classification" and data[0] == 3:
                        employee.classification = Commissioned(data[1], data[2])
                    elif fields[0] == "Name":
                        full_name = data[0].split(' ')
                        first_name = full_name[0]
                        last_name = full_name[1]
                        setattr(employee, "first_name", first_name)
                        setattr(employee, "last_name", last_name)
                        setattr(employee, "name", data[0])
                    else:
                        for index in range(len(fields)):
                            setattr(employee, fields[index].lower(), data[index])


def _add_row(employee: Employee, file):
    with open(file, "a", newline='', encoding="utf8") as database:
        writer = csv.writer(database, delimiter=',')
        #if employee is hourly & direct deposit
        if str(employee.classification) == 'Hourly' and str(employee.pay_method) == 'Direct Deposit':
            var =  [-1,
                        employee.classification.hourly_rate, -1,
                        employee.pay_method.route_num,
                        employee.pay_method.account_num]
        #if employee is hourly & mail
        elif str(employee.classification) == 'Hourly' and str(employee.pay_method) == 'Mail':
            var = [-1,
                        employee.classification.hourly_rate, -1, -1, -1]
        #if employee is salary & direct deposit
        elif str(employee.classification) == 'Salary' and str(employee.pay_method) == 'Direct Deposit':
            var = [employee.classification.salary, -1, -1, 
                        employee.pay_method.route_num,
                        employee.pay_method.account_num]
        #if employee is salary & mail
        elif str(employee.classification) == 'Salary' and str(employee.pay_method) == 'Mail':
            var = [employee.classification.salary, -1, -1, -1, -1]
        #if employee is comissioned & direct deposit
        elif str(employee.classification) == 'Commissioned' and str(employee.pay_method) == 'Direct Deposit':
            var = [employee.classification.salary, -1,
                        employee.classification.commission_rate,
                        employee.pay_method.route_num,
                        employee.pay_method.account_num]
        #if employee is comissioned & mail
        elif str(employee.classification) == 'Commissioned' and str(employee.pay_method) == 'Mail':
            var = [employee.classification.salary, -1,
                        employee.classification.commission_rate, -1, -1]
    
        writer.writerow([employee.id, employee.name, employee.address,
                                 employee.city, employee.state, employee.zip,
                                 employee.classification.num(),
                                 employee.pay_method.num(),
                                 var[0],var[1],var[2],var[3],var[4],
                                 employee.birth_date, employee.ssn, employee.phone, employee.email, 
                                 employee.start_date, employee.end_date, employee.title, 
                                 employee.dept, employee.permission, employee.password])
      
           
def exportDB(employee,filePath):
    _add_row(employee, filePath)

def add_new_employee(emp_db: EmployeeDB, id_num, first_name, last_name,
                     address, city, state, zip_code, classification,
                     pay_method_num, birth_date, ssn, phone, email,
                     start_date, title, dept, permission, password,
                     route_num=0, account_num=0):
    """Creates a new employee given all of the necessary data, and adds
    that employee to the database, and writes them to the database file.
    """
    name = f'{first_name} {last_name}'
    employee = Employee(id_num, name, classification, birth_date,
                        ssn, phone, email, permission, password)

    employee.set_address(address, city, state, zip_code)
    employee.set_job(start_date, title, dept)
    employee.set_pay_method(pay_method_num, route_num, account_num)

    emp_db.add_employee(employee)
    return employee




def open_file(the_file):
    """Function to open a file"""
    os.system(the_file)


# emp_list should be a list of Employee objects.
def find_employee_by_id(employee_id, emp_list):
    """Finds an employee with the given ID in the given employee list, and
    returns it. Returns None if no employee has the given ID.
    Input: int, list of Employee objects
    Output: Employee object with matching id, or None.
    """
    for employee in emp_list:
        if employee.id == int(employee_id):
            return employee
    return None
