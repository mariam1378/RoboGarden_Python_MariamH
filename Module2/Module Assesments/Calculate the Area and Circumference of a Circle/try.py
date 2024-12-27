def main():  

  

    ls=[2,8,6,5,2,7,9]   
    count = 0
    index = 0

    ## Type your code here 
    for item in ls:
        count +=1
        if (item % 2 == 0):
            pass
        elif (item % 2 != 0):
            index = count -1
 
  
    print(index)
    return index  

  

main() 