# Module 7 Assignment: Organizing Data with Lists and Tuples
# TechElectronics Inventory Tracking System
# Chloe Cunningham
# Oct 8 2025

# Welcome message
print("=" * 60)
print("TECHELECTRONICS INVENTORY TRACKING SYSTEM")
print("=" * 60)

# TODO 1: Create product tuples
product1 = ("P001", "Smartphone X", 799.99, 10, "Mobile Phones")
product2 = ("P002", "MacBook Pro", 1299.99, 5, "Laptops")
product3 = ("P003", "Beats Headphones", 199.99, 15, "Audio")
product4 = ("P004", "Applewatch", 349.99, 4, "Wearables")
product5 = ("P005", "Bluetooth Speaker", 149.99, 8, "Audio")

# TODO 2: Create an inventory list containing all product tuples
inventory = [product1, product2, product3, product4, product5]

product_drone = ("P008", "Drone AirX", 899.99, 6, "Gadgets")
inventory.insert(1, product_drone)

# TODO 3: Display all products
print("\nCurrent Inventory:")
print("-" * 60)
for product in inventory:
    print(product)

# TODO 4: Access specific elements
print("\n\nAccessing Specific Products:")
print("-" * 60)

first_product = inventory[0]
print("First product:", first_product)

last_product = inventory[-1]
print("Last product:", last_product)

third_product_name = inventory[2][1]
print("Third product name:", third_product_name)

second_price = inventory[1][2]
second_quantity = inventory[1][3]
print("Second product price:", second_price)
print("Second product quantity:", second_quantity)

# TODO 5: Use slicing to get subsets
print("\n\nProduct Subsets Using Slicing:")
print("-" * 60)
first_three = inventory[:3]
print("First 3 products:", first_three)

middle_products = inventory[2:5]
print("Products index 2 to 4:", middle_products)

all_except_first = inventory[1:]
print("All except first product:", all_except_first)

# TODO 6: Add new products to inventory
print("\n\nAdding New Products:")
print("-" * 60)
product6 = ("P006", "Gaming Laptop", 1599.99, 3, "Laptops")
product7 = ("P007", "ipad 5th gen", 499.99, 12, "Mobile Devices")

inventory.append(product6)
inventory.append(product7)

for product in inventory:
    print(product)

# TODO 7: Remove a product
print("\n\nRemoving a Product:")
print("-" * 60)
removed_product = inventory.pop(2)
print("Removed product:", removed_product)

for product in inventory:
    print(product)

# ✅ TODO 8: Insert a product and recompute variables after all edits
print("\n\nInserting a Product:")
print("-" * 60)

new_product = ("P008", "Drone AirX", 899.99, 6, "Gadgets")

# Remove duplicate appends — only insert the new product
inventory.insert(1, new_product)

for product in inventory:
    print(product)

# ✅ Recompute AFTER all appends/pops/inserts
first_product = inventory[0]
last_product = inventory[-1]
third_product_name = inventory[2][1]
second_price = inventory[1][2]
second_quantity = inventory[1][3]

first_three = inventory[:3]
middle_products = inventory[2:5]
all_except_first = inventory[1:]

print("\nRecomputed Variables After Final Edits:")
print("-" * 60)
print("First product:", first_product)
print("Last product:", last_product)
print("Third product name:", third_product_name)
print("Second product price:", second_price)
print("Second product quantity:", second_quantity)
print("First three:", first_three)
print("Middle products:", middle_products)
print("All except first:", all_except_first)

# TODO 9: Create category lists
print("\n\nProducts by Category:")
print("-" * 60)
mobile_phones = []
laptops = []
audio = []
wearables = []
gadgets = []
mobile_devices = []

for product in inventory:
    category = product[4]
    if category == "Mobile Phones":
        mobile_phones.append(product)
    elif category == "Laptops":
        laptops.append(product)
    elif category == "Audio":
        audio.append(product)
    elif category == "Wearables":
        wearables.append(product)
    elif category == "Gadgets":
        gadgets.append(product)
    elif category == "Mobile Devices":
        mobile_devices.append(product)

print("Mobile Phones:", mobile_phones)
print("Laptops:", laptops)
print("Audio:", audio)
print("Wearables:", wearables)
print("Gadgets:", gadgets)
print("Mobile Devices:", mobile_devices)

