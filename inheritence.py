#creating a class
class University:
    #class variables
    school_name = "alexandria university"

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + last +"@gmail.com"
    #performing actions
    def get_fullname(self):
        return "{} {}".format(self.first, self.last)
    def school(self):
        return self.school_name
    
class Student(University):
    num_students = 0
    def __init__(self, first, last, gpa, id):
        super().__init__(first, last)
        self.gpa =gpa
        self.id = id
        Student.num_students +=1
    def is_honors(self):
        return self.gpa >= 3.5
    
class Professors(University): #
    def __init__(self, first, last, pay, courses = None):
        super().__init__(first, last) #
        self.pay = pay
        if courses is None:
            self.courses=[]
        else: 
            self.courses = courses
    def add_course(self, crs):
        if crs not in self.courses:
            self.courses.append(crs)


stud1 = Student("batoul", "salah", 3.1, 7705)
Prof1 = Professors("farouk", "ahmed", 5000, ["mechanics"])
print(stud1.get_fullname())
print(stud1.school())
# print(stud1.__dict__)
# print(Prof1.__dict__)
# Prof1.add_course("math")
# print(Prof1.courses)
# print(stud1.is_honors())
print(isinstance(stud1, Professors)) #output: False
print(issubclass(Student, University)) #output: True











