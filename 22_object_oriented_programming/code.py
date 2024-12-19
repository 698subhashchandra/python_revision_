# student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}
#
#
# def average(sequence):
#     return sum(sequence) / len(sequence)
#
# print(average(student["grades"]))



#############################
# class Student:
#     def __init__(self):
#         self.name = "Rolf"
#         self.grades =  (89, 490, 93, 78, 90)
#
#     def average(self):
#         return sum(self.grades) / len(self.grades)
#
# student = Student()
# print(student.average())
# print(student.name)
# print(student.grades)

#############################
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", (100, 100, 93, 78, 90))
student2 = Student("Rolf", (1, 100, 93, 78, 90))
student3 = Student("Atul", (100, 100, 200, 100, 100))

print(student.average())
print(student2.average())
print(student3.average())
