class StudentManagementSystem:
        def __init__(self):
                self.students = {}

        def add_student(self, student_id, name, age, grade):
                self.students[student_id] = {'Name' : name, 'Age' : age, 'Grade' : grade}