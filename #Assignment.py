#Assignment
#Methods are functions which are defined by us




#Library managment system
class Book:
    def __init__(self,title,author,isbn,publish_year,available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publish_year = publish_year
        self.available_copies = available_copies
    
    def check_out(self):
        if self.available_copies > 0:
            self.available -= 1
            print("checkout succesful")
        else:
            print("No copies available")

    def return_book(self):
        self.return_book += 1
        print("Book retured succesfully")
        
    def display_book_info(self):
        print("title", self.title)
        print("author", self.author)
        print("isbn",self.isbn)
        print("publishyear",self.publish_year)
        print("available copies", self.available_copies)

b1 = Book("Two states","Chethan Bhagath","123","2016","10")
b1.display_book_info
b1.check_out
b1.return_book
b1.display_book_info

    
# Ticket Booking system

class Ticket:
    def __init__(self,ticket_id,event_name,event_date,venue,seat_number,price):
        self.ticket_id = ticket_id
        self.event_name = event_name
        self.event_date = event_date
        self.venue = venue
        self.seat_number = seat_number
        self.price = price
        self.is_reserved = False

    def reserve_ticket(self):
        if not self.is_reserved:
            self.is_reserved = True
            print("Ticket booking succesful")
        else:
            print("Tucket not available")

    def cancel_reservation(self):
        if  self.is_reserved:
            self.is_reserved = False
            print("Cancel succesful")
        else:
            print("ticket not bookled")

    def display_ticket_info(self):
        
        print("Ticket id", self.ticket_id)
        print("event_name", self.event_name)
        print("event date", self.event_date)
        print("venue", self.venue)
        print("seat number", self.seat_number)
        print("price", self.price)
        print("Resrved ststus", "Reserved" if self.is_reserved else "not reserved")

t1 = Ticket("1","kyx","1","hyd","SL-30","100")
t1.display_ticket_info()
t1.reserve_ticket()
t1.cancel_reservation()
t1.display_ticket_info()




class shopping_cart:
    def __init__(self):
        self.item = []

    def add_item(self,item):
        self.item.append[item]
        print("added succesfully")

    def remove_item(self,item):
        if item in self.item:
            self.item.remove(item)
            print("Removed")
        else:
            print("no item")

    def view_cart(self):
        if self.item:
            for item in self.item:
                print (item)
        else:
            print("no items")

    def clear_cart(self):
        self.items = []
        print("cart is cleared")

# school managemnet sysxtem

class Student:
    def __init__(self,name,age,grade,student_id,attendence):
        self.name = name
        self.age = age
        self.grade = grade
        self.student_id = student_id
        self.attendence = {}

    def update_attendence(self,date,status):
        self.attendence[date] = status

    def get_attendence(self):
        return self.attendence
    
    def get_average_attendance(self):
        total_days = len(self.attendance)
        present_days = sum(1 for status in self.attendance.values() if status == 'present')
        attendance_percentage = (present_days / total_days) * 100
        return attendance_percentage

    
        
#6TH Question

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_make(self):
        return self.make
    
    def get_model(self):
        return self.model
    
    def get_year(self):
        return self.year
    
    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
    
    def get_fuel_type(self):
        return self.fuel_type
    
    def display_info(self):
        super().display_info()
        print(f"Fuel Type: {self.fuel_type}")

vehicle1 = Vehicle("Kia", "ev", 2022)
print("Vehicle 1:")
vehicle1.display_info()
print()

car1 = Car("Tesla", "ab", 2023, "Electric")
print("Car 1:")
car1.display_info()

#7th question 
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def get_name(self):
        return self.name
    
    def get_salary(self):
        return self.salary
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def get_department(self):
        return self.department
    
    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    
    def get_programming_language(self):
        return self.programming_language
    
    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

employee1 = Employee("Ajay", 1)
print("Employee 1:")
employee1.display_info()
print()

manager1 = Manager("Barsha", 2, "backend")
print("Manager 1:")
manager1.display_info()
print()

developer1 = Developer("Mani", 3, "Testing")
print("Developer 1:")
developer1.display_info()


#8th qn
class Shape:
    def __init__(self, colour, border_width):
        self.colour = colour
        self.border_width = border_width
    
    def get_colour(self):
        return self.colour
    
    def get_border_width(self):
        return self.border_width
    
    def display_info(self):
        print(f"Colour: {self.colour}")
        print(f"Border Width: {self.border_width}")


class Rectangle(Shape):
    def __init__(self, colour, border_width, length, width):
        super().__init__(colour, border_width)
        self.length = length
        self.width = width
    
    def get_length(self):
        return self.length
    
    def get_width(self):
        return self.width
    
    def display_info(self):
        super().display_info()
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")


class Circle(Shape):
    def __init__(self, colour, border_width, radius):
        super().__init__(colour, border_width)
        self.radius = radius
    
    def get_radius(self):
        return self.radius
    
    def display_info(self):
        super().display_info()
        print(f"Radius: {self.radius}")

shape1 = Shape("Red", 2)
print("Shape 1:")
shape1.display_info()
print()

rectangle1 = Rectangle("Blue", 1, 5, 3)
print("Rectangle 1:")
rectangle1.display_info()
print()

circle1 = Circle("Green", 2, 7)
print("Circle 1:")
circle1.display_info()

#9thqn

class Device:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def get_brand(self):
        return self.brand
    
    def get_model(self):
        return self.model
    
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model:{self.model}")

class Phone(Device):
      def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size
        
      def get_screen_size(self):
        return self.screen_size
    
      def display_info(self):
        super().display_info()
        print(f"Screen Size: {self.screen_size}")


class Tablet(Device):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
    
    def get_battery_capacity(self):
        return self.battery_capacity
    
    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity}")

device1 = Device("realme", "7 pro")
print("Device 1:")
device1.display_info()
print()

phone1 = Phone("Samsung", "J7 max", 6.2)
print("Phone 1:")
phone1.display_info()
print()

tablet1 = Tablet("Samsung", "kk", "10,000 mAh")
print("Tablet 1:")
tablet1.display_info()
              
        

#10th qn

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def get_account_number(self):
        return self.account_number
    
    def get_balance(self):
        return self.balance
    
    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
    
    def calculate_interest(self, interest_rate):
        interest = self.balance * interest_rate
        self.balance += interest
    
    def display_info(self):
        super().display_info()
        print("Account Type: Savings Account")


class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
    
    def deduct_fees(self, fee_amount):
        self.balance -= fee_amount
    
    def display_info(self):
        super().display_info()
        print("Account Type: Checking Account")

savings_account1 = SavingsAccount("s1", 5000)
print("Savings Account 1:")
savings_account1.display_info()
savings_account1.calculate_interest(0.05)  
print("Balance after interest calculation:", savings_account1.get_balance())
print()

checking_account1 = CheckingAccount("C1", 1000)
print("Checking Account 1:")
checking_account1.display_info()
checking_account1.deduct_fees(10)  
print("Balance after fee deduction:", checking_account1.get_balance())

