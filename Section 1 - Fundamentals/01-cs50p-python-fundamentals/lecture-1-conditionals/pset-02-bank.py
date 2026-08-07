# In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. 
# If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. 
# Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

def main():
    greeting = input("Greeting: ").strip().lower()
    if first_five(greeting) == True:
        print("$0")
    # elif greeting[0] == "h" and not first_five(greeting):
    elif greeting[0] == "h" and first_five(greeting) == False:
        print("$20")
    else:
        print("$100")

def first_five(greeting):
    return greeting.startswith("hello", 0,5)
    
main()

# greeting = "hello, newman"
# print(greeting.startswith("hello", 0,4))