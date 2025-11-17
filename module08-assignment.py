# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
# Store in variable: services
# Include at least 5 different services

services = {
    "Web Development": 150,
    "App Development": 140,
    "Data Analysis": 175,
    "Software Integration": 160,
    "IoT Implementation": 200
}



# TODO 2: Create customer dictionaries
# Each customer should have: company_name, contact_person, email, phone

customer1 = {
    "company_name": "TechNova Solutions",
    "contact_person": "Tara Johnson",
    "email": "liam.johnson@technova.com",
    "phone": "412-238-7491"
}

customer2 = {
    "company_name": "GreenWave Analytics",
    "contact_person": "Sophia Martinez",
    "email": "sophia.martinez@greenwave.io",
    "phone": "412-660-8932"
}

customer3 = {
    "company_name": "BlueSky Retailers",
    "contact_person": "Noah Kim",
    "email": "noah.kim@blueskyretail.com",
    "phone": "412-903-1248"
}

customer4 = {
    "company_name": "NextGen Manufacturing",
    "contact_person": "Emma Davis",
    "email": "emma.davis@nextgenmfg.com",
    "phone": "412-672-4159"
}







# TODO 3: Create a master customers dictionary
# Store in variable: customers
# Use customer IDs as keys and customer dictionaries as values
# Example: customers = {"C001": customer1, "C002": customer2, ...}

customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}








# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)
# Add your code here to display all customer information
for customer_id, customer_info in customers.items():
    print(f"\nCustomer ID: {customer_id}")
    print(f"  Company Name: {customer_info['company_name']}")
    print(f"  Contact Person: {customer_info['contact_person']}")
    print(f"  Email: {customer_info['email']}")
    print(f"  Phone: {customer_info['phone']}")





# TODO 5: Look up specific customers
# Use dictionary access to:
# - Get and display customer C002's information (store in c002_info)
# - Get and display customer C003's contact person (store in c003_contact)
# - Try to get customer C999 (doesn't exist) using .get() with a default message (store in c999_info)

print("\n\nCustomer Lookups:")
print("-" * 60)
# Add your code here
# Get customer C002's full information
c002_info = customers["C002"]

# Get customer C003's contact person
c003_contact = customers["C003"]["contact_person"]

# Try to get a non-existent customer safely using .get()
c999_info = customers.get("C999", "Customer not found.")

# Display the retrieved information
print("Customer C002 Information:")
print(c002_info)

print("\nCustomer C003 Contact Person:")
print(c003_contact)

print("\nCustomer C999 Lookup Result:")
print(c999_info)




# TODO 6: Update customer information
# - Change customer C001's phone number
# - Add a new field "industry" to customer C002
# - Display the updated customer information

print("\n\nUpdating Customer Information:")
print("-" * 60)
# Add your code here

# Change customer C001's phone number
customers["C001"]["phone"] = "555-987-4321"

# Add a new field "industry" to customer C002
customers["C002"]["industry"] = "Data Analytics"

# Display updated information for C001 and C002
print("Updated Customer C001 Information:")
for key, value in customers["C001"].items():
    print(f"  {key.capitalize()}: {value}")

print("\nUpdated Customer C002 Information:")
for key, value in customers["C002"].items():
    print(f"  {key.capitalize()}: {value}")




# TODO 7: Create project dictionaries for each customer
# Each project: {"name": "Project Name", "service": "Service Type", "hours": X, "budget": Y}
# Create a projects dictionary where customer IDs map to lists of projects
# Store in variable: projects
# Example: projects = {"C001": [project1, project2], "C002": [project3], ...}

print("\n\nProject Information:")
print("-" * 60)
# Add your code here
# Define individual projects
project1 = {"name": "E-Commerce Website", "service": "Web Development", "hours": 120, "budget": 18000}
project2 = {"name": "Mobile App Upgrade", "service": "App Development", "hours": 90, "budget": 12600}
project3 = {"name": "Data Visualization Dashboard", "service": "Data Analysis", "hours": 75, "budget": 13125}
project4 = {"name": "Retail Automation System", "service": "Software Integration", "hours": 150, "budget": 24000}
project5 = {"name": "IoT Smart Factory Setup", "service": "IoT Implementation", "hours": 200, "budget": 40000}

# Assign projects to customers
projects = {
    "C001": [project1, project2],
    "C002": [project3],
    "C003": [project4],
    "C004": [project5]
}

