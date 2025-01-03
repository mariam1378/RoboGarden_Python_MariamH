class product: 
    def __init__(self, name, price, quantity): 

        self.name = name 
        self.price = price 
        self.quantity = quantity 

    def display_info(self): 

        print(f"This book is {self.title} by {self.author} is {self.quantity}.") 

#Calculate and display the total value of the inventory (sum of the values of all products).
    def display_total_value(self):

        total = self.quantity * self.price
        return total

    def update_quantity(self, quantity):
        self.quantity = quantity

def main():
    print("\n--- inventory ---")
    print("1. Add a new book")
    try:
        name = input("input book name: ")
        author = input("input authhor name: ")
        status = input("input book status:")
        my_book = product(name, author, status) 
        my_book.display_info()
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


main()