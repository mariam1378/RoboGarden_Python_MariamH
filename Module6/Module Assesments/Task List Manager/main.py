import os

def add_tasks(tasks):
    temp =[]
    task = input("Enter task")
    temp.append(task)
    for i,task in enumerate(temp):
        task_tup = (str(i),task)
        tasks.append(task_tup)

    return 

def remove_tasks(ls, no):
    for item in ls:
        if int(item[0]) == no:
            del item

def save_tasks_to_file(file_name,tasks):
    try:
        with open(file_name, "a") as file:
            for i in range(len(tasks)):
                file.write(tasks[i] +"\n")
            print("Your entry has been saved!")
    except PermissionError:
        print("Error: You do not have permission to write to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def view_the_current_task_list(ls):
    print(f"Your current list is {ls}")

def load_tasks_from_file(file_name):
    try:
        curr_ls = []
        with open(file_name, "r") as file:
            curr_ls = file.read()
            print(f"Your current list is {curr_ls}")
        return curr_ls
    except PermissionError:
        print("Error: You do not have permission to write to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    file_name = "task_list.txt"
    if os.path.exists(file_name):
        print(f"The file '{file_name}' exists.")
        tasks =load_tasks_from_file(file_name)
    else:
        print(f"The file '{file_name}' does not exist.")
        tasks =[]
    
    # view_the_current_task_list(tasks)
    while True:
        print("\n--- Task Manager ---")
        print("1. Write a new Task")
        print("2. Remove task")
        print("3. Save tasks to file")
        print("4. Load tasks from file")
        print("5. Exit")
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                add_tasks(tasks)
                save_tasks_to_file(file_name,tasks)
            elif choice == 2:
                no = int(input("Choose a nunber to delete "))
                remove_tasks(tasks, no)
            elif choice == 3:
                save_tasks_to_file(file_name,tasks)
            elif choice == 4:
                load_tasks_from_file(file_name)
            elif choice == 5:
                print("Goodbye! Your diary is safe.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


main()


