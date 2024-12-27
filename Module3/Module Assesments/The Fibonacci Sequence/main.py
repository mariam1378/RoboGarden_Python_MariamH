def main():  
    first_number = int(input("Enter first_number: "))
    second_number = int(input("Enter second_number: "))
    iterations = int(input("Enter iterations: "))
    ls = [first_number,second_number]
    ## Type your code here 
    for i in range(0,iterations):
        fibonacci = ls[i]+ls[i+1]
        ls.append(fibonacci)
        print(fibonacci)  

main() 