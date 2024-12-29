def fibonacci(limit):
    ls = [0,1]
    ## Type your code here 
    for i in range(0,limit):
        fibonacci = ls[i]+ls[i+1]
        ls.append(fibonacci)
    print(ls) 
    return fibonacci

def main():  
    iterations = int(input("Enter count: "))
    fib = fibonacci(iterations)
    return fib

main() 