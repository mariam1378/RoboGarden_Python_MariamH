# # def conv_degree_to_percentage(degree): 

# #     if (degree<0): 

# #         raise ValueError("Your course degree or total degree is below zero") 

# #     return (degree/total_degree)*100 

  

# # try:  

# #     conv_degree_to_percentage(-1) 

  

# # except ValueError as arg: 

# #     print("The ValueError exception is raised due to:", arg)

# # def main(): 

# #     ls=[16,9,8] 

# #     idx=2 
    
# #     try:  
# #         print(ls[idx])
# #         print("True")
# #         return True
# #     except:  
# #         print("False")
# #         return False 

# # main() 

# def main(): 

#     dictionary={"a": "apple", "b":"banana"} 

#     key="c" 
#     try:
#         print(dictionary[key])
#         print("True")
#         return True  
#     except KeyError:
#         print("False")
#         return False 


# main() 

def main():
    command = 'remove'
    # match command:
    #  	case 'Hello, World!':
    #          print('Hello to you too!')
    #  	case 'Goodbye, World!':
    #          print('See you later')
    #  	case other:
    #          print('No match found')
    match command.split():
        case ['show']:
                print('List all files and directories: ')
                # code to list files
        case ['remove', *files]:
                print('Removing files: {}'.format(files))
                # code to remove files
        case _:
                print('Command not recognized')

main() 
