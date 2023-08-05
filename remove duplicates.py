prime_numbers = [3, 5,7, 3, 11, 13,19,23,23,19,29]
non = []
for numbers in prime_numbers:
    if numbers not in non:
        non.append(numbers)
print(non)