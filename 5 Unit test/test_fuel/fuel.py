def main():
    while True:
        try:
            # Prompt the user to input a fraction
            Fraction = input("Fraction: ")
            # Convert the fraction to a percentage
            percentage = convert(Fraction)
            break  # Exit the loop if conversion is successful
        except (ValueError, ZeroDivisionError):
            # Ignore invalid inputs and prompt again
            pass
    # Print the gauge reading based on the percentage
    print(guage(percentage))

def guage(percentage):
    # Determine the gauge reading based on the percentage
    if percentage <= 1:
        return "E"  # Empty
    elif percentage < 99:
        return f"{round(percentage)}%"  # Percentage between 1 and 99
    else:
        return "F"  # Full

def convert(Fraction):
    # Split the fraction into numerator and denominator
    x, y = Fraction.split("/")
    x, y = int(x), int(y)  # Convert to integers
    try:
        if x > y and y != 0:
            raise ValueError  # Raise an error if the numerator is greater than the denominator
        if y == 0:
            raise ZeroDivisionError  # Raise an error if the denominator is zero
        return (x / y) * 100  # Return the percentage
    except (ValueError, ZeroDivisionError):
        raise  # Re-raise the error to be handled by the main function

# Ensure the main function is called only when the script is executed directly
if __name__ == "__main__":
    main()
