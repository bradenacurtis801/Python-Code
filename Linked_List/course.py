"""
This module defines the Course class for managing course information.
"""
from courseADT import CourseADT
class Course(CourseADT):
    """ Course ADT Class """
    # pylint: disable=too-many-arguments
    def __init__(self, number: int = 0, name: str = "",
                 credit_hr: float = 0.0,
                 grade: float = 0.0, dept: str = ""):
        if not isinstance(number, int) or number < 0:
            raise ValueError
        if not isinstance(name, str):
            raise ValueError
        if not isinstance(credit_hr, float) or credit_hr < 0:
            raise ValueError
        if not isinstance(grade, float) or grade < 0:
            raise ValueError
        self._dept = dept
        self._number = number
        self._name = name
        self._credit_hour = credit_hr
        self._grade = grade
        self._next = None
        self._prev = None

    def next(self): # pylint: disable=arguments-differ
        """returns the next node"""
        return self._next

    def prev(self): # pylint: disable=arguments-differ
        """returns the next node"""
        return self._prev

    def set_next(self, val):
        """setter for _next private attribute"""
        self._next = val

    def set_prev(self, val):
        """setter for _prev private attribute"""
        self._prev = val

    def dept(self): # pylint: disable=arguments-differ
        """OPTIONAL"""
        return self._dept

    def number(self): # pylint: disable=arguments-differ
        return self._number

    def name(self): # pylint: disable=arguments-differ
        return self._name

    def credit_hr(self): # pylint: disable=arguments-differ
        return self._credit_hour

    def grade(self): # pylint: disable=arguments-differ
        return self._grade

    def __str__(self): # pylint: disable=arguments-differ
        return f"{self._dept}{self._number} {self._name} \
               Grade: {self._grade} Credit Hours: {self._credit_hour}"