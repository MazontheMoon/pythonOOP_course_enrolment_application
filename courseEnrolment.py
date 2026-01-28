'''
SD-GAL-05 SD-TA-007 Exercise 013
Author: Mary Ronan
Last Modified: 28/01/2026
A Course Enrolment System with OOP Python and Unit Tests
'''

# Required imports
from abc import ABC, abstractmethod
import unittest

# Parent Class
class Course (ABC):

    # Class Instance
    def __init__(self, courseName, coursePrice, courseStartDate, studentQty):
        self.courseName = courseName
        self.coursePrice = coursePrice
        self.courseStartDate = courseStartDate
        self.studentQty = studentQty

    # Class Getter Functions
    def getCourseName(self):
        return self.courseName

    def getCoursePrice(self):
        return self.coursePrice

    def getCourseStartDate(self):
        return self.courseStartDate

    def getStudentQty(self):
        return self.studentQty

    # Display Welcome Message
    def displayWelcomeMessage():
        print("=".ljust(55, "="))
        print("Welcome to GTIs Course Enrolment Application".center(50))
        print("=".ljust(55, "="))

    # Display Exit Message
    def displayExitMessage():
        print("=".ljust(55, "="))
        print("Thank you for using GTIs Course Enrolment Application".center(50))
        print("=".ljust(55, "="))

    # Abstract Methods
    @abstractmethod
    def calcTotalIncome(self):
        pass
    
    @abstractmethod
    def printCourseEnrolment(self):
        pass

class Online(Course):

    # Class Instance
    def __init__(self, courseName, coursePrice, courseStartDate, studentQty):
        super().__init__(courseName, coursePrice, courseStartDate, studentQty)

    # Class Setter Function
    def setCourseUrl(self):
        self.courseUrl = input(f"Enter URL of {self.courseName}:")

    # Class Getter Functions
    def getCourseUrl(self):
        return self.courseUrl

    # Calculate Total Income
    def calcTotalIncome(self):
        return self.coursePrice * self.studentQty

    # Display Course Enrolment
    def printCourseEnrolment(self):
        print("-".ljust(55, "-"))
        print("GTI Online Course Enrolment".center(50))
        print("-".ljust(55, "-"))
        print("Course Name".ljust(25),": ", self.getCourseName())
        print("Course Price".ljust(25),":  €", self.getCoursePrice())
        print("Course Start Date".ljust(25),": ", self.getCourseStartDate())
        print("Number of Participants".ljust(25),": ", self.getStudentQty())
        print("Course URL".ljust(25),": ", self.getCourseUrl())
        print("*".ljust(55, "*"))
        print("Total Income".ljust(25),": €", self.calcTotalIncome())
        print("-".ljust(55, "-"))

# Child Class
class Inhouse(Course):

    # Class Variables
    insurancePremium = 100.00

    # Class Instance
    def __init__(self, courseName, coursePrice, courseStartDate, studentQty):
        super().__init__(courseName, coursePrice, courseStartDate, studentQty)

    # Calculate Total Income
    def calcTotalIncome(self):
        return (self.coursePrice + self.insurancePremium)* self.studentQty

    # Display Course Enrolment
    def printCourseEnrolment(self):
        print("-".ljust(55, "-"))
        print("GTI Inhouse Course Enrolment".center(50))
        print("-".ljust(55, "-"))
        print("Course Name".ljust(25),":", self.getCourseName())
        print("Course Price".ljust(25),":  €", self.getCoursePrice())
        print("Course Start Date".ljust(25),":", self.getCourseStartDate())
        print("Number of Participants".ljust(25),":", self.getStudentQty())
        print("*".ljust(55, "*"))
        print("Total Income".ljust(25),": €", self.calcTotalIncome())
        print("-".ljust(55, "-"))

# MAIN PROGRAM

# Display Welcome
Course.displayWelcomeMessage()

# Get User Input
courseType = input("Enter Course Type ('O' for Online or 'I' for Inhouse):").upper()
courseName = input("Enter Name of Course: ")
coursePrice = float(input(f"Enter Price of {courseName}: €"))
courseStartDate = input(f"Enter Start Date of {courseName}:")
studentQty = int(input(f"Enter Number of Students for {courseName}:"))

# Create COurse Enrolment
if courseType == "O":
    course = Online(courseName, coursePrice, courseStartDate, studentQty)
    course.setCourseUrl()
    course.printCourseEnrolment()
else:
    course = Inhouse(courseName, coursePrice, courseStartDate, studentQty)
    course.printCourseEnrolment()
    
# Display Exit Message
Course.displayExitMessage()
