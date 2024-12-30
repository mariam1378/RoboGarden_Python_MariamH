def average_grade(ls):
    total = sum(ls)
    average = total / len(ls)
    return average

def store_in_file(file_name,name,ls, average):
    try:
        with open(file_name, "a") as file:
            file.write(name+" ")
            for i in range(len(ls)):
                strls=str(ls[i])
                file.write(strls+" ")
            file.write(str(average) +"\n")
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
    
    average = average_grade(grades_list)
    store_in_file(file_name,student_name,grades_list, average)
    return grades_list, student_name , average

def main():
    file_name = "student_grades.txt"
    while True:
        print("\n--- Grade Tracker ---")
        try:
            grade_tracker(file_name)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


main()
