def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperature_C = 10
temperature_F = 17

converted_to_degrees = fahrenheit_to_celsius(temperature_C)
converted_to_fahrenheit = celsius_to_fahrenheit(temperature_F)
