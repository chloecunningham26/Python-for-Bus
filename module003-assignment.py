#Chloe Cunningham
#Module 3 Assignment
#String manipulation

#print("=" * 50)
#print("CUSTOMER ORDER PROCESSING SYSTEM")
#print("=" * 50)
#print("Please enter the following information:\n")

customer_name = input("Enter customer name: ").strip().title()
customer_email = input("Enter customer email: ").strip().lower()
product_name = input("Enter product name: ").strip().title()

quantity = int(input("Enter quantity: ").strip())
int(quantity)

unit_price = float(input("Enter unit price: ").strip())
float(unit_price)

subtotal = quantity * unit_price

tax_amount = subtotal * 0.085

order_total = subtotal + tax_amount



print("\nORDER SUMMARY")
print("=" * 6)
print(f"Customer: {customer_name}")
print(f"Email: {customer_email}")
print(f"Product: {product_name}")
print(f"Quantity: {quantity}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8.5%): ${tax_amount:.2f}")
print(f"Order Total: ${order_total:.2f}")