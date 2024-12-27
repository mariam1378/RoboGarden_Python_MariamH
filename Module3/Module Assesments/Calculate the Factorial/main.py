def main():  
    num = int(input("Enter number: "))
    factorial = 1
    ## Type your code here 
    for i in range(0,num):
        factorial *= num
        num -=1

    print(factorial)  

main() 