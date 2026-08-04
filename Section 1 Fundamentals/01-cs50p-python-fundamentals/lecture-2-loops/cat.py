# using while
# i = 0
# while i < 3:
#     print("meow")
#     i += 1

# using for
# for i in range(3):
#     print("meow")


# pythonic way
# print("meow\n" * 3, end="")


def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What is n? "))
        if n > 0:
            return n        
    
def meow(n):
    for _ in range(n):
        print("meow")
        
main()