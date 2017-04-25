"""
Group C's MVC Assignment

Below is the Controller which will take care of the system functionalities

Student Controller class.
Responsible for:
- Calculating the average grade of any student given his id.
- Calculating the class average
- Calculating the average per course
"""

import StudentModel as mod

class studentControl:

    def __init__(self, mod):
        self.model = mod

#Function to get the average for a student given his ID.
    #The function also handles several IDs.
    def getAvgById(self, *ids):
        values = []
        #If we are passed several ids:
        for idIE in ids:
            tot = 0
            if idIE.lower().strip() in self.model.studentIDs:
                #Load the student using the model's loadStudent method
                student = self.model.loadStudent(idIE.lower().strip())
                #Get all grades for this student
                grades = student.getGrades()
                #Get the total of grades for this student
                for g in grades:
                    tot += grades[g]
                #Calculate the average
                average = tot/len(grades)
                #Get the name of the student
                name = student.getName()
                str = "The average for Student {0},{1}, is {2:.3f}"
                message = str.format(idIE, name, average)
                values.append(message)
            #Warn user if the id is not part of the student ids list
            else:
                str = "The ID {0} is not part of the student IDs"
                message = str.format(idIE)
                values.append(message)
        return values

#Function to calculate the class average accessing directly the class variables of the model
    def classAvg(self):
        return self.model.total / self.model.count

#Get the course average:
    #The function also handles several courses,
    def getAvgPerCourse(self, *courses):
        courseList = []
        #If we are passed several courses:
        for course in courses:
            if course.lower().strip() in self.model.courses:
                #get the grades for this course
                thisCourseList = self.model.courses[course.lower().strip()]
                #calculate the average of grades
                value = sum(thisCourseList)/len(thisCourseList)
                str = "The average for the {0} course is {1:.3f}"
                message = str.format(course, value)
                courseList.append(message)
            else:
                #Notify the user that the course is not part the courses
                str = "The course {0} is not part of the courses. " \
                      "Available courses are:"
                message = str.format(course)
                courseList.append(message)
                #Add the avaailble courses to display them to the user
                for key in self.model.courses:
                    courseList.append(key)
        return courseList