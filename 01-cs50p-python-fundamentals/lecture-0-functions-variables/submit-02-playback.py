# In a file called playback.py, implement a program in Python that prompts the user 
# for input and then outputs that same input, replacing each space with ... 
# (i.e., three periods
def playback():
    user_input = input("What do you want to say? ")
    split_input = user_input.split()
    print(*split_input, sep="...")
    
playback()