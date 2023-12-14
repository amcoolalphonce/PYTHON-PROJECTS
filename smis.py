class StudentManagementSystem:
        def __init__(self):
                self.students = {}

        def add_student(self, student_id, name, age, grade):
                self.students[student_id] = {'Name' : name, 'Age' : age, 'Grade' : grade}

        def view_student(self, student_id):
                if student_id in self.students:
                        student_info = self.students[student_id]
                        if name :
                                student_info['Nmae'] = name
                        if age:
                                student_info['Age'] = age
                        if grade:
                                student_info['Grade'] = grade
                        else:
                                print(f'Student with ID {student_id} updated successfully.')

        
        def delete_student(self, student_id):
                if student_id in self.students:
                        del self.students[student_id]