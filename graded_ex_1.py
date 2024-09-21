products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    if sort_order == "asc":
        sorted_list = sorted(products_list, key=lambda x: x[1])
    elif sort_order == "desc":
        sorted_list = sorted(products_list, key=lambda x: x[1], reverse=True)
    print(f"Sorted products: {sorted_list}")
    return sorted_list


def display_products(products_list):
    for i, (product, price) in enumerate(products_list):
        print(f"{i + 1}. {product} - ${price}")


def display_categories():
    categories = list(products.keys())
    for i, category in enumerate(categories):
        print(f"{i + 1}. {category}")
    try:
        choice = int(input("Select a category (Enter the number): "))
        if 1 <= choice <= len(categories):
            return choice - 1  # Return zero-based index
        else:
            return None
    except ValueError:
        return None


def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))
    print(f"Cart after adding: {cart}")


def display_cart(cart):
    total_cost = 0
    for product, price, quantity in cart:
        cost = price * quantity
        total_cost += cost
        print(f"{product} - ${price} x {quantity} = ${cost}")
    print(f"Total cost: ${total_cost}")


def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print("Items Purchased:")
    for product, price, quantity in cart:
        print(f"{quantity} x {product} - ${price} = ${price * quantity}")
    print(f"Total: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days.")
    print("Payment will be accepted after delivery.")


def validate_name(name):
    parts = name.split()
    if len(parts) == 2 and all(part.isalpha() for part in parts):
        print(f"Name {name} is valid.") 
        return True
    print(f"Name {name} is invalid.") 
    return False



def validate_email(email):
    return "@" in email and len(email) > 3

    
def main():
    cart = []
    total_cost = 0

    name = input("Enter your name: ")
    while not validate_name(name):
        print("Invalid name. Please enter a valid first and last name.")
        name = input("Enter your name: ")

    email = input("Enter your email: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email.")
        email = input("Enter your email: ")

    while True:
        category_index = display_categories()
        if category_index is None:
            continue

        category_name = list(products.keys())[category_index]
        products_list = products[category_name]
        display_products(products_list)

        while True:
            action = input("\n1. Select a product to buy\n2. Sort products by price\n3. Go back\n4. Finish shopping\nChoose an option: ")
            if action == "1":
                product_index = int(input("Select a product (Enter number): ")) - 1
                if 0 <= product_index < len(products_list):
                    quantity = int(input("Enter quantity: "))
                    add_to_cart(cart, products_list[product_index], quantity)
                    total_cost += products_list[product_index][1] * quantity
                else:
                    print("Invalid product number.")
            elif action == "2":
                sort_order = input("Sort by: 1. Ascending 2. Descending: ")
                sorted_products = display_sorted_products(products_list, "asc" if sort_order == "1" else "desc")
                display_products(sorted_products)
            elif action == "3":
                break
            elif action == "4":
                if cart:
                    display_cart(cart)
                    address = input("Enter delivery address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for visiting. Hope you buy something next time.")
                return


""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
