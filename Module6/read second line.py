import os
def read_second_last_line(file_name): 
    file=open(file_name,"r") 
    file_lines=file.readlines()
    if (len(file_lines) <= 2):
        print("no second last line")
    else:
        second_last_line = file_lines[-2].strip()
    return second_last_line
    

def main(): 
    # with open(file="D:/RoboGarden_Python_MariamH/Module6/test.txt",mode="r") as my_file:
    # # file=open('test.txt',"r")
    #     my_file.write("Hellloooooo") 
    #     print(os.path.abspath("test.txt"))
        # file_lines=my_file.readlines()
        # second_last_line = file_lines[-2]
        # print(second_last_line)
    data = read_second_last_line("D:/RoboGarden_Python_MariamH/Module6/test.txt") 

    print(data) 

    return data 

  

main() 