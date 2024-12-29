def main():
    ls = [10, 2, 7, 23, 5, 11, 15]
    
    # Bubble Sort Algorithm
    n = len(ls) 
    for i in range(n - 1):
        for j in range(n - i - 1): 
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]  
    
    sorted_list = ls 
    print(sorted_list)  
    return sorted_list

main()
