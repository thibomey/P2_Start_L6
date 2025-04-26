from student import Student

class Klaslokaal:
    def __init__(self):
        self.studenten = []
    def voeg_student_toe(self, student):
        self.studenten.append(student)
    def toon_studenten (self):
        for student in self.studenten:
            student.stel_voor()

student1 = Student("Thibo", "14")
student2 = Student("Jacob", "85")

Klaslokaal1 = Klaslokaal()
Klaslokaal1.voeg_student_toe(student1)
Klaslokaal1.toon_studenten()

Klaslokaal2 = Klaslokaal()
Klaslokaal2.voeg_student_toe(student2)
Klaslokaal2.toon_studenten()