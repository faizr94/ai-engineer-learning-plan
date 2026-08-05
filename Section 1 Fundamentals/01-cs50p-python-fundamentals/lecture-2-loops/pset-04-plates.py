"""
In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. 
Among the requirements, though, are:

- “All vanity plates must start with at least two letters.”
- “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
- “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; 
    AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
- “No periods, spaces, or punctuation marks are allowed.”

In plates.py, implement a program that prompts the user for a vanity plate and then output 
Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. 
Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. 
Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
"""

#script below works but alot of room for improvement
# go see how this should be solved

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
        
def is_valid(s):
    if not start_length(s):
        return False
    if not number_end(s):
        return False
    if not first_number(s):
        return False
    if not punc(s):
        return False
    
    return True
        
# criteria 1: must start with two letters
# criteria 2: a max of 6 characters and a min of 2 characters. either letters or numbers or both
def start_length(s):
    c1 = s[0:2]
    if c1.isalpha() and 2 <= len(s) <= 6:
        return True
    else:
        return False

# criteria 3: numbers can only be at the end. 
def number_end(s):
    found_number = False
    for char in s:
        if char.isdigit():
            found_number = True
        elif char.isalpha() and found_number:
            return False
    if found_number == False and s.isalpha() == True:
        return True
    else:
        return found_number

# criteria 4: first number used cannot be a '0'
def first_number(s):
    number = []
    for char in s:
        if char.isdigit():
            number.append(char)
    if len(number) > 0 and number[0] == '0':
        return False
    else:
        return True
    
# criteria 4: no period, spaces or punctuation allowed
def punc(s):
    if s.isalnum():
        return True
    else:
        return False

main()


