def calc_dot_product(ls1,ls2):
    dot_product = 0
    if (len(ls1)==len(ls2)):
        for i in range(len(ls1)):
            dot_product += ls1[i]*ls2[i]
       
    #####################
    return dot_product

def main():
    list_1 = [2, 7, 4, 6, 2]
    list_2 = [1, 6, 3, 5, 1]

    result = calc_dot_product(list_1, list_2)
    print("The Dot Product of these two lists is:", result)
    
main()