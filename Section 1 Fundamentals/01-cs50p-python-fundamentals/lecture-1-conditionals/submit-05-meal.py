"""
Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. 
Wouldn’t it be nice if you had a program that could tell you what to eat when?

In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. 
If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. 
And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, 
to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).
"""


# breakfast = 7:00 to 8:00d
# lunch = 12:00 to 13:00
# dinner = 18:00 to 19:00

def convert(mealTime):
    hr = float(mealTime.split(sep=":")[0])
    min = float(mealTime.split(sep=":")[1])/60
    return hr + min
    

def check_meal(mealTime):
    if 7.0 <= mealTime <= 8.0:
        return "breakfast time"
    elif 12.0 <= mealTime <= 13.0:
        return "lunch time"
    elif 18.0 <= mealTime <= 19.0:
        return "dinner time"
    else:
        return ""
    
def main():
    user_input = input("What time is it? ")
    conv = convert(user_input)
    result = check_meal(conv)
    print(result)

main()
