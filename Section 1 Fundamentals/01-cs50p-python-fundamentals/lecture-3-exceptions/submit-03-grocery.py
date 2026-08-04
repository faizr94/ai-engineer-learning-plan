"""
Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). 
Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. 
Treat the user’s input case-insensitively.
"""

grocery_list = {}


def main():
    print()
    while True:
        x = check_input()
        if x == "end of input":
            print()
            break
        else:
            update_list(x)
    print(dict_sort())
            # continue

# 1. Get user input and check for EOFError
def check_input():
    try:
        item = input("").upper()
    except EOFError:
        return "end of input"
    else:
        return item

# 2. Add item to dictionary as a key
def update_list(food):
    if food in grocery_list:
        grocery_list[food] += 1
    else:
        grocery_list[food] = 1
        
        
# 3. sort items in dictionary in ascending order and return as value, key 
def dict_sort():
    result = ""
    ascending = sorted(grocery_list.items())
    for i in ascending:
        result += f"{i[1]} {i[0]}\n"
    return result
    
main()