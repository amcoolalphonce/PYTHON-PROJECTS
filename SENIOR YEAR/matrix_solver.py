print("Matrix Solution Finder")
row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))
matrix = []

for i in range(row):
    row_numbers = []
    for j in range(column):
        number = float(input(f"Enter the number for matrix[{i + 1}][{j + 1}]: "))
        row_numbers.append(number)
    matrix.append(row_numbers)
