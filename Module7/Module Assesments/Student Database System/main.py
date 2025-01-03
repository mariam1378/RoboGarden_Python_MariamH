class Student: 
    def __init__(self, title, author, availability): 

        self.title = title 
        self.author = author 
        self.availability = availability 

    def display_info(self): 

        print(f"This book is {self.title} by {self.author} is {self.availability}.") 

    def check_out_and_return_books(self, title, availability):
        self.availability = availability

def main():
    print("\n--- inventory ---")
    print("1. Add a new book")
    try:
        name = input("input book name: ")
        author = input("input authhor name: ")
        status = input("input book status:")
        my_book = Student(name, author, status) 
        my_book.display_info()
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


main()