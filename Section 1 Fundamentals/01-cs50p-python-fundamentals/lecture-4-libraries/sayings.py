# Creating our own module/library which can then be re-used

def hello(name):
    print(f"Hello, {name}")
    
def goodbye(name):
    print(f"Goodbye, {name}")
    
    
# If you do not remove main(), when this library is used, main() will also get called
def main():
    hello("world")
    goodbye("world")
# main()

# Can do this instead:

if __name__ == "__main__":
    main()