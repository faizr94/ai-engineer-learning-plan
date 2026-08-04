# using f strings to combine input and outputting the stored variable in print
# trimming whitespace and capitalize the user input using string methods
name = input("What is your name? ").title().strip()


#split user's name into first name and last name
first, last = name.split()

# say hello
print(f"Hello {last}!")


# named parameters
# print("Hello, ", end="")
# print(name)

#escape characters
# print("hello, \"friend\"")