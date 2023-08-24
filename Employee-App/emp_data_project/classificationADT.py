class ClassificationADT:
    """Used for tracking the payment type and rate of an employee, and
    calculating how much they will be paid. An abstract class.
    """

    def __init__(self):
        """Initialize the abstract class.
        """

    def calculate_pay(self):
        """Calculates the employee's pay. Implemented differently in child
        classes based on payment type.
        """

    def __str__(self):
        """Returns the employee's payment type, i.e. the name of the
        class.
        """

    def num(self):
        """Returns an integer that represents the classification of the
        employee.
        """
        
class Hourly(ClassificationADT):
    """Used for tracking the payment rate of an hourly-paid employee, and
    to store the hours they've worked, and calculate their pay.
    """

    def __init__(self, hourly_rate):
        """Initialize the hourly employee's data members, with no
        timecards stored.
        """
        self.hourly_rate = float(hourly_rate)
        self.timecards = []

    def add_timecard(self, hours):
        """Adds the hours worked in a day to the hourly employee's
        timecards record.
        """
        self.timecards.append(hours)

    def calculate_pay(self):
        """Calculates the amount that will be paid to the hourly employee,
        hours worked x hourly rate.
        """
        payment = 0
        for hours in self.timecards:
            payment += hours * self.hourly_rate

        # Clear timecards so they are not reused.
        self.timecards = []

        return payment

    def __str__(self):
        """Returns a string representing employee's payment type.
        """
        return "Hourly"

    def num(self):
        """Returns an integer representing the hourly classification type.
        """
        return 1


class Salary(ClassificationADT):
    """Used to track the salary of a salaried employee, and to calculate
    their pay.
    """

    def __init__(self, salary):
        """Initialize the salaried employee's data members.
        """
        self.salary = float(salary)

    def calculate_pay(self):
        """Calculates the amount that will be paid to the salaried
        employee, 1/24th of their salary.
        """
        payment = self.salary / 24

        return payment

    def __str__(self):
        """Return's a string representing employee's payment type.
        """
        return "Salary"

    def num(self):
        """Returns an integer representing the salary classification type.
        """
        return 2


class Commissioned(Salary):
    """Used for tracking the salary of a commissioned employee and storing
    their commission rate and the commissions they've made. Also used to
    calculate their pay.
    """

    def __init__(self, salary, commission_rate):
        """Initialize the commissioned employee's data members, with no
        commission receipts stored.
        """
        super().__init__(salary)
        self.commission_rate = float(commission_rate)
        self.receipts = []

    def add_receipt(self, receipt):
        """Adds the number of commissions made in a day to the employee's
        receipts record.
        """
        self.receipts.append(receipt)

    def calculate_pay(self):
        """Calculates the amount that will be paid to the commissioned
        employee, 1/24th of their salary, and their commissions x
        commission rate.
        """
        payment = super().calculate_pay()
        for receipt in self.receipts:
            payment += self.commission_rate * receipt

        # Clear receipts so they are not reused.
        self.receipts = []

        return payment

    def __str__(self):
        """Return's a string representing employee's payment type.
        """
        return "Commissioned"

    def num(self):
        """Returns an integer representing the commissioned classification
        type.
        """
        return 3


def create_classification(class_num, pay_num_1: float, pay_num_2=0.0):
    """Creates an Hourly, Salary, or Commissioned class object based on
    the class_num, and assigns the proper data members.
    Input: pay_num_1 - a float representing hourly pay or salary,
                depending on the employee's classification.
           pay_num_2 - a float representing commissioned pay rate, used
                only for commissioned employees (class_num = 3).
    Output: Either an Hourly, Salary, or Commissioned class object.
    """
    if class_num == 1:
        return Hourly(pay_num_1)
    if class_num == 2:
        return Salary(pay_num_1)
    if class_num == 3:
        return Commissioned(pay_num_1, pay_num_2)

    raise Exception(f'Invalid classification number {class_num}. Should be 1, 2, or 3.')


class PayMethod():
    """Used to track an employee's payment method, and print an applicable
    message about how and how much they will be paid. An abstract class.
    """

    def __init__(self, employee):
        """Initialize data members.
        Input: Employee object ("employee" param)
        """
        # self.employee = " ".join([employee.first_name, employee.last_name])
        self.employee = employee

    def payment_message(self, amount):
        """Used to print an applicable message about how much employee
        will be paid, and in what method.
        """

    def num(self):
        """Returns an integer that represents the payment method in the
        data file.
        """


class DirectMethod(PayMethod):
    """Used for employees who opt to be paid by direct deposit. Stores
    their bank account information, and prints an applicable message about
    how much they will be paid via direct deposit on their next payday.
    """

    def __init__(self, employee, route_num, account_num):
        """Initialize data members for direct deposit. Keeps track of
        associated employee, their bank's routing number, and their bank
        account number.
        """
        super().__init__(employee)
        self.route_num = route_num
        self.account_num = account_num

    def payment_message(self, amount):
        """Used to print a message about how much the employee will be
        paid via direct deposit on their next payday.
        """
        return f'Will transfer ${amount:.2f} for {self.employee.name} to \
{self.route_num} at {self.account_num}'

    def __str__(self):
        """Returns a string representing the desired pay method.
        """
        return "Direct Deposit"

    def num(self):
        """Returns an integer that represents the direct pay method in the
        database file.
        """
        return 1


class MailedMethod(PayMethod):
    """Used for employees who opt to be paid by mail. Prints an applicable
    message about how much they will be paid via mail on their next
    payday.
    """

    def __init__(self, employee):
        """Initialize data members for mail method. Keeps track of the
        employee, and can access employee's mailing address.
        """
        super().__init__(employee)

    def payment_message(self, amount):
        """Used to print a message about how much the employee will be
        paid via mail on their next payday.
        """
        return f'Will mail ${amount:.2f} to {self.employee.name} at {self.employee.full_address()}'

    def __str__(self):
        """Returns a string representing the desired pay method.
        """
        return "Mail"

    def num(self):
        """Returns an integer that represents the mail pay method in the
        database file.
        """
        return 2


def create_pay_method(employee, pay_method_num, route_num=0,
                      account_num=0):
    """Creates an DirectMethod or MailedMethod class object based on the
    pay_method_num, and assigns the proper data members.
    Input: employee - an employee class object that the pay method will be
                tied to.
           route_num - a string representing the employee's bank routing
                number, used only if they're using DirectMethod
                (pay_method_num = 1).
           account_num - a string representing the employee's account
                number, used only if they're using DirectMethod
                (pay_method_num = 1).
    Output: Either a DirectMethod or MailedMethod class object.
    """
    if pay_method_num == 1:
        return DirectMethod(employee, route_num, account_num)
    if pay_method_num == 2:
        return MailedMethod(employee)

    raise Exception(f'Invalid pay method number {pay_method_num}. Should be 1 or 2.')