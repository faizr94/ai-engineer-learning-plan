# x = int(input("What is x? "))

# if x%2 == 0:
#     print("even")
# else:
#     print("odd")

def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("even")
    else:
        print("odd")
        
def is_even(n):
    return n % 2 == 0
        
        
main()