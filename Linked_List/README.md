This is an application which stores the courses taken by a student and prints out a report. 
Data will be read from a data.txt file. Once all data has been read from the data.txt file, 
the program prints a report as shown in the Program Output section below. 
After the list of courses has been printed, you should then calculate and display the 
cumulative GPA of all courses in the list.



**Program Example Output**

```temp.py
import random
from courselist import CourseList
from course import Course

random.seed(0)
cl = CourseList()
courseNumbers = []
for _ in range(37):
    courseNumbers.append(random.randrange(1000, 7000))
for number in courseNumbers:
    cl.insert(Course(number, "test", 1.0, 2.0))
    
print(cl)
```
```bash
PS C:\Users\Braden\OneDrive\Homework Documents\Spring 2022\CS 2420\Project3\Project3Code\revisedVersion>      & C:/Python311/python.exe "c:/Users/Braden/OneDrive/Homework Documents/Spring 2022/CS 2420/Project3/Project3Code/revisedVersion/temp.py"
Current List: (37)
1331 test Grade: 2.0 Credit Hours: 1.0
1604 test Grade: 2.0 Credit Hours: 1.0
1776 test Grade: 2.0 Credit Hours: 1.0
1809 test Grade: 2.0 Credit Hours: 1.0
1824 test Grade: 2.0 Credit Hours: 1.0
2140 test Grade: 2.0 Credit Hours: 1.0
2144 test Grade: 2.0 Credit Hours: 1.0
```

## STAR Method Breakdown:

### Situation: 

During the course of the project, I was tasked with creating an application that manages and reports on student course data 
tored in a linked list. My goal was to read course data from a file, organize it using OOP principles and a linked list 
implementation, and generate a report containing the course information and cumulative GPA.

### Task: 

My specific task was to implement two separate modules: course.py and courselist.py, each containing classes that contribute to 
the overall functionality of the application. The Course class in course.py needed to provide methods for retrieving course details 
and formatting course information as a string. The CourseList class in courselist.py had to implement methods for managing courses 
in a linked list, including insertion, removal, finding, size calculation, GPA calculation, and sorting verification.

### Action:

I approached the project by first creating the Course class with appropriate methods for retrieving and formatting course details. 
I implemented parameter validation and default values in the constructor. Next, I worked on the CourseList class, using a linked list 
data structure to manage courses. I implemented methods for inserting, removing, finding, and calculating statistics like size and
GPA. Additionally, I ensured the list's sorting was verified with the is_sorted() method.

### Result:

As a result of my efforts, I successfully created the Course and CourseList classes with the required methods and functionality. 
The application was able to read course data from a file, organize it using the linked list structure, and generate a report that 
displayed course information for each student. The cumulative GPA was accurately calculated based on the provided grading scale. 
My code adhered to the specified coding style and earned a good score in the pylint assessment.


## Running Tests with Pytest
To test the implementation of class definitions, methods, and attributes, use the test_linked_list.py file. Use the following 
command to run the tests using pytest:

```bash
pytest ./test_linked_list.py
```

The test session will start, and pytest will execute the test cases defined in test_linked_list.py. You should see a summary 
of passed tests and the overall test results.

Make sure you have pytest and pylint installed. If not, you can install it using the following command:

```bash
pip install pytest pylint
```

Remember to run these tests to ensure that your linked list implementation is working as expected.

## Example Output from pytest:

```bash
PS C:\Users\Braden\OneDrive\Homework Documents\Spring 2022\CS 2420\Project3\Project3Code\revisedVersion> pytest .\test_linked_list.py                                                              
===================== test session starts ======================
platform win32 -- Python 3.11.4, pytest-7.4.0, pluggy-1.2.0      
rootdir: C:\Users\Braden\OneDrive\Homework Documents\Spring 2022\CS 2420\Project3\Project3Code\revisedVersion
collected 9 items                                                

test_linked_list.py .........                             [100%]

====================== 9 passed in 0.58s =======================
```


