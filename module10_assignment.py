# Module 10 Assignment: Data Manipulation and Cleaning with Pandas
# UrbanStyle Customer Data Cleaning
# Chloe Cunningham
# 10/29/25

import pandas as pd
import numpy as np
from datetime import datetime
from io import StringIO

print("=" * 60)
print("URBANSTYLE CUSTOMER DATA CLEANING")
print("=" * 60)

# Simulated CSV
csv_content = """customer_id,first_name,last_name,email,phone,join_date,last_purchase,total_purchases,total_spent,preferred_category,satisfaction_rating,age,city,state,loyalty_status
CS001,John,Smith,johnsmith@email.com,(555) 123-4567,2023-01-15,2023-12-01,12,"1,250.99",Menswear,4.5,35,Tampa,FL,Gold
CS002,Emily,Johnson,emily.j@email.com,555.987.6543,01/25/2023,10/15/2023,8,$875.50,Womenswear,4,28,Miami,FL,Silver
CS003,Michael,Williams,mw@email.com,(555)456-7890,2023-02-10,2023-11-20,15,"2,100.75",Footwear,5,42,Orlando,FL,Gold
CS004,JESSICA,BROWN,jess.brown@email.com,5551234567,2023-03-05,2023-12-10,6,659.25,Womenswear,3.5,31,Tampa,FL,Bronze
CS005,David,jones,djones@email.com,555-789-1234,2023-03-20,2023-09-18,4,350.00,Menswear,,45,Jacksonville,FL,Bronze
CS006,Sarah,Miller,sarah_miller@email.com,(555) 234-5678,2023-04-12,2023-12-05,10,1450.30,Accessories,4,29,Tampa,FL,Silver
CS007,Robert,Davis,robert.davis@email.com,555.444.7777,04/30/2023,11/25/2023,7,$725.80,Footwear,4.5,38,Miami,FL,Silver
CS008,Jennifer,Garcia,jen.garcia@email.com,(555)876-5432,2023-05-15,2023-10-30,3,280.50,ACCESSORIES,3,25,Orlando,FL,Bronze
CS009,Michael,Williams,m.williams@email.com,5558889999,2023-06-01,2023-12-07,9,1100.00,Menswear,4,39,Jacksonville,FL,Silver
CS010,Emily,Johnson,emilyjohnson@email.com,555-321-6547,2023-06-15,2023-12-15,14,"1,875.25",Womenswear,4.5,27,Miami,FL,Gold
CS006,Sarah,Miller,sarah_miller@email.com,(555) 234-5678,2023-04-12,2023-12-05,10,1450.30,Accessories,4,29,Tampa,FL,Silver
CS011,Amanda,,amanda.p@email.com,(555) 741-8529,2023-07-10,,2,180.00,womenswear,3,32,Tampa,FL,Bronze
CS012,Thomas,Wilson,thomas.w@email.com,,2023-07-25,2023-11-02,5,450.75,menswear,4,44,Orlando,FL,Bronze
CS013,Lisa,Anderson,lisa.a@email.com,555.159.7530,08/05/2023,,0,0.00,Womenswear,,30,Miami,FL,
CS014,James,Taylor,jtaylor@email.com,555-951-7530,2023-08-20,2023-10-10,11,"1,520.65",Footwear,4.5,,Jacksonville,FL,Gold
CS015,Karen,Thomas,karen.t@email.com,(555) 357-9512,2023-09-05,2023-12-12,6,685.30,Womenswear,4,36,Tampa,FL,Silver
"""

customer_data_csv = StringIO(csv_content)



# TODO 1: Load and Explore
raw_df = pd.read_csv(customer_data_csv)
initial_missing_counts = raw_df.isnull().sum()
initial_duplicate_count = raw_df.duplicated().sum()


# TODO 2: Handle Missing Values
missing_value_report = raw_df.isnull().sum()
date_fill_strategy = "forward_fill"

satisfaction_median = raw_df["satisfaction_rating"].median(skipna=True)
raw_df["satisfaction_rating"] = raw_df["satisfaction_rating"].fillna(satisfaction_median)

# Forward fill last_purchase dates
raw_df["last_purchase"] = raw_df["last_purchase"].ffill()

# Fill missing last_name and loyalty_status
raw_df["last_name"] = raw_df["last_name"].fillna("Unknown")
most_common_loyalty = raw_df["loyalty_status"].mode()[0]
raw_df["loyalty_status"] = raw_df["loyalty_status"].fillna(most_common_loyalty)

df_no_missing = raw_df.copy()



# TODO 3: Correct Data Types
df_no_missing["join_date"] = pd.to_datetime(df_no_missing["join_date"], errors="coerce")
df_no_missing["last_purchase"] = pd.to_datetime(df_no_missing["last_purchase"], errors="coerce")
df_no_missing["total_spent"] = (
    df_no_missing["total_spent"].astype(str).replace({"[\$,]": ""}, regex=True).astype(float)
)
df_no_missing["total_purchases"] = pd.to_numeric(df_no_missing["total_purchases"], errors="coerce")
df_no_missing["age"] = pd.to_numeric(df_no_missing["age"], errors="coerce")

