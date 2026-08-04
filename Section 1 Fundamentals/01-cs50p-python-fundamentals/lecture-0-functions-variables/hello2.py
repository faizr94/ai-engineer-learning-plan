# `to` lets the caller decide who gets greeted; default makes the arg optional
def hello(to="world"):
    print("Hello", to)

hello()  # uses the default since no argument is passed
name = input("What is your name? ")
hello(name)