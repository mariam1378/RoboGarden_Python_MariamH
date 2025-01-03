class BankAccount: 

    def __init__(self, name, accountType, balance =0): 

        self.name = name 
        self.accountType = accountType 
        self.balance = balance 


    def display_info(self): 

        print(f"This is a {self.name} {self.accountType}.") 

    def __del__(self): 

        print(f"{self.name} {self.accountType} 'Car' object has been deleted.")    

#Create an object of the Car class and display its info. 

another_car = BankAccount("Nissan","Versa") 
