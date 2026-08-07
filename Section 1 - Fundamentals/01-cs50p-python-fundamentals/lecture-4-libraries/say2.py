# Using the sayings module that we created
import sys
from sayings import hello

if len(sys.argv) ==2:
    hello(sys.argv[1])
    
    