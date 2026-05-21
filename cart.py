# Products available
products = {
    1: {"name": "Apple",  "price": 50},
    2: {"name": "Banana", "price": 20},
    3: {"name": "Mango",  "price": 80},
    4: {"name": "Grapes", "price": 60},
}

# Cart
cart = {}

def show_products():
    print("\n=== Products ===")
    for id, item in products.items():
        print(f"{id}. {item['name']} - Rs.{item['price']}")

def add_to_cart(product_id, quantity):
    if product_id in products:
        product = products[product_id]
        cart[product['name']] = {
            'quantity': quantity,
            'price': product['price'] * quantity
        }
        print(f"{product['name']} added to cart!")
    else:
        print("Product nahi mila!")

def show_cart():
    if cart:
        total = 0
        print("\n=== Your Cart ===")
        for item, details in cart.items():
            print(f"{item}: {details['quantity']} x = Rs.{details['price']}")
            total += details['price']
        print(f"\nTotal: Rs.{total}")
    else:
        print("Cart empty hai!")

# Main Program
while True:
    print("\n=== Shop ===")
    print("1. Show Products")
    print("2. Add to Cart")
    print("3. Show Cart")
    print("4. Exit")

    choice = int(input("Choose: "))

    match choice:
        case 1:
            show_products()
        case 2:
            show_products()
            pid = int(input("Product number: "))
            qty = int(input("Quantity: "))
            add_to_cart(pid, qty)
        case 3:
            show_cart()
        case 4:
            print("Thank you!")
            break
        case _:
            print("Wrong choice!")