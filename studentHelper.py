class Student:

   def __init__(self,name,idIE,email):
        self.name = name
        self.__idIE = idIE
        self.email = email
        self._grades = {}

   def getName(self):
        return self.name

   def setName(self,name):
       self.name = name

   def getEmail(self):
        return self.email

   def getGrades(self):
        return self._grades

   def setGrade(self,course,grade):
        self._grades[course]=grade

   def getGrade(self,course):
       return self._grades[course]

   def getId(self):
       return self.__idIE

   def clearGrades(self):
       self._grades = {}

   def __str__(self):
       return self.getName()