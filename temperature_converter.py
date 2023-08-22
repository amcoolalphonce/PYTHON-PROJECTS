def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperature_C = 10
temperature_F = 17

converted_to_celsius = fahrenheit_to_celsius(temperature_C)
converted_to_fahrenheit = celsius_to_fahrenheit(temperature_F)


print(f"{temperature_F} degrees Fahrenheit is {converted_to_celsius:.2f} degrees Celsius.")
print(f"{temperature_C} degrees Celsius is {converted_to_fahrenheit:.2f} degrees Fahrenheit.")

#now work on query input from user and if the user and ask which conversion they want to perform eg if F ; do q etc