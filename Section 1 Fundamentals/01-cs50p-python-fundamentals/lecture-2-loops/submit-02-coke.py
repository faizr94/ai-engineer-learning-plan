"""
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. 
Once the user has inputted at least 50 cents, output how many cents in change the user is owed. 
Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
"""

def validate_coin(x):
    if x in (25, 10, 5):
        return True
    else:
        return False
    
def calculate_change(user_coins):
    coke = 50
    if user_coins >= 50:
        change = user_coins - coke
        return change
    else:
        return 0
    
def main():
    coke = 50
    user_coins = 0
    
    while user_coins < 50:
        print(f"Amount Due: {coke}")
        insert_coin = int(input("Insert Coin: "))
        if validate_coin(insert_coin) is True:
            user_coins += insert_coin
            coke -= insert_coin
    change = calculate_change(user_coins)
    print(f"Change Owed: {change}")
    
main()