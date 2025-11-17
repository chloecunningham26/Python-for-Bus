# Module 6 Python Assingment
#Chloe Cunningham


print("=" * 60)
print("TECHRETAIL SALES ANALYSIS SYSTEM")
print("=" * 60)


# Sample quarterly sales data 
sales_data = [
    ["Smartphone Pro", "Phones", 899.99, 15, "E101"],
    ["Laptop Ultra", "Computers", 1299.99, 10, "E105"],
    ["Wireless Earbuds", "Audio", 149.99, 30, "E101"],
    ["Smart Watch", "Wearables", 249.99, 12, "E102"],
    ["Gaming Console", "Gaming", 499.99, 8, "E103"],
    ["Bluetooth Speaker", "Audio", 79.99, 25, "E102"],
    ["Tablet Lite", "Computers", 399.99, 18, "E104"],
    ["Digital Camera", "Cameras", 599.99, 5, "E105"],
    ["VR Headset", "Gaming", 299.99, 7, "E103"],
    ["Fitness Tracker", "Wearables", 129.99, 22, "E104"],
    ["Smartphone Plus", "Phones", 699.99, 20, "E101"],
    ["Laptop Basic", "Computers", 899.99, 14, "E105"]
]



# Employee info
# Format: {employee_id: [name, commission_rate]}
employees = {
    "E101": ["Alex Johnson", 0.05],
    "E102": ["Sarah Williams", 0.045],
    "E103": ["James Brown", 0.04],
    "E104": ["Lisa Davis", 0.05],
    "E105": ["Michael Wilson", 0.055]
}


# TODO: 1.1 Calculate total sales revenue
def calculate_total_sales():
    total = 0
    for item in sales_data:
        price = item[2]
        quantity = item[3]
        total += price * quantity
    return total


# 1.2 Calculate total sales for a specific category
def calculate_category_sales(category):
    total = 0
    for item in sales_data:
        if item[1] == category:
            total += item[2] * item[3]
    return total


# 1.3 Find best-selling product (by revenue)
def find_best_selling_product():
    best_product = None
    best_revenue = 0
    for item in sales_data:
        revenue = item[2] * item[3]
        if revenue > best_revenue:
            best_revenue = revenue
            best_product = item[0]
    return best_product, best_revenue



# 2.1 Calculate commission for a specific employee
def calculate_employee_commission(employee_id):
    commission_rate = employees[employee_id][1]
    total_sales = 0
    for item in sales_data:
        if item[4] == employee_id:
            total_sales += item[2] * item[3]
    return total_sales * commission_rate



# 2.2 Calculate total commission for all employees
def calculate_total_commission():
    total_commission = 0
    for emp_id in employees:
        total_commission += calculate_employee_commission(emp_id)
    return total_commission



# 3.1 Generate sales summary report
def generate_sales_summary(include_categories=True):
    report = f"Total Sales: ${calculate_total_sales():,.2f}\n"
    if include_categories:
        report += "Sales by Category:\n"
        categories = set(item[1] for item in sales_data)
        for category in sorted(categories):
            cat_sales = calculate_category_sales(category)
            report += f"  {category}: ${cat_sales:,.2f}\n"
    return report



# 3.2 Generate employee performance report
def generate_employee_report():
    report = ""
    for emp_id, (name, rate) in employees.items():
        sales = 0
        for item in sales_data:
            if item[4] == emp_id:
                sales += item[2] * item[3]
        commission = sales * rate
        report += f"{name} (ID: {emp_id}): Sales = ${sales:,.2f}, Commission = ${commission:,.2f}\n"
    return report



# 4.1 Get all products in a specific category
def get_products_by_category(category):
    result = []
    for row in sales_data:
        if row[1] == category:
            result.append(row)
    return result



# 4.2 Calculate average sale price (price * quantity per transaction)
def calculate_average_sale_price():
    total_revenue = 0
    total_quantity = 0
    for item in sales_data:
        total_revenue += item[2] * item[3]
        total_quantity += item[3]
    return total_revenue / total_quantity if total_quantity else 0



# Main program flow
def main():
    print("\nTECHRETAIL QUARTERLY SALES ANALYSIS")
    print("-" * 40)
    
    # Total sales
    print("\nTOTAL QUARTERLY SALES:")
    total_sales = calculate_total_sales()
    print(f"${total_sales:,.2f}")
    
    # Sales by category
    print("\nSALES BY CATEGORY:")
    categories = ["Phones", "Computers", "Audio", "Wearables", "Gaming", "Cameras"]
    for cat in categories:
        cat_sales = calculate_category_sales(cat)
        print(f"{cat}: ${cat_sales:,.2f}")
    
    # Best-selling product
    print("\nBEST-SELLING PRODUCT:")
    product, revenue = find_best_selling_product()
    print(f"{product} with revenue ${revenue:,.2f}")
    
    # Employee commissions
    print("\nEMPLOYEE COMMISSIONS:")
    for emp_id, (name, _) in employees.items():
        commission = calculate_employee_commission(emp_id)
        print(f"{name} (ID: {emp_id}): ${commission:,.2f}")
    
    # Sales summary report
    print("\nQUARTERLY SALES SUMMARY REPORT:")
    print(generate_sales_summary())
    
    # Employee performance report
    print("\nEMPLOYEE PERFORMANCE REPORT:")
    print(generate_employee_report())

if __name__ == "__main__":
    main()
