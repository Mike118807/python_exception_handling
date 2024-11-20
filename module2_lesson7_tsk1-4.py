# Task 1-4 put together.

# Completed script:


def convert_to_celsius(fahrenheit):
    try:
        # Attempt to convert the input to float
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * 5/9 

    except ValueError:
        # Handle the case where the input is not a valid number
        print("Error: Please enter a valid number for the temperature.")
        
    else: 
        # If no exception occurs, print the converted temperature 
        print(f"{fahrenheit} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
        
    finally:
        # This block will always execute.
        print("Thank you for using the weather forecast application.")
        
        
def main():
    # Task 1: Ask the user to enter the temperature in Fahrenheit
    user_input = input("Enter the temperature in Fahrenheit: ")
    
    # Task 2 & 3: Convert the temperature and provide user-friendly output
    convert_to_celsius(user_input)
    
if __name__ == "__main__":
    main()

