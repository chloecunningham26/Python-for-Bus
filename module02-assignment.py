#Chloe Cunningham
#Module 2 Assignment
#Calculate net price and total revenue project

product_name = "aerie sweatpants"
units_sold_str = "50000"     #int, not a string 
price_per_unit_str = "45.95"   #float, not a string
tax_rate = .07 #7% tax rate
discount_rate = .20 #20% off for students (us)

units_sold = 50000
price_per_unit = 45.95

int(50000)
#changed number of units sold from string to int

float(45.95)
#changes number per unit from string to a float


#add tax to original price 
taxed_price = price_per_unit + (price_per_unit * tax_rate)

#subtract student discount
net_price = taxed_price * (1 - discount_rate)

#calculate total revenue
total_revenue = net_price * units_sold

print(f"Product: aerie sweatpants")
print(f"Net Price: $39.33")
print(f"Total Revenue: $1966660.00")

