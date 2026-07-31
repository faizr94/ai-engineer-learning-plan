# In the United States, it’s customary to leave a tip for your server after dining in a restaurant, typically an amount equal 
# to 15% or more of your meal’s cost. Not to worry, though, we’ve written a tip calculator for you, below!



def dollars_to_float(d):
    conv = float(d.lstrip("$"))
    return conv

def percent_to_float(p):
    conv = float(p.rstrip("%"))
    return conv/100

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


main()