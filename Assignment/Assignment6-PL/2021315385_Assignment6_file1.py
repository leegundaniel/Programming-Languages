from datetime import datetime

# Citizen class
class Citizen:
    # initialize
    def __init__(self, ssn, name, address):
        self._ssn = ssn
        self._name = name
        self._address = address
    
    # properties
    @property
    def ssn(self):
        return self._ssn
    @property
    def name(self):
        return self._name
    @property
    def address(self):
        return self._address
    
    # setters
    @ssn.setter
    def ssn(self, ssn):
        self._ssn = ssn
    @name.setter
    def name(self, name):
        self._name = name
    @address.setter
    def address(self, address):
        self._address = address

    # str()
    def __str__(self):
        return (f"{'Name':<12}: {self._name}\n"
                f"{'SSN':<12}: {self._ssn}\n"
                f"{'Address':<12}: {self._address}")

# Staff class with Citizen as Parent class
class Staff(Citizen):
    # initialize
    def __init__(self, id, ssn, name, address, jobtitle, salary):
        super().__init__(ssn, name, address)
        self._id = id
        self._jobtitle = jobtitle
        self._salary = salary

    # properties
    @property
    def id(self):
        return self._id
    @property
    def jobtitle(self):
        return self._jobtitle
    @property
    def salary(self):
        return self._salary

    # setters
    @id.setter
    def id(self, id):
        self._id = id
    @jobtitle.setter
    def jobtitle(self, jobtitle):
        self._jobtitle = jobtitle
    @salary.setter
    def salary(self, salary):
        self._salary = salary    
    
    # str()
    def __str__(self):
        staff = (f"{'ID':<12}: {self._id}\n"
                      f"{'Job Title':<12}: {self._jobtitle}\n"
                      f"{'Salary':<12}: {self._salary}")
        
        return f"{super().__str__()}\n{staff}"



# Customer class with Citizen as Parent class
class Customer(Citizen):
    # initialize
    def __init__(self, ssn, name, address, tel, purchasing_points = 0):
        super().__init__(ssn, name, address)
        self._tel = tel
        self._purchasing_points = purchasing_points
        self._memberships = []

    # properties
    @property
    def id(self):
        return self._ssn
    @property
    def tel(self):
        return self._tel
    @property
    def purchasing_points(self):
        return self._purchasing_points
    
    # setter
    @purchasing_points.setter
    def purchasing_points(self, purchasing_points):
        self._purchasing_points = purchasing_points
    @tel.setter
    def tel(self, tel):
        self._tel = tel
    
    # helper function to add membership to list
    def add_membership(self, membership):
        self._memberships.append(membership)
    
    # str()
    def __str__(self):
        customer = (f"{'Tel':<12}: {self._tel}\n"
                     f"{'Points':<12}: {self._purchasing_points}")
        
        if self._memberships:
            membership = ", ".join(self._memberships)
            customer += f"\n{'Memberships':<12}: {membership}"
        return f"{super().__str__()}\n{customer}"
     
# Store class
class Store:
    # initialize
    def __init__(self, id, name, address, tel):
        self._id = id
        self._name = name
        self._address = address
        self._tel = tel
    
    # properties
    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._name
    @property
    def address(self):
        return self._address
    @property
    def tel(self):
        return self._tel
    
    # setters
    @id.setter
    def id(self, id):
        self._id = id
    @name.setter
    def name(self, name):
        self._name = name
    @address.setter
    def address(self, address):
        self._address = address
    @tel.setter
    def tel(self, tel):
        self._tel = tel
    
    # str()
    def __str__(self):
        # return f"Store: {self._name} (ST # {self._id})\nAddress: {self._address}\nTel: {self._tel}"
    
        return (f"{'Store':<12}: {self._name}\n"
                f"{'ST':<12}: {self._id}\n"
                f"{'Address':<12}: {self._address}\n"
                f"{'Tel':<12}: {self._tel}")

# Product class
class Product:
    # initialize
    def __init__(self, code, name, description, price, points):
        self._code = code
        self._name = name
        self._description = description
        self._price = price
        self._points = points

    # properties
    @property
    def code(self):
        return self._code
    @property
    def name(self):
        return self._name
    @property
    def description(self):
        return self._description
    @property
    def price(self):
        return self._price
    @property
    def points(self):
        return self._points
    
    # setters
    @code.setter
    def code(self, code):
        self._code = code
    @name.setter
    def name(self, name):
        self._name = name
    @description.setter
    def description(self, description):
        self._description = description
    @price.setter
    def price(self, price):
        self._price = price
    @points.setter
    def points(self, points):
        self._points = points

    # str()
    def __str__(self):
        return f"Name: {self._name}\nCode: {self._code}\nPrice: {self._price}"
    
