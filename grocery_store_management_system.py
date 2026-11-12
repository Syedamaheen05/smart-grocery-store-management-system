
print("====================================")
print("     SMART GROCERY STORE SYSTEM")
print("====================================")

# Initialize product records
products = [
    {
        "id": 101,
        "name": "Milk",
        "category": "Dairy",
        "price": 250,
        "stock": 20
    },
    {
        "id": 102,
        "name": "Bread",
        "category": "Bakery",
        "price": 150,
        "stock": 15
    },
    {
        "id": 103,
        "name": "Rice",
        "category": "Grains",
        "price": 300,
        "stock": 10
    },
    {
        "id": 104,
        "name": "Sugar",
        "category": "Grocery",
        "price": 180,
        "stock": 3
    }
]

# Initialize sales records
sales = []


# Function to display the main menu
def display_menu():
    print("\n====================================")
    print("     SMART GROCERY STORE SYSTEM")
    print("====================================")
    print("1. Add New Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Update Product Stock")
    print("5. Process Customer Sale")
    print("6. View Sales Records")
    print("7. Generate Store Report")
    print("8. Exit")
    print("====================================")


# Function to find a product using its ID
def find_product(product_id):
    for product in products:
        if product["id"] == product_id:
            return product

    # Return None when product does not exist
    return None


# Function to add a new product
def add_product():
    print("\n====================================")
    print("          ADD NEW PRODUCT")
    print("====================================")

    # Validate product ID
    try:
        product_id = int(input("Enter Product ID: "))

        if product_id <= 0:
            print("Product ID must be greater than zero!")
            return

    except ValueError:
        print("Invalid Product ID! Enter a numeric value.")
        return

    # Prevent duplicate product IDs
    if find_product(product_id) is not None:
        print("Product ID already exists! Try another ID.")
        return

    # Get product name
    product_name = input("Enter Product Name: ").strip()

    if product_name == "":
        print("Product name cannot be empty!")
        return

    # Get product category
    product_category = input("Enter Product Category: ").strip()

    if product_category == "":
        print("Product category cannot be empty!")
        return

    # Validate product price
    try:
        product_price = float(input("Enter Product Price: "))

        if product_price < 0:
            print("Price cannot be negative!")
            return

    except ValueError:
        print("Invalid price! Enter a numeric value.")
        return

    # Validate available stock
    try:
        product_stock = int(input("Enter Available Stock: "))

        if product_stock < 0:
            print("Stock cannot be negative!")
            return

    except ValueError:
        print("Invalid stock! Enter a whole number.")
        return

    # Create a product dictionary
    new_product = {
        "id": product_id,
        "name": product_name,
        "category": product_category,
        "price": product_price,
        "stock": product_stock
    }

    # Add product dictionary to products list
    products.append(new_product)

    print("\nProduct added successfully!")
    print("Product ID:", new_product["id"])
    print("Product Name:", new_product["name"])
    print("Category:", new_product["category"])
    print("Price: Rs.", new_product["price"])
    print("Available Stock:", new_product["stock"])


# Function to display all products
def view_all_products():
    print("\n====================================")
    print("          ALL PRODUCTS")
    print("====================================")

    # Check whether products are available
    if len(products) == 0:
        print("No products available in the store.")
        return

    # Display product information using a loop
    for product in products:
        print("------------------------------------")
        print("Product ID:", product["id"])
        print("Product Name:", product["name"])
        print("Category:", product["category"])
        print("Price: Rs.", product["price"])
        print("Available Stock:", product["stock"])

    print("------------------------------------")