# Optional: Display all projects neatly
print("=== Projects by Customer ===")
for customer_id, project_list in projects.items():
    print(f"\nCustomer ID: {customer_id}")
    for project in project_list:
        print(f"  Project: {project['name']} | Service: {project['service']} | Hours: {project['hours']} | Budget: ${project['budget']}")



# TODO 8: Calculate project costs
# For each project, calculate: cost = hourly_rate * hours
# Display each project with its calculated cost

print("\n\nProject Cost Calculations:")
print("-" * 60)
# Add your code here
print("=== Project Cost Calculations ===")

for customer_id, project_list in projects.items():
    print(f"\nCustomer ID: {customer_id}")
    for project in project_list:
        service_type = project["service"]
        hours = project["hours"]
        hourly_rate = services.get(service_type, 0)  # get hourly rate from services dictionary
        cost = hourly_rate * hours
        project["calculated_cost"] = cost  # store the cost inside the project dictionary
        print(f"  Project: {project['name']}")
        print(f"    Service: {service_type}")
        print(f"    Hours: {hours}")
        print(f"    Hourly Rate: ${hourly_rate}")
        print(f"    Calculated Cost: ${cost}")








# TODO 9: Customer statistics using dictionary methods
# Display:
# - All customer IDs using .keys()
# - All customer companies using .values() and extracting company names
# - Count of total customers using len()

print("\n\nCustomer Statistics:")
print("-" * 60)
# Add your code here
# Get all customer IDs
customer_ids = customers.keys()

# Get all customer company names
customer_companies = [customer["company_name"] for customer in customers.values()]

# Get total number of customers
total_customers = len(customers)

# Display results
print("=== Customer Statistics ===")
print(f"Customer IDs: {list(customer_ids)}")
print(f"Customer Companies: {customer_companies}")
print(f"Total Number of Customers: {total_customers}")



# TODO 10: Service usage analysis
# Create a dictionary that counts how many projects use each service
# Store in variable: service_counts
# Display the service usage counts

print("\n\nService Usage Analysis:")
print("-" * 60)
# Add your code here
service_counts = {}

# Loop through all projects for each customer
for project_list in projects.values():
    for project in project_list:
        service = project["service"]
        service_counts[service] = service_counts.get(service, 0) + 1

# Display the service usage counts
print("=== Service Usage Analysis ===")
for service, count in service_counts.items():
    print(f"{service}: {count} project(s)")


# TODO 11: Financial aggregations # Calculate and display: # - Total hours across all projects (store in total_hours) # - Total budget across all projects (store in total_budget) # - Average project budget (store in avg_budget) # - Most expensive and least expensive projects (store in max_budget, min_budget) print("\n\nFinancial Summary:") print("-" * 60) # Flatten all projects into a single list (include every project for every customer) all_projects = [project for project_list in projects.values() for project in project_list] # Global aggregations (calculated once and never overwritten later) total_hours = sum(project["hours"] for project in all_projects) total_budget = sum(project["budget"] for project in all_projects) avg_budget = total_budget / len(all_projects) if all_projects else 0 max_budget = max((project["budget"] for project in all_projects), default=0) min_budget = min((project["budget"] for project in all_projects), default=0) # Debug prints (these should match your test expectations) print("=== Financial Aggregations ===") print(f"Total Hours Across All Projects: {total_hours}") print(f"Total Budget Across All Projects: ${total_budget}") print(f"Average Project Budget: ${avg_budget:.2f}") print(f"Most Expensive Project Budget: ${max_budget}") print(f"Least Expensive Project Budget: ${min_budget}") print(f"\nDEBUG CHECK - total_budget right after aggregation: {total_budget}") # Optional assertions to catch problems early (safe to keep while debugging) # Remove or comment these out once tests pass. assert total_hours == 635, f"Unexpected total_hours: {total_hours} (expected 635)" assert total_budget == 107725, f"Unexpected total_budget: {total_budget} (expected 107725)"
# TODO 11: Financial aggregations
# Calculate and display:
# - Total hours across all projects (store in total_hours)
# - Total budget across all projects (store in total_budget)
# - Average project budget (store in avg_budget)
# - Most expensive and least expensive projects (store in max_budget, min_budget)

print("\n\nFinancial Summary:")
print("-" * 60)

# Flatten all projects into a single list (include every project for every customer)
all_projects = [p for plist in projects.values() for p in p list]

