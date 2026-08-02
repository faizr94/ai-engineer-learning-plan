"""
When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. 
In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, 
whether inputted in uppercase or lowercase.
"""


def vowel(ori_string):
    new_string = []
    for char in ori_string:
        if char.lower() not in ("a", "e", "i", "o", "u"):
            new_string.append(char)
    return "".join(new_string)

def main():
    ori_string = input("Input: ")
    result = vowel(ori_string)
    print(result)
    
main()
