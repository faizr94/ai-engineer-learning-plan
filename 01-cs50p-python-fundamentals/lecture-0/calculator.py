# integers
# x = int(input("First number to add: "))
# y = int(input("Second number to add: "))

# float 
x = float(input("First number to add: "))
y = float(input("Second number to add: "))


# rounding to nearest int
# z = round(x + y)


#division to nearest decimal place
z = round(x / y, 2)

# can also use below for 2 dp
print(f"{z:.2f}")

# adding separators after every 1000
print(f"{z:,}")

