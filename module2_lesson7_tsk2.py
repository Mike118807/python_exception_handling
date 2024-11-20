# convert the Fahrenheit temperature to Celsius. Use a try block to catch any potential
# errors during the conversion process.


def convert_to_celsius(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * 5/9
    
    except ValueError:
        print("Error: Please enter a valid number for the temperature. ")
    



