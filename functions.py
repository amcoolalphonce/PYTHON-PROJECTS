def greet(name):
        print("Hello", name)
        print("How do you do today?") 

#define a function first as shown above then call the function
greet("Amcool")


def add_numbers(num1, num2):
        result = num1 + num2
        return result

x = 100
y = 200
result = add_numbers(x, y)
print(result)

marks = [100, 25, 75, 50, 125, 200]
#get length
length = len(marks)
print(length)

#get sum
marks_sum = sum(marks)
print(marks_sum)