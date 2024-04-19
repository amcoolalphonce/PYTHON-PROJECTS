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

# Forward elimination
for i in range(row - 1): 
    pivot_row = i
    while pivot_row < row and matrix[pivot_row][i] == 0:
        pivot_row += 1
    if pivot_row == row:
        print("No unique solution exists")
        exit()