# TODO 10: Calculate inventory statistics
print("\n\nInventory Statistics:")
print("-" * 60)
total_products = len(inventory)
total_value = sum(product[2] * product[3] for product in inventory)
product_names = [product[1] for product in inventory]
product_prices = [product[2] for product in inventory]

print(f"Total products: {total_products}")
print(f"Total inventory value: ${total_value:.2f}")
print("Product names:", product_names)
print("Product prices:", product_prices)

# TODO 11: Find expensive products using list comprehension
print("\n\nExpensive Products (> $500):")
print("-" * 60)
expensive_products = [product for product in inventory if product[2] > 500]
for product in expensive_products:
    print(product)

# TODO 12: Low stock alert using list comprehension
print("\n\nLow Stock Alert (< 5 units):")
print("-" * 60)
low_stock = [product for product in inventory if product[3] < 5]
for product in low_stock:
    print(product)

# TODO 13: Create price list using list comprehension
print("\n\nPrice Lists:")
print("-" * 60)
original_prices = [product[2] for product in inventory]
discounted_prices = [price * 0.9 for price in original_prices]
print("Original prices:", original_prices)
print("Discounted prices (10% off):", discounted_prices)

# TODO 14: Product name formatting using list comprehension
print("\n\nFormatted Product Names:")
print("-" * 60)
uppercase_names = [product[1].upper() for product in inventory]
product_codes = [product[0][:3] + product[1][:3] for product in inventory]
print("Uppercase names:", uppercase_names)
print("Product codes:", product_codes)

# TODO 15: Using Loops to Process Inventory
print("\n\nLoop-Based Analysis:")
print("-" * 60)
mobile_count = 0
laptop_value = 0
most_expensive = inventory[0]

for product in inventory:
    category = product[4]
    price = product[2]
    quantity = product[3]
    if category == "Mobile Phones":
        mobile_count += 1
    if category == "Laptops":
        laptop_value += price * quantity
    if price > most_expensive[2]:
        most_expensive = product

print(f"Number of Mobile Phones: {mobile_count}")
print(f"Total value of Laptops: ${laptop_value:.2f}")
print("Most expensive product:", most_expensive)

# TODO 16: Using Conditionals with Lists
print("\n\nConditional Analysis:")
print("-" * 60)
restock_list = []
high_value_items = []
price_ranges = {"under_100": 0, "100_to_500": 0, "over_500": 0}

for product in inventory:
    price = product[2]
    quantity = product[3]
    if quantity < 5:
        restock_list.append(product)
    if price > 500 and quantity > 10:
        high_value_items.append(product)
    if price < 100:
        price_ranges["under_100"] += 1
    elif 100 <= price <= 500:
        price_ranges["100_to_500"] += 1
    else:
        price_ranges["over_500"] += 1

print("Products needing restock:", restock_list)
print("High-value items:", high_value_items)
print("Price ranges count:", price_ranges)

# TODO 17: Define and Use Functions
print("\n\nFunction-Based Operations:")
print("-" * 60)
def calculate_product_value(product):
    return product[2] * product[3]

def find_products_by_category(inventory, category):
    return [product for product in inventory if product[4] == category]

def apply_discount(inventory, discount_percent):
    discounted_inventory = []
    for product in inventory:
        discounted_price = product[2] * (1 - discount_percent / 100)
        discounted_product = (product[0], product[1], discounted_price, product[3], product[4])
        discounted_inventory.append(discounted_product)
    return discounted_inventory

total_inventory_value = sum(calculate_product_value(p) for p in inventory)
print(f"Total inventory value: ${total_inventory_value:.2f}")
audio_products = find_products_by_category(inventory, "Audio")
print("Audio products:", audio_products)
discounted_inventory = apply_discount(inventory, 15)
print("Inventory with 15% discount applied:")
for product in discounted_inventory:
    print(product)

# TODO 18: Comprehensive Inventory Report
print("\n\nComprehensive Inventory Report:")
print("-" * 60)
def generate_inventory_report(inventory):
    total_products = len(inventory)
    total_value = sum(product[2] * product[3] for product in inventory)
    categories = list({product[4] for product in inventory})
    low_stock = [product for product in inventory if product[3] < 5]
    average_price = sum(product[2] for product in inventory) / total_products if total_products > 0 else 0
    report = {
        "total_products": total_products,
        "total_value": total_value,
        "categories": categories,
        "low_stock": low_stock,
        "average_price": average_price
    }
    return report

inventory_report = generate_inventory_report(inventory)
for key, value in inventory_report.items():
    print(f"{key}: {value}")
