"""
FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art.

Among the fonts supported by FIGlet are those at figlet.org/examples.html.

FIGlet has since been ported to Python as a module called pyfiglet.

In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.
"""

# import pyfiglet
from pyfiglet import Figlet
import sys

# List of fonts to check against
font_list = Figlet().getFonts()

def main():
    x = sys_check()
    user_input = input("Input: ")
    result = render_figlet(user_input, x)
    print(result)

def sys_check():
    font_check = ['-f', '--font']
    if len(sys.argv) == 1:
        return None
    elif len(sys.argv) != 3 or sys.argv[1] not in font_check or sys.argv[2] not in font_list:
        sys.exit('Invalid usage')
    else:
        return sys.argv[2]


def render_figlet(user_input, user_font):
    if sys_check() is None:
        return Figlet().renderText(user_input)
    # elif sys_check() == 2:
    else:
        f = Figlet(font=user_font)
        return f.renderText(user_input)
            
    
main()