# Function to search products by name or ID
def search_product():
    print("\n====================================")
    print("          SEARCH PRODUCT")
    print("====================================")

    if len(products) == 0:
        print("No products available in the store.")
        return

    search_value = input("Enter Product Name or ID: ").strip()

    if search_value == "":
        print("Search value cannot be empty!")
        return

    # Check whether search value is a product ID
    if search_value.isdigit():
        product_id = int(search_value)

        product = find_product(product_id)

        if product is not None:
            print("\nProduct Found!")
            print("------------------------------------")
            print("Product ID:", product["id"])
            print("Product Name:", product["name"])
            print("Category:", product["category"])
            print("Price: Rs.", product["price"])
            print("Available Stock:", product["stock"])
            print("------------------------------------")
        else:
            print("Product with this ID does not exist!")

    else:
        # Search product by name
        product_found = False

        for product in products:
            if product["name"].lower() == search_value.lower():
                print("\nProduct Found!")
                print("------------------------------------")
                print("Product ID:", product["id"])
                print("Product Name:", product["name"])
                print("Category:", product["category"])
                print("Price: Rs.", product["price"])
                print("Available Stock:", product["stock"])
                print("------------------------------------")

                product_found = True

        if not product_found:
            print("Product with this name does not exist!")


# Function to update product stock
def update_product_stock():
    print("\n====================================")
    print("        UPDATE PRODUCT STOCK")
    print("====================================")

    try:
        product_id = int(input("Enter Product ID: "))

        if product_id <= 0:
            print("Product ID must be greater than zero!")
            return

    except ValueError:
        print("Invalid Product ID! Enter a numeric value.")
        return

    # Find product using its ID
    product = find_product(product_id)

    if product is None:
        print("Product does not exist!")
        return

    print("\nProduct Name:", product["name"])
    print("Current Stock:", product["stock"])

    print("\n1. Add Stock")
    print("2. Set Stock Quantity")

    stock_choice = input("Enter your choice: ").strip()

    # Add new stock to existing quantity
    if stock_choice == "1":
        try:
            added_stock = int(input("Enter quantity to add: "))

            if added_stock <= 0:
                print("Quantity must be greater than zero!")
                return

        except ValueError:
            print("Invalid quantity! Enter a whole number.")
            return

        product["stock"] += added_stock

        print("\nStock added successfully!")

    # Set a completely new stock quantity
    elif stock_choice == "2":
        try:
            new_stock = int(input("Enter new stock quantity: "))

            if new_stock < 0:
                print("Stock cannot be negative!")
                return

        except ValueError:
            print("Invalid quantity! Enter a whole number.")
            return

        product["stock"] = new_stock

        print("\nStock quantity updated successfully!")

    else:
        print("Invalid stock update choice!")
        return

    # Display updated stock information
    print("------------------------------------")
    print("Product Name:", product["name"])
    print("Product ID:", product["id"])
    print("Updated Stock:", product["stock"])
    print("------------------------------------")


# Function to process customer sale
def process_customer_sale():
    print("\n====================================")
    print("        PROCESS CUSTOMER SALE")
    print("====================================")

    try:
        product_id = int(input("Enter Product ID: "))

        if product_id <= 0:
            print("Product ID must be greater than zero!")
            return

    except ValueError:
        print("Invalid Product ID! Enter a numeric value.")
        return

    # Check whether product exists
    product = find_product(product_id)

    if product is None:
        print("Product does not exist!")
        return

    print("\nProduct Name:", product["name"])
    print("Price: Rs.", product["price"])
    print("Available Stock:", product["stock"])

    # Get purchase quantity
    try:
        purchase_quantity = int(input("Enter Purchase Quantity: "))

        if purchase_quantity <= 0:
            print("Purchase quantity must be greater than zero!")
            return

    except ValueError:
        print("Invalid quantity! Enter a whole number.")
        return

    # Check whether sufficient stock is available
    if purchase_quantity > product["stock"]:
        print("Insufficient stock!")
        print("Available Stock:", product["stock"])
        print("Requested Quantity:", purchase_quantity)
        return

    # Calculate total purchase amount
    total_amount = product["price"] * purchase_quantity

    # Deduct purchased quantity from available stock
    product["stock"] -= purchase_quantity

    # Create sales record dictionary
    sale_record = {
        "product_id": product["id"],
        "product_name": product["name"],
        "quantity": purchase_quantity,
        "total_amount": total_amount
    }

    # Store completed sale in sales list
    sales.append(sale_record)

    # Display purchase summary
    print("\n====================================")
    print("        PURCHASE SUMMARY")
    print("====================================")
    print("Product ID:", product["id"])
    print("Product Name:", product["name"])
    print("Price per Unit: Rs.", product["price"])
    print("Quantity Purchased:", purchase_quantity)
    print("Total Amount: Rs.", total_amount)
    print("Remaining Stock:", product["stock"])
    print("====================================")
    print("Sale completed successfully!")


