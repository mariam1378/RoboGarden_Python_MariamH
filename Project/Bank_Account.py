class BankAccount: 

    def __init__(self, make, model): 

        self.make = make 

        self.model = model 

    def display_info(self): 

        print(f"This is a {self.make} {self.model}.") 

    def __del__(self): 

        print(f"{self.make} {self.model} 'Car' object has been deleted.")    

#Create an object of the Car class and display its info. 

another_car = BankAccount("Nissan","Versa") 
