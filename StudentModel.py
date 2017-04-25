"""
Below is the model which will take care of the translation between the data source and the controller
"""

import studentHelper

class StudentModel(object):

#Class variables to keep track of:
    # course names and grades
    courses = {}
    #sudents list containing student objects
    students = []
    #list with student IDs
    studentIDs = []
    #total (sum) of grades
    total = 0
    #count of students
    count = 0

    def __init__(self, file):
        self.file = file

#Function which will:
    #read a file and split the lines
    #read the name, id and grade and store them as part of a student object
        #Add the newly create object to the student list class variable
        #Add the id to the studentIDs class variable,
    #read the course and grade, increment the total number of users and increase the sum of grades
    def readFile(self):
        with open(self.file) as f:
            lines = f.read().splitlines()
            for l in lines:
                line = l.split(",")
                if len(line) == 2:
                    studentInfo = line[1].split("*")
                    #Create student object
                    stud = studentHelper.Student(studentInfo[0], studentInfo[1].lower(), studentInfo[2])
                    #Append student ID to the Student Ids list
                    StudentModel.studentIDs.append(studentInfo[1].lower())
                    #Append student object to the student list
                    StudentModel.students.append(stud)
                else:
                    #Retrieve course and grade
                    courseAndGrade = l.split("*")
                    #Convert them to lower to deal with case sensitive cases
                    course = courseAndGrade[0].lower()
                    #Convert the grade to float
                    grade = float(courseAndGrade[1])
                    #Add the grade to the total
                    StudentModel.total += grade
                    #Increment the student count
                    StudentModel.count += 1
                    #Add course and grade to the course dictionary
                    self.addCourseGrade(course, grade)
                    #Set the student grade for this course
                    stud.setGrade(course, grade)

#helper method to Load a student by id
    def loadStudent(self, id):
        for student in StudentModel.students:
            if student.getId() == id:
                return student

#helper method to add course grade to the courses dictionary:
        #If the course is already there, add the grade to the list.
        # If not, create a new dictionary  with the course as key and the grade as value.
    def addCourseGrade(self, course, grade):
        if course not in StudentModel.courses:
            StudentModel.courses[course] = [grade]
        else:
            StudentModel.courses[course].append(grade)

