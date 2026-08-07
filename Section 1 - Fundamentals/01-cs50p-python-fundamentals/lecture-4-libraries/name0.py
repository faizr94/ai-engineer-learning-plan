# command-line arguments
import sys
"""
sys.argv
    --> argument vector
    --> the list of all the words that the human typed in at their prompt before they hit Enter
"""

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few args")