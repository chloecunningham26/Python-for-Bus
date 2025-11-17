#Chloe Cunningham
#Python for business Module 5 Assignment 
#Sept 24 2025


# Welcome message
print("=" * 60)
print("QUICKMART SALES ANALYSIS")
print("=" * 60)

# Monthly sales data per store (in thousands of dollars)
# Data structure: Dictionary with store locations as keys
# Each store contains a list of 12 monthly sales figures (Jan-Dec)
sales_data = {
    "Downtown": [120.5, 115.8, 131.2, 140.5, 150.2, 160.1, 155.3, 148.9, 152.5, 160.8, 165.2, 180.3],
    "Suburb Mall": [85.6, 90.2, 93.5, 100.8, 110.5, 115.7, 120.2, 118.5, 125.6, 130.2, 140.8, 155.5],
    "Westside": [95.2, 88.7, 92.3, 100.5, 105.8, 110.2, 115.7, 120.5, 125.8, 130.2, 135.5, 145.8],
    "University": [55.3, 60.2, 65.8, 70.5, 65.2, 50.1, 45.2, 55.8, 80.5, 85.9, 90.2, 95.3]
}

# Store locations
locations = list(sales_data.keys())

# List of month names for reporting
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"
]



# Calculate the total sales for each month across all stores
# Initialize a list to store the total monthly sales
monthly_totals = []
for month_index in range(12):
    total = 0 
    for store in locations:
        total += sales_data[store][month_index]
    monthly_totals.append(total)  # ← must be inside the loop


# TODO 2: Find the month with the highest and lowest total sales
# Initialize variables to track highest and lowest sales
highest_month_index = 0
lowest_month_index = 0
highest_sales = float('-inf')
lowest_sales = float('inf')

for i in range(12):
    if monthly_totals[i] > highest_sales:
        highest_sales = monthly_totals[i]
        highest_month_index = i
    if monthly_totals[i] < lowest_sales:
        lowest_sales = monthly_totals[i]
        lowest_month_index = i
        
#help i dont understand this one
        
        
#calculate all monthly sales across stores 
average_monthly_sales = sum(monthly_totals) / len(monthly_totals)




# Find the store with the highest annual sales
best_store = ""
best_store_sales = 0

for store in locations:
    total_sales = sum(sales_data[store])
    if total_sales > best_store_sales:
        best_store_sales = total_sales
        best_store = store 

# Create performance report from monthly sales
performance_report = []
for i in range(12):
    if monthly_totals[i] > average_monthly_sales:
        performance_report.append(f"{months[i]}: {monthly_totals[i]:.2f} (Above Average)")
    else:
            performance_report.append(f"{months[i]}: {monthly_totals[i]:.2f} (Below Average)")
        
#bonus- try it??
longest_growth_streak = 0
growth_streak_start = 0

current_streak = 0
current_start = 0

for i in range(1, 12):
    if monthly_totals[i] > monthly_totals[i-1]:
        current_streak += 1
        if current_streak > longest_growth_streak:
            longest_growth_streak = current_streak
            growth_streak_start = current_start
            
    else:
        current_streak = 1
        current_start = i
    
    
    
    
#sum it all up
print("\n" + "=" * 60)
print("QUICKMART SALES ANALYSIS SUMMARY")
print("=" * 60)
print("\nPerformance Report:")
for line in performance_report:
    print(line)
    
print("=" * 60)
print(f"Best Month: {months[highest_month_index]} (${highest_sales:.2f})")
print(f"Worst Month: {months[lowest_month_index]} (${lowest_sales:.2f})")
print(f"Average Monthly Sales: ${average_monthly_sales:.2f}")
print(f"Best Performing Store: {best_store} (${best_store_sales:.2f})")
if longest_growth_streak > 1:
    print(f"\nLongest Growth Streak: {longest_growth_streak} months "
          f"(starting in {months[growth_streak_start]})")
    
else:
        print("\nNo consecutive growth streaks found.")



