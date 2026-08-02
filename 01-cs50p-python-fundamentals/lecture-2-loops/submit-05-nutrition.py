"""
The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters that “show nutrition information for the 20 most frequently consumed raw fruits … in the United States. 
Retail stores are welcome to download the posters, print, display and/or distribute them to consumers in close proximity to the relevant foods in the stores.”

In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories 
in one portion of that fruit, per the FDA’s poster for fruits, which is also available as text. Capitalization aside, assume that users will 
input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.
"""

# Fruit Dictionary
fruits = [
    {"fruit": "apple", "calories": "130"},
    {"fruit": "avocado", "calories": "50"},
    {"fruit": "banana", "calories": "110"},
    {"fruit": "canteloupe", "calories": "50"},
    {"fruit": "grapefruit", "calories": "60"},
    {"fruit": "grapes", "calories": "90"},
    {"fruit": "honeydew melon", "calories": "50"},
    {"fruit": "kiwifruit", "calories": "90"},
    {"fruit": "lemon", "calories": "15"},
    {"fruit": "lime", "calories": "20"},
    {"fruit": "nectarine", "calories": "60"},
    {"fruit": "orange", "calories": "80"},
    {"fruit": "peach", "calories": "60"},
    {"fruit": "pear", "calories": "100"},
    {"fruit": "pineapple", "calories": "50"},
    {"fruit": "plums", "calories": "70"},
    {"fruit": "strawberries", "calories": "50"},
    {"fruit": "sweet cherries", "calories": "100"},
    {"fruit": "tangerine", "calories": "50"},
    {"fruit": "watermelon", "calories": "80"},
]


def main():
    user_fruit = input("Item: ").lower()
    # for each dict in this list
    for i in fruits:         
        # if apple matches the value of the fruit key in the first iterated list
        # use equality and not in. In means is the input inside the name. so pineapple would also be matched
        if user_fruit == i["fruit"]:      
            result = i["calories"]
            print(f"Calories: {result}")  
    
main()

# print(fruits[0]["fruit"])