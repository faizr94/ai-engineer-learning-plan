# In a file called indoor.py, implement a program in Python that prompts the user for input 
# and then outputs that same input in lowercase. Punctuation and whitespace should 
# be outputted unchanged. You’re welcome, but not required, to prompt the user 
# explicitly, as by passing a str of your own as an argument to input
def inside_voice():
    user_input = input("What do you want to say? ")
    print(user_input.lower())
    
inside_voice()