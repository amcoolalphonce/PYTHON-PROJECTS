#factorial of a number using recursion

num=int(input('ENTER A NUMBER WHOSE FACTORIAL YOU WANT'))
def factorial(x):
    if x==1:
        return 1
    else:
        return x +factorial(x-1)

print(factorial(num))