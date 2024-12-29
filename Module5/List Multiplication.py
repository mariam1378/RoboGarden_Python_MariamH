def calc_list_items_mul(ls):
    mul_out = 1
    for item in ls:
        mul_out *=item
    return mul_out


def main():  

    ls = [12, 70, -4, 16, 22]  

    result = calc_list_items_mul(ls)   

    print(result)  

    return result 

main() 