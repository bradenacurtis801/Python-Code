from abc import ABC, abstractclassmethod

"""OOP Abstraction Layer"""
"""Each method needs to be overridden in the implementation class"""
class CourseADT(ABC):
    """ Course ADT Class """
    @abstractclassmethod
    def __init__(self):
        """ must have default values for all parameters and must validate all parameters """
        pass
    @abstractclassmethod
    def number(self):
        """ retrieve Course Number as an integer """
        pass
    @abstractclassmethod
    def name(self):
        """ retrieve Course Name as a string """
        pass
    @abstractclassmethod
    def credit_hr(self):
        """ retrieve Credits as a floating-point number """
        pass
    @abstractclassmethod
    def grade(self):
        """ retrieve Grade as a numeric value in range 4.0 – 0.0 """
        pass
    @abstractclassmethod
    def __str__(self):
        """returns a string representing a single Course"""
        pass
    