# Function to display sales records
def view_sales_records():
    print("\n====================================")
    print("          SALES RECORDS")
    print("====================================")

    # Check whether sales records exist
    if len(sales) == 0:
        print("No sales transactions recorded yet.")
        return

    # Display all sales records
    for sale in sales:
        print("------------------------------------")
        print("Product ID:", sale["product_id"])
        print("Product Name:", sale["product_name"])
        print("Quantity Sold:", sale["quantity"])
        print("Total Amount: Rs.", sale["total_amount"])

    print("------------------------------------")


# Function to generate store report
def generate_store_report():
    print("\n====================================")
    print("          STORE REPORT")
    print("====================================")

    # Check whether products exist
    if len(products) == 0:
        print("No products available for store report.")
        return

    # Initialize report variables
    total_products = len(products)
    total_available_stock = 0
    total_sales_transactions = len(sales)
    total_revenue = 0

    # Calculate total available stock
    for product in products:
        total_available_stock += product["stock"]

    # Calculate total revenue from completed sales
    for sale in sales:
        total_revenue += sale["total_amount"]

    # Find products with stock below 5 units
    low_stock_products = []

    for product in products:
        if product["stock"] < 5:
            low_stock_products.append(product)

    # Find product with highest price
    highest_price_product = products[0]

    for product in products:
        if product["price"] > highest_price_product["price"]:
            highest_price_product = product

    # Find product with lowest price
    lowest_price_product = products[0]

    for product in products:
        if product["price"] < lowest_price_product["price"]:
            lowest_price_product = product

    # Display general store information
    print("Total Number of Products:", total_products)
    print("Total Available Stock:", total_available_stock)
    print("Total Sales Transactions:", total_sales_transactions)
    print("Total Revenue Generated: Rs.", total_revenue)

    # Display low stock products
    print("\n------------------------------------")
    print("       LOW STOCK PRODUCTS")
    print("------------------------------------")

    if len(low_stock_products) == 0:
        print("No products have stock below 5 units.")
    else:
        for product in low_stock_products:
            print(
                product["name"],
                "- Stock:",
                product["stock"],
                "- ID:",
                product["id"]
            )

    # Display highest-priced product
    print("\n------------------------------------")
    print("       HIGHEST PRICE PRODUCT")
    print("------------------------------------")
    print("Product Name:", highest_price_product["name"])
    print("Product ID:", highest_price_product["id"])
    print("Price: Rs.", highest_price_product["price"])

    # Display lowest-priced product
    print("\n------------------------------------")
    print("       LOWEST PRICE PRODUCT")
    print("------------------------------------")
    print("Product Name:", lowest_price_product["name"])
    print("Product ID:", lowest_price_product["id"])
    print("Price: Rs.", lowest_price_product["price"])

    print("\n====================================")
    print("       END OF STORE REPORT")
    print("====================================")


# Main program loop
while True:

    # Display application menu
    display_menu()

    choice = input("Enter your choice: ").strip()

    # Perform operation according to user choice
    if choice == "1":
        add_product()

    elif choice == "2":
        view_all_products()

    elif choice == "3":
        search_product()

    elif choice == "4":
        update_product_stock()

    elif choice == "5":
        process_customer_sale()

    elif choice == "6":
        view_sales_records()

    elif choice == "7":
        generate_store_report()

    elif choice == "8":
        print("\n====================================")
        print("Thank you for using Grocery Store!")
        print("Exiting the system...")
        print("====================================")
        break

    else:
        print("\nInvalid choice! Please select from 1 to 8.")
