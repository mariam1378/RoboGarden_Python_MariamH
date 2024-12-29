def factorial(n):
    if n == 0 or n == 1:  
        return 1

    return n * factorial(n - 1) 

def main():
    num = int(input("Enter a non-negative integer to calculate its factorial: "))

    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(num)
        print(f"The factorial of {num} is: {result}")

main()
