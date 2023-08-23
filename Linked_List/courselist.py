"""This module implements CourseListADT to a full functioning linker class"""

from courselistADT import CourseListADT
from course import Course


class CourseList(CourseListADT):
    """Implementation of CourseListADT"""
    def __init__(self):
        self._head = None
        self._tail = None
        self.current_node = None
        self._node_count = 0


    def insert(self, course: Course): # pylint: disable=arguments-differ
        """Courses that get passed in will be linked in ascending order by course number"""
        if not isinstance(course, Course):
            raise TypeError("Course must be an instance of the Course class.")

        new_node = course

        if self._head is None:
            self._head = self._tail = new_node

        elif new_node.number() <= self._head.number():
            new_node.set_next(self._head)
            self._head.set_prev(new_node)
            self._head = new_node


        elif new_node.number() >= self._tail.number():
            new_node.set_prev(self._tail)
            self._tail.set_next(new_node)
            self._tail = new_node

        else:
            prev = None
            cur = self._head
            while cur is not None and cur.number() < new_node.number():
                prev = cur
                cur = cur.next()
            new_node.set_next(cur)
            new_node.set_prev(prev)
            prev.set_next(new_node)
            cur.set_prev(new_node)

        self._node_count += 1

    def remove(self, number: int):
        if not isinstance(number, int):
            raise TypeError("the parameter you passed in must be an integer!")

        if number == self._head.number():
            self._head.set_next(self._head.next())
            if self._head is not None:
                self._head.set_prev(None)
        elif number == self._tail.number():
            self._tail = self._tail.prev()
            if self._tail is not None:
                self._tail.set_next(None)
        else:
            cur = self.find(number)
            if cur is not None:
                cur.prev().set_next(cur.next())
                cur.next().set_prev(cur.prev())
        self._node_count -= 1

    def find(self, number: int):
        if not isinstance(number, int):
            raise TypeError("the parameter you passed in must be an integer!")

        # testing if number is closer to the head, or the tail - shortest path to course
        if abs(self._head.number() - number) < abs(self._tail.number() - number):
            cur = self._head
            while cur is not None and cur.number() != number:
                cur = cur.next()
        else:
            cur = self._tail
            while cur is not None and cur.number() != number:
                cur = cur.prev()
        return cur

    def clear(self):
        """empty linked list"""
        self._head = None
        self._tail = None
        self._node_count = 0

    def remove_all(self, number):
        while self.find(number):
            self.remove(number)

    def size(self):
        return self._node_count

    def calculate_gpa(self): # pylint: disable=arguments-differ
        if self.size() == 0:
            return 0

        grade_total = 0
        credit_hr_total = 0
        current = self._head

        while current is not None:
            grade_total += current.grade()*current.credit_hr()
            credit_hr_total += current.credit_hr()
            current = current.next()

        if credit_hr_total == 0:
            raise ZeroDivisionError("Total credit hours cannot be zero for GPA calculation.")

        total_gpa = grade_total / credit_hr_total
        return total_gpa

    def is_sorted(self): # pylint: disable=arguments-differ
        if self._head:
            cur = self._head
            while cur.next() is not None:
                if cur.next().number() < cur.number():
                    return False
                cur = cur.next()
        return True

    def __str__(self):
        course_strings = []
        current = self._head

        while current is not None:
            course_strings.append(str(current.course))
            current = current.next()

        return "\n".join(course_strings)

    def __iter__(self):
        self.current_node = self._head
        return self

    def __next__(self): # pylint: disable=arguments-differ
        if self.current_node is None:
            raise StopIteration
        self.current_node = self.current_node.next()
        return self.current_node