class Order:
    def __init__(self, store, customer, staff):
        self._store = store
        self._customer = customer
        self._staff = staff
        self._products = []
        self._quantity = []

    # properties
    @property
    def store(self):
        return self._store
    @property
    def customer(self):
        return self._customer
    @property
    def staff(self):
        return self._staff
    @property
    def products(self):
        return self._products
    @property
    def quantity(self):
        return self._quantity

    # setters
    @store.setter
    def store(self, store):
        self._store = store
    @customer.setter
    def customer(self, customer):
        self._customer = customer
    @staff.setter
    def staff(self, staff):
        self._staff = staff
    @products.setter
    def products(self, products):
        self._products = products
    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    # addProduct method
    def addProduct(self, product, quantity):
        # append product to the products list
        self._products.append(product)
        # append its quantity to the quantity list
        self._quantity.append(quantity)
        
        # add points to the customer
        self._customer.purchasing_points += product.points * quantity

    # printReceipt method
    def printReceipt(self):
        # Print required information
        print("="*50)
        print(f"Welcome to {self._store.name}".center(50))
        print(f"{'Staff':<10}: {self._staff.name}".center(50))
        print(f"{'Customer ID':<12}: {self._customer.id}".center(50))
        print("-"*20 + " RECEIPT " + "-"*20)
        
        current_datetime = datetime.now()
        print(f"{current_datetime.strftime("%m/%d/%Y"):^50}")
        print(f"{current_datetime.strftime("%H:%M:%S"):^50}")
        print(f"ST # {self._store.id}".center(50))
        print("-"*50)
        print(f"{'Product Name':<15} {'ProductCode':<15} {'Price':<10} {'Q':<5}")

        # total = total price
        total_price = 0
        total_quantity = 0
        for i in range(len(self._products)):
            # print each product information
            product = self._products[i]
            quantity = self._quantity[i]

            print(f"{product.name:<15}\t{product.code:<15}\t{product.price:<10}{quantity:<5}")
            # add price and quantity
            total_price += product.price * quantity
            total_quantity += quantity

        print('-'*50)
        print(f"{'Total':<40} {total_price}")
        print(f"# ITEMS SOLD {total_quantity}".center(50))
        print(f"Total Points: {self._customer.purchasing_points}".center(50))
        print(f"*** Customer Copy ***".center(50))

# run program
def main():
    # create store object
    store = Store(1235, "HomeStore", "SKKU Street, Suwon", "032-1111-2222")

    # print store information
    print("-"*10 + "Store Information" + "-"*10)
    print(store)

    # 2 staff members
    staff1 = Staff("J101", "123-456", "Lee Kimchi", "Suwon", "Manager", "010-1234-5678")
    staff2 = Staff("J110", "111-222", "Park Hello", "Seoul", "Cashier", "010-2345-6789")

    # 2 customers
    customer1 = Customer("121-234", "Kim Chiguk", "Busan", "010-3333-4444")
    customer2 = Customer("345-789", "Cheong Gukjang", "Daegu", "010-5555-6666")
    
    # print staff information
    print("-"*10 + "Staff Information" + "-"*10)
    print(staff1)
    print()
    print(staff2)

    # print customer information
    print("-"*10 + "Customer Information" + "-"*10)
    print(customer1)
    print()
    print(customer2)

    # create order
    order = Order(store, customer1, staff2)

    # create products
    chicken = Product('0192837465', "Chicken Breasts", "Tender chicken stolen from KFC", 8.15, 10)
    milk = Product('0695847320', "Milk", "You thought it was cow milk, but it's goat milk.", 2.55, 5)
    jelly = Product('2294385198', "Jelly", "Squishy wishy jelly welly", 1.55, 2)

    # product list
    products = [chicken, milk, jelly]

    print("-"*15 + "Orders" + "-"*15)
    # while loop to prompt for inputs
    while True:
        # print out product informaiton
        print("Choose a product:")
        for idx, product in enumerate(products):
            print(f"[{idx + 1}] {product.name} (${product.price}), {product.points} Pts")

        # request for choice (assume that integer value will be input)
        choice = int(input("Enter choice (0 to quit or complete order): "))

        # if choice is 0, finish order and move on
        if choice == 0:
            break

        # ensure that choice exists in product list
        choice_val = choice - 1
        if not 0 <= choice_val < len(products):
            print("Invalid choice.")
            continue

        product = products[choice_val]
        # request for quantity using while loop
        while True:
            qty = int(input(f"Enter quantity for {product.name}: "))
            # if quantity less than or equal to 0, restart
            if not qty > 0:
                print("Invalid quantity.")
                continue
            else:
                break
        # add product to order
        order.addProduct(product, qty)
        print(f"Added {qty} {product.name}.\n")

    order.printReceipt()

main()