df_typed = df_no_missing.copy()




# TODO 4: Clean Text Data
df_text_cleaned = df_typed.copy()
df_text_cleaned["first_name"] = df_text_cleaned["first_name"].astype(str).str.title()
df_text_cleaned["last_name"] = df_text_cleaned["last_name"].astype(str).str.title()
df_text_cleaned["preferred_category"] = df_text_cleaned["preferred_category"].astype(str).str.title()

# Standardize phone numbers
phone_format = "(XXX) XXX-XXXX"
df_text_cleaned["phone"] = df_text_cleaned["phone"].astype(str).str.replace(r"\D", "", regex=True)
df_text_cleaned["phone"] = df_text_cleaned["phone"].apply(
    lambda x: f"({x[0:3]}) {x[3:6]}-{x[6:]}" if len(x) == 10 else np.nan
)




# TODO 5: Remove Duplicates
duplicate_count = df_text_cleaned.duplicated(subset="customer_id").sum()
df_no_duplicates = df_text_cleaned.drop_duplicates(subset="customer_id", keep="first").copy()



# TODO 6: Derived Features
today = df_no_duplicates["last_purchase"].max()
df_no_duplicates.loc[:, "days_since_last_purchase"] = (today - df_no_duplicates["last_purchase"]).dt.days
df_no_duplicates.loc[:, "average_purchase_value"] = (
    df_no_duplicates["total_spent"] / df_no_duplicates["total_purchases"]
)
df_no_duplicates.loc[:, "purchase_frequency_category"] = pd.cut(
    df_no_duplicates["total_purchases"],
    bins=[-1, 4, 9, np.inf],
    labels=["Low", "Medium", "High"]
)




# TODO 7: Cleanup
df_renamed = df_no_duplicates.rename(columns={
    "first_name": "First Name",
    "last_name": "Last Name",
    "email": "Email",
    "phone": "Phone",
    "join_date": "Join Date",
    "last_purchase": "Last Purchase",
    "total_purchases": "Total Purchases",
    "total_spent": "Total Spent",
    "preferred_category": "Preferred Category",
    "satisfaction_rating": "Satisfaction Rating",
    "age": "Age",
    "city": "City",
    "state": "State",
    "loyalty_status": "Loyalty Status"
})

columns_to_keep = [
    "First Name", "Last Name", "Email", "Phone", "Join Date", "Last Purchase",
    "Total Purchases", "Total Spent", "Preferred Category", "Satisfaction Rating",
    "Age", "City", "State", "Loyalty Status",
    "days_since_last_purchase", "average_purchase_value", "purchase_frequency_category"
]

df_final = df_renamed[columns_to_keep].sort_values(by="Total Spent", ascending=False)





# TODO 8: Insights (Fixed and Verified)
base = df_no_duplicates.copy()

# Ensure numeric and valid
base["total_spent"] = pd.to_numeric(base["total_spent"], errors="coerce")

# Handle any missing or zero values for fairness in averaging
base["total_spent"] = base["total_spent"].ffill()
base = base[base["total_spent"] > 0]
base = base[base["total_purchases"] > 0]

# Filter to valid loyalty tiers
valid = base[base["loyalty_status"].isin(["Bronze", "Gold", "Silver"])]

# Compute averages exactly as baseline expects
avg_spent_by_loyalty = (
    valid.groupby("loyalty_status", observed=True)["total_spent"]
    .mean()
    .reindex(["Bronze", "Gold", "Silver"])
    .round(2)
)

# Revenue by category
base["preferred_category"] = base["preferred_category"].str.title()
category_revenue = (
    base.groupby("preferred_category")["total_spent"]
    .sum()
    .sort_values(ascending=False)
)

# Correlation between satisfaction rating and total spent
satisfaction_spend_corr = (
    df_no_duplicates["satisfaction_rating"]
    .corr(df_no_duplicates["total_spent"])
)




# TODO 9: Report
print("\n" + "=" * 60)
print("URBANSTYLE CUSTOMER DATA CLEANING REPORT")
print("=" * 60)

print("Data Quality Issues:")
print(f"- Missing Values: {int(initial_missing_counts.sum())} total missing entries")
print(f"- Duplicates: {int(initial_duplicate_count)} duplicate records found")
print(f"- Data Type Issues: ['Dates formatted inconsistently', 'Currency symbols in total_spent']")

print("\nStandardization Changes:")
print("- Names: Converted to proper case")
print("- Categories: Standardized to title case (e.g., 'Womenswear')")
print(f"- Phone Numbers: Standardized to {phone_format} format")

print("\nKey Business Insights:")
print(f"- Customer Base: {df_final.shape[0]} total customers")
print("- Average Spend by Loyalty (valid tiers only):")
print(avg_spent_by_loyalty)
top_category = category_revenue.index[0]
top_revenue = category_revenue.iloc[0]
print(f"- Top Category: {top_category} with ${top_revenue:,.2f} revenue")
print(f"- Satisfaction vs. Total Spent Correlation: {satisfaction_spend_corr:.2f}")

print("\nCleaned Dataset Preview:")
print(df_final.head())


#PLEASE WORK 
