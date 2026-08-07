"""
One of the most popular places to eat in Harvard Square is Felipe’s Taqueria, which offers a menu of entrees, per the dict below, wherein the value of each key is a price in dollars:

{
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


In a file called taqueria.py, implement a program that enables a user to place an order, prompting them for items, one per line, 
until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, display the 
total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. 
Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.
"""

"""
Steps Needed:
1) Prompt user for their order
2) Store the cost of the order placed 
3) Continue the loop and each time keep adding the total cost of orders
4) User will exit program on their own 

-> What kind of exceptions do we need to handle?
1. ValueError? 
2. EOFError (use to detect when the user input control-d)
"""


menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Original

# def order():
#     value = 0.0
#     while True:
#         try:
#             user_order = input("Item: ").strip().title()
#         except EOFError:
#             print()
#             break
#             # return ""
#             pass
#         else: 
#             # For each "key" in the menu dictionary
#             for food in menu:
#                 # If the user input matches the "key"
#                 if user_order == food:
#                     # We add in the "value" of the key that matched
#                     value += menu[user_order]
#                     print(f"Total: ${value:.2f}")

            
# 1) check order input
def check_order():
    try:
        user_order = input("Item: ").strip().title()
        menu[user_order]
    except EOFError:
        return "end of input"
    except KeyError:
        return "invalid order"
    else:
        return user_order

def main():
    total_price = 0
    while True:
        food = check_order()
        if food == "end of input":
            break
        elif food == "invalid order":
            continue
        else:
            total_price += menu[food]
            print(f"Total: ${total_price:.2f}")
main()