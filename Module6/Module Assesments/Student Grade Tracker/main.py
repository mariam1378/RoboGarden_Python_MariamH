def average_grade(ls):
    total = sum(ls)
    average = total / len(ls)
    return average

def store_in_file(file_name,name,ls):
    # print("hello essam")
    try:
        with open(file_name, "a") as file:
            file.write(name+" ")
            for i in range(len(ls)):
                strls=str(ls[i])
                print(type(strls))
                file.write(strls+" ")
            file.write("\n")
            print("Your entry has been saved!")
    except PermissionError:
        print("Error: You do not have permission to write to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def grade_tracker(file_name):
    student_name = input("Enter student name : ")
    print("enter student grades ")
    subjects = ["Arabic", "Math", "Spanish", "Geography", "History"]
    grade = 0
    grades_list =[]
    for i in range(len(subjects)):
        grade = int(input(f"enter {subjects[i]} grade : "))
        grades_list.append(grade)
    
    store_in_file(file_name,student_name,grades_list)
    average = average_grade(grades_list)
    return grades_list, student_name , average

def main():
    file_name = "student_grades.txt"
    while True:
        print("\n--- Grade Tracker ---")
        print("1. Write a new entry")
        print("2. View previous entries")
        print("3. Exit")
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                grade_tracker(file_name)
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        # file_name = "Grade_Tracker.txt"
        # grades = grade_tracker()
        # print(grades)


main()
