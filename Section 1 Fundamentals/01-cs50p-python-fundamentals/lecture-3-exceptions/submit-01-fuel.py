"""
Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 
1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, 
wherein X is a non-negative integer and Y is a positive integer, and then outputs, as a percentage rounded to the nearest integer, 
how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. 
And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. 
(It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""

def main():
    result = fuel_convert()
    if result <= 1:
        print("E")
    elif result >= 99:
        print("F")
    else:
        print(f"{result}%")
    
# Division occurs at this step
# Check if denominator is 0, if 0 then should raise the ZeroDivision Error
def fuel_convert():
    """
    1) Performs the math to safely divide the user input, accepting 2 params
    2) Returns result to the nearest integer
    """
    x,y = fuel_check()
    result = round((x/y)*100)
    return result


# Check if our input can be converted to an integer
# Check if the numerator > denominator
def fuel_check():
    while True:
        try:
            fuel = input("Fraction: ")
            fuel_split = fuel.split("/")
            numerator = int(fuel_split[0])
            denominator = int(fuel_split[1])
            if numerator > denominator or numerator < 0:
                raise ValueError()
            if denominator == 0:
                raise ZeroDivisionError()
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            return numerator, denominator

main()