# In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the 
# equivalent number of Joules as an integer. Assume that the user will input an integer.

def joules_conv(mass):
    c2 = 300000000*300000000
    return mass*c2

def main():
    user_input = int(input("Insert mass: "))
    result = joules_conv(user_input)
    print(f"{result:,}")

main()