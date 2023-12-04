class Student:
    def __init__(self, name, id, address):
        self.name = name
        self.id = id
        self.address = address
    
    def display(self):
        print(f"Name = {self.name}")
        print(f"ID = {self.id}")
        print(f"Address = {self.address}")
    
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def displayPerimeter(self):
        print(f"Perimeter: {2*3.14*self.radius}")

    def displayArea(self):
        print(f"Perimeter: {3.14*self.radius**2}")

class bankAccount:
    def __init__(self, accountNumber, customerName, balance):
        self.accountNumber = accountNumber
        self.customerName = customerName
        self.balance = int(balance)
    
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        self.balance -= amount
    
    def display(self):
        print(f"Account Number: {self.accountNumber}")
        print(f"Customer Name: {self.customerName}")
        print(f"Balance: {self.balance}")
        

