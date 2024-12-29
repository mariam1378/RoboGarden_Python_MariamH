# def fibonacci(limit):
#     ls = [0,1]
#     ## Type your code here 
#     for i in range(0,limit):
#         fibonacci = ls[i]+ls[i+1]
#         ls.append(fibonacci)
#     print(ls) 
#     return fibonacci

def rec_fibonacci(limit):
    if limit == 0:
        return 0
    elif limit == 1:  
        return 1
    
    return rec_fibonacci(limit - 1) + rec_fibonacci(limit - 2) 

def main():  
    iterations = int(input("Enter count: "))
    fib_num = rec_fibonacci(iterations)
    print("Fibonacci number is: ",fib_num)
    return fib_num

main() 