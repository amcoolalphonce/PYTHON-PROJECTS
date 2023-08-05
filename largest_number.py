def find_max(numbers):
    largest=numbers[0]
    for each in numbers:
        if each> largest:
            largest=each
    return largest
    

numbers=[23, 45, 63, 100]
largest=find_max(numbers)
print(largest)