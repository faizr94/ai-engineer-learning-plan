# you only need to try on the instance where the error is most likely to occur

"""
In this example, the ValueError happened first before x was assigned the value, resulting in the NameError where x is not defined
try:
    x = int(input ("What is x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")
"""


# The else block runs only when the conversion succeeds, so x is not used after a ValueError.
# The else clause is associated with the try clause and not the except
def main():
    x = get_int("What is x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            x = int(input (prompt))
        except ValueError:
            # print("x is not an integer")
            # Use pass to acknowledge the exception but not doing anything about it
            pass
        else:
            # return can not only break you out of the loop but also return a value for you
            return x

main()