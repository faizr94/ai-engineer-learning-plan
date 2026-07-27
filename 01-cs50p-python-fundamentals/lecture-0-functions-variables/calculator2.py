def main():
    x = int(input("Number to square: "))
    print(f"{x} squared is", square(x))
    
def square(n):
    return n * n

main()