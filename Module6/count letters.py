# import os
# with open("test.txt",mode="w") as my_file:
#     my_file.write('''
    
#     Hi!! 
#     Hello 
#     Welcome 
    
#     ''')

def cnt_file_chars(file_name): 
    count =0
    file=open(file_name,"r") 
    for item in file:
        for i in item:
            if (i != " " and i != "\n"):
                count +=1
    return count
    

     

def main(): 

    out = cnt_file_chars("D:/RoboGarden_Python_MariamH/Module6/test.txt") 

    print(out) 

    return out 

  

main() 