"""
Group C's MVC Assignment

Below is the view which will take care of the user interface
"""

import StudentModel as model
import studentController as controller


class View:

    def __init__(self, file):
        self.file = file

    #instantiate the model
    #read the file and instantiate the controller
    #Read user input
    def run(self):
        mod = model.StudentModel(self.file)
        mod.readFile()
        cont = controller.studentControl(mod)
        questions = """
        Press 0 to quit
        Press 1 to get class average
        Press 2 to get student average by ID
        Press 3 to get course average
        Enter your request:
        """
        userInput = input(questions)
        while True:
            try:
                answer = int(userInput)
                if answer == 1:
                    print("The class average is {:.3f} ".format(cont.classAvg()))
                    userInput = input(questions)
                elif answer == 2:
                    ids = input("Enter student ID: ")
                    ids = ids.split(',')
                    values = cont.getAvgById(*ids)
                    print(*values, sep='\n')
                    userInput = input(questions)
                elif answer == 3:
                    courseName = input("Enter course name: ")
                    courses = courseName.split(',')
                    values = cont.getAvgPerCourse(*courses)
                    print(*values, sep='\n')
                    userInput = input(questions)
                elif answer == 0:
                    print('See you Soon!')
                    break
                else:
                    print("Oops, wrong input. Please Enter a valid question ID:")
                    userInput = input(questions)
            except:
                    print("Oops, wrong input. Please Enter a valid question ID")
                    userInput = input(questions)

if __name__ == "__main__":
    view = View("StudentFile.txt")
    view.run()
