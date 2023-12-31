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
                for student_id, student_info in self.students.items():
                        print(f'Student ID: {student_id}, Name : {student_info['Name'] }')


#USAGE OF THESE FUNCTIONS IS AS ILLUSTRATED BELOW
student_system = StudentManagementSystem()

student_system.add_student(101, 'John Doe', 18, 'A')
student_system.add_student(102, 'Jane Smith', 17, 'B')

student_system.display_all_students()

student_system.view_student(101)

student_system.update_student(101, age=19)

student_system.view_student(101)

student_system.delete_student(102)

student_system.display_all_students()