def main():  
    iterations = int(input("Enter count: "))
    ls = [0,1]
    ## Type your code here 
    for i in range(0,iterations):
        fibonacci = ls[i]+ls[i+1]
        ls.append(fibonacci)
        print(fibonacci)  

main() 