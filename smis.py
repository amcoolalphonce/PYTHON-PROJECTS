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
                        print(f'Student with ID {student_id} updated successfully.')
                else:
                        print(f'Student with ID {student_id}  not found.')

        
        def delete_student(self, student_id):
                if student_id in self.students:
                        del self.students[student_id]
                        print(f'Student with ID {student_id} deleted successfully')
                else:
                        print(f'Student with ID {student_id} not found.')


        def display_all_students(self):
                print("All students")