"""
Temperature Conversion
Create a function that converts temperatures between Celsius, Fahrenheit, and Kelvin.
It should take two arguments: the temperature and the current scale,
and return the temperature in all three scales.
"""

def convert_temperature(temp, scale):
    # Your code here
    if scale == 'celsius':
        celsius = temp
        fahrenheit = (9/5) * temp + 32
        kelvin = temp + 273.15
    elif scale == 'kelvin':
        kelvin = temp
        celsius = temp - 273.15
        fahrenheit = (temp - 273.15) * (9/5) + 32
    elif scale == 'fahrenheit':
        fahrenheit = temp
        celsius = (temp - 32) * (5/9)
        kelvin = (temp - 32) * (5/9) + 273.15
    else:
        raise ValueError("Invalid scale. Use 'celsius', 'fahrenheit', or 'kelvin'.")

    return celsius, fahrenheit, kelvin