# Perform global financial aggregations
total_hours = sum(p["hours"] for p in all_projects)
total_budget = sum(p["budget"] for p in all_projects)
avg_budget = total_budget / len(all_projects) if all_projects else 0
max_budget = max((p["budget"] for p in all_projects), default=0)
min_budget = min((p["budget"] for p in all_projects), default=0)

# Display summary
print("=== Financial Aggregations ===")
print(f"Total Hours Across All Projects: {total_hours}")
print(f"Total Budget Across All Projects: ${total_budget}")
print(f"Average Project Budget: ${avg_budget:.2f}")
print(f"Most Expensive Project Budget: ${max_budget}")
print(f"Least Expensive Project Budget: ${min_budget}")

#Assertions to match test expectations
assert total_hours == 635, f"total_hours incorrect (found {total_hours}, expected 635)"
assert total_budget == 107725, f"total_budget incorrect (found {total_budget}, expected 107725)"


# TODO 12: Customer summary report
# ---------------------------
print("\n\nCustomer Summary Report:")
print("-" * 60)
print("=== Customer Summary Report ===")

for customer_id, customer_info in customers.items():
    # Get all projects for this customer (may be empty list)
    customer_projects = projects.get(customer_id, [])
    
    # Customer-specific totals: use names that don't conflict with the global ones
    customer_num_projects = len(customer_projects)
    customer_total_hours = sum(project["hours"] for project in customer_projects)
    customer_total_budget = sum(p["budget"] for p in customer_projects)
    
    # Display customer details (unchanged)
    print(f"\nCustomer ID: {customer_id}")
    print(f"  Company Name: {customer_info['company_name']}")
    print(f"  Contact Person: {customer_info['contact_person']}")
    print(f"  Email: {customer_info['email']}")
    print(f"  Phone: {customer_info['phone']}")
    if "industry" in customer_info:
        print(f"  Industry: {customer_info['industry']}")
    
    # Display per-customer project summary
    print(f"  Number of Projects: {customer_num_projects}")
    print(f"  Total Hours: {customer_total_hours}")
    print(f"  Total Budget: ${customer_total_budget}")



# TODO 13: Create rate adjustments using dictionary comprehension
# Create a new dictionary with all service rates increased by 10%
# Store in variable: adjusted_rates
# Use dictionary comprehension: adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
# Add your code here
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}
for service, rate in adjusted_rates.items():
    print(f"{service}: ${rate:.2f}")







# TODO 14: Filter customers using dictionary comprehension
# Create a dictionary of only customers who have projects
# Store in variable: active_customers
# Hint: Use the projects dictionary to check which customers have projects

print("\n\nActive Customers (with projects):")
print("-" * 60)
# Add your code here
active_customers = {customer_id: customer_info 
                    for customer_id, customer_info in customers.items() 
                    if projects.get(customer_id)}  # Only include if customer has projects

for customer_id, info in active_customers.items():
    print(f"{customer_id}: {info['company_name']}")









# TODO 15: Create project summaries using dictionary comprehension
# Create a dictionary mapping customer IDs to their total project budgets
# Store in variable: customer_budgets
# Example result: {"C001": 25000, "C002": 15000, ...}

print("\n\nCustomer Budget Totals:")
print("-" * 60)
# Add your code here
customer_budgets = {customer_id: sum(project["budget"] for project in project_list) 
                    for customer_id, project_list in projects.items()}

# Display customer budget summaries
for customer_id, total in customer_budgets.items():
    print(f"{customer_id}: ${total_budget}")









# TODO 16: Service pricing tiers using dictionary comprehension
# Create a dictionary categorizing services as "Premium" (>= 200), "Standard" (100-199), or "Basic" (< 100)
# Store in variable: service_tiers
# Use conditional expressions in the comprehension

print("\n\nService Pricing Tiers:")
print("-" * 60)
# Add your code here
service_tiers = {service: ("Premium" if rate >= 200 else "Standard" if rate >= 100 else "Basic")
                 for service, rate in services.items()}

# Display service tiers
for service, tier in service_tiers.items():
    print(f"{service}: {tier}")








# TODO 17: Customer validation function
# Create a function validate_customer(customer_dict) that:
# - Checks if all required fields are present (company_name, contact_person, email, phone)
# - Returns True if valid, False otherwise
# - Use conditional logic to verify each field
# Test it on all customers and report results

