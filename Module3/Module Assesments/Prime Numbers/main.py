def main():
    limit = int(input("Enter the upper limit to find prime numbers: "))

    if limit <= 1:
        print("There are no prime numbers less than or equal to 1.")
    else:
        print(f"Prime numbers up to {limit}:")

        for num in range(2, limit + 1): 
            is_prime = True 

            for divisor in range(2, int(num ** 0.5) + 1):
                if num % divisor == 0:
                    is_prime = False 
                    break 

            if is_prime:
                print(num)

main()
