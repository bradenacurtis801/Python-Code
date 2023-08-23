from abc import ABC, abstractclassmethod
class CourseListADT:
    """Abstract Data Type For CourseList"""
    @abstractclassmethod
    def __init__(self):
        """constructor to initialize all needed data for an empty list"""
        pass
    @abstractclassmethod
    def insert(self, Course):
        """insert the specified Course in Course Number ascending order"""
        pass
    
    def remove(self, number):
        """remove the first occurrence of the specified Course"""
        pass
    
    def remove_all(self, number):
        """removes ALL occurrences of the specified Course"""
        pass
    
    def find(self, number):
        """find the first occurrance of the specified course in the list or return -1"""
        pass
    
    def size(self):
        """return the number of items in the list"""
        pass
    
    def calculate_gpa():
        """return the GPA using all courses in the list"""
        pass
    
    def is_sorted():
        """return True if the list is sorted by Course Number, False otherwise"""
        pass
   
    def __str__():
        """returns a string with each Course's data on a separate line"""
        pass
   
    def __iter__():
        pass
    
    def __next__():
        pass