print("\n\nCustomer Validation:")
print("-" * 60)
# Add your code here
def validate_customer(customer_dict):
    """
    Validates that a customer dictionary contains all required fields.
    Required fields: company_name, contact_person, email, phone
    Returns True if valid, False otherwise.
    """
    required_fields = ["company_name", "contact_person", "email", "phone"]
    for field in required_fields:
        if field not in customer_dict or not customer_dict[field]:
            return False
    return True

# Test the function on all customers and report results
for customer_id, customer_info in customers.items():
    is_valid = validate_customer(customer_info)
    status = "Valid" if is_valid else "Invalid"
    print(f"{customer_id} ({customer_info['company_name']}): {status}")


# TODO 18: Project status tracking with loops and conditionals
# Add a "status" field to each project ("active", "completed", "pending")
# Use a loop to count projects by status
# Store counts in status_counts dictionary
# Display a summary of project statuses
print("\n\nProject Status Summary:")
print("-" * 60)
import random

statuses = ["active", "completed", "pending"]

# Add a "status" field randomly for demonstration
for project_list in projects.values():
    for project in project_list:
        project["status"] = random.choice(statuses)

# Initialize status_counts with all statuses
status_counts = {status: 0 for status in statuses}

# Count projects by status
for project_list in projects.values():
    for project in project_list:
        status_counts[project["status"]] += 1

# Display summary
for status, count in status_counts.items():
    print(f"{status.capitalize()}: {count} project(s)")






# TODO 19: Budget analysis function with aggregation
# Create a function analyze_customer_budgets(projects_dict) that:
# - Takes the projects dictionary as input
# - Uses loops to calculate total and average budget per customer
# - Returns a dictionary with customer IDs as keys and budget stats as values
# - Each value should be a dict with 'total', 'average', and 'count' keys

print("\n\nDetailed Budget Analysis:")
print("-" * 60)
# Add your code here
def analyze_customer_budgets(projects_dict):
    """
    Analyzes budgets per customer.
    Returns a dictionary with customer IDs as keys and a dictionary as value:
    {
        'total': total budget,
        'average': average budget,
        'count': number of projects
    }
    """
    budget_analysis = {}
    
    for customer_id, project_list in projects_dict.items():
        total_budget = sum(project["budget"] for project in project_list)
        project_count = len(project_list)
        average_budget = total_budget / project_count if project_count else 0
        budget_analysis[customer_id] = {
            "total": total_budget,
            "average": average_budget,
            "count": project_count
        }
    
    return budget_analysis

# Use the function and display results
budget_stats = analyze_customer_budgets(projects)

for customer_id, stats in budget_stats.items():
    print(f"Customer {customer_id}:")
    print(f"  Number of Projects: {stats['count']}")
    print(f"  Total Budget: ${stats['total']}")
    print(f"  Average Budget: ${stats['average']:.2f}")
    print("-" * 60)


# TODO 20: Service recommendation system
# Create a function recommend_services(customer_id, customers, projects, services) that:
# - Analyzes the customer's past projects
# - Identifies services they haven't used yet
# - Returns a list of recommended services based on their budget range
# - Use loops, conditionals, and dictionary operations

print("\n\nService Recommendations:")
print("-" * 60)
# Add your code here
def recommend_services(customer_id, customers, projects, services):
    """
    Recommends services to a customer based on past projects.
    
    - Identifies services the customer hasn't used yet.
    - Recommends services within the budget range of their past projects.
    """
    if customer_id not in customers:
        return f"Customer {customer_id} not found."
    
    customer_projects = projects.get(customer_id, [])
    
    if not customer_projects:
        # If no past projects, recommend all services
        return list(services.keys())
    
    # Identify services already used
    used_services = set(project["service"] for project in customer_projects)
    
    # Determine budget range based on past projects
    budgets = [project["budget"] for project in customer_projects]
    min_budget, max_budget = min(budgets), max(budgets)
    
    # Recommend services not yet used and within budget range
    recommended_services = []
    for service, rate in services.items():
        # Estimate cost if 10 hours minimum, for demonstration
        estimated_cost = rate * 10
        if service not in used_services and min_budget <= estimated_cost <= max_budget:
            recommended_services.append(service)
    
    return recommended_services

# Example usage
for cid in customers.keys():
    rec_services = recommend_services(cid, customers, projects, services)
    print(f"{cid} ({customers[cid]['company_name']}): Recommended Services -> {rec_services}")








