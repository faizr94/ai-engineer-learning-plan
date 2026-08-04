# Error handling and pre-check instead of simply checking the exceptions
import sys
"""
sys.argv
    --> argument vector
    --> the list of all the words that the human typed in at their prompt before they hit Enter
"""



if len(sys.argv) < 2:
    sys.exit("Too few args")
elif len (sys.argv) > 2:
    sys.exit("Too many args")

print("hello, my name is", sys.argv[1])