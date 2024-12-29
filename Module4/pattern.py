def main():  

  

    count = 0
    pattern= 'patt'
    arr=['ffafsadasdfmda;dmsa;dsoa;fnewlkwdnkwqndpatt', 'patt', 'pattfhnalsdnsal', 'patt', 'fjoaflasdlasdowqroqnld', 'patt']
    #enter your code here
    for i in range(0,len(arr)):
    #    if pattern is partof(arr[i])
        # print(arr[i].find(pattern))
        if (arr[i].find(pattern) >=0):
            count+=1
    print(count)
    return (count )
    

main() 