#Chloe Cunningham
# Module 11 Assignment: Data Visualization with Matplotlib
# SunCoast Retail Visual Analysis
#11/5/25

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("=" * 60)
print("SUNCOAST RETAIL VISUAL ANALYSIS")
print("=" * 60)

# ----- DATA CREATION -----
np.random.seed(42)


quarters = pd.date_range(start='2022-01-01', periods=8, freq='QE')
quarter_labels = ['Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022',
                  'Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023']

locations = ['Tampa', 'Miami', 'Orlando', 'Jacksonville']
categories = ['Electronics', 'Clothing', 'Home Goods', 'Sporting Goods', 'Beauty']

quarterly_data = []

for quarter_idx, quarter in enumerate(quarters):
    for location in locations:
        for category in categories:
            base_sales = np.random.normal(loc=100000, scale=20000)
            if quarter.quarter == 4:
                seasonal_factor = 1.3  # holiday boost
            elif quarter.quarter == 1:
                seasonal_factor = 0.8  # post-holiday dip
            else:
                seasonal_factor = 1.0

            location_factor = {
                'Tampa': 1.0,
                'Miami': 1.2,
                'Orlando': 0.9,
                'Jacksonville': 0.8
            }[location]

            category_factor = {
                'Electronics': 1.5,
                'Clothing': 1.0,
                'Home Goods': 0.8,
                'Sporting Goods': 0.7,
                'Beauty': 0.9
            }[category]

            growth_factor = (1 + 0.05/4) ** quarter_idx

            sales = base_sales * seasonal_factor * location_factor * category_factor * growth_factor
            sales = sales * np.random.normal(loc=1.0, scale=0.1)
            ad_spend = (sales ** 0.7) * 0.05 * np.random.normal(loc=1.0, scale=0.2)

            quarterly_data.append({
                'Quarter': quarter,
                'QuarterLabel': quarter_labels[quarter_idx],
                'Location': location,
                'Category': category,
                'Sales': round(sales, 2),
                'AdSpend': round(ad_spend, 2),
                'Year': quarter.year
            })

sales_df = pd.DataFrame(quarterly_data)
sales_df['Quarter_Num'] = sales_df['Quarter'].dt.quarter
sales_df['SalesPerDollarSpent'] = sales_df['Sales'] / sales_df['AdSpend']

# CUSTOMER DATA
customer_data = []
total_customers = 2000
age_params = {'Tampa': (45, 15), 'Miami': (35, 12), 'Orlando': (38, 14), 'Jacksonville': (42, 13)}

for location in locations:
    mean_age, std_age = age_params[location]
    customer_count = int(total_customers * {'Tampa': 0.3, 'Miami': 0.35, 'Orlando': 0.2, 'Jacksonville': 0.15}[location])
    ages = np.clip(np.random.normal(mean_age, std_age, customer_count), 18, 80).astype(int)
    for age in ages:
        if age < 30:
            category_pref = np.random.choice(categories, p=[0.3, 0.3, 0.1, 0.2, 0.1])
        elif age < 50:
            category_pref = np.random.choice(categories, p=[0.25, 0.2, 0.25, 0.15, 0.15])
        else:
            category_pref = np.random.choice(categories, p=[0.15, 0.1, 0.35, 0.1, 0.3])

        base_amount = np.random.gamma(5, 20)
        price_tier = np.random.choice(['Budget', 'Mid-range', 'Premium'], p=[0.3, 0.5, 0.2])
        tier_factor = {'Budget': 0.7, 'Mid-range': 1.0, 'Premium': 1.8}[price_tier]
        purchase_amount = base_amount * tier_factor
        customer_data.append({
            'Location': location,
            'Age': age,
            'Category': category_pref,
            'PurchaseAmount': round(purchase_amount, 2),
            'PriceTier': price_tier
        })

customer_df = pd.DataFrame(customer_data)

print("\nSales Data Sample:")
print(sales_df.head())
print("\nCustomer Data Sample:")
print(customer_df.head())
print("\nDataFrames ready for visualization!")

# ===============================================================
# VISUALIZATION FUNCTIONS
# ===============================================================

def plot_quarterly_sales_trend():
    fig, ax = plt.subplots()
    trend = sales_df.groupby('QuarterLabel')['Sales'].sum()
    ax.plot(trend.index, trend.values, marker='o', color='teal')
    ax.set_title("Overall Quarterly Sales Trend")
    ax.set_xlabel("Quarter")
    ax.set_ylabel("Total Sales ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

def plot_location_sales_comparison():
    fig, ax = plt.subplots()
    for loc in locations:
        loc_data = sales_df[sales_df['Location'] == loc].groupby('QuarterLabel')['Sales'].sum()
        ax.plot(loc_data.index, loc_data.values, marker='o', label=loc)
    ax.set_title("Quarterly Sales by Location")
    ax.set_xlabel("Quarter")
    ax.set_ylabel("Sales ($)")
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

def plot_category_performance_by_location():
    fig, ax = plt.subplots()
    grouped = sales_df.groupby(['Location', 'Category'])['Sales'].sum().unstack()
    grouped.plot(kind='bar', ax=ax)
    ax.set_title("Category Performance by Location")
    ax.set_xlabel("Location")
    ax.set_ylabel("Total Sales ($)")
    plt.tight_layout()
    return fig

def plot_sales_composition_by_location():
    fig, ax = plt.subplots()
    grouped = sales_df.groupby(['Location', 'Category'])['Sales'].sum().unstack()
    grouped.plot(kind='bar', stacked=True, ax=ax)
    ax.set_title("Sales Composition by Location")
    ax.set_xlabel("Location")
    ax.set_ylabel("Total Sales ($)")
    plt.tight_layout()
    return fig

def plot_ad_spend_vs_sales():
    fig, ax = plt.subplots()
    ax.scatter(sales_df['AdSpend'], sales_df['Sales'], color='purple', alpha=0.6)
    ax.set_title("Ad Spend vs Sales")
    ax.set_xlabel("Advertising Spend ($)")
    ax.set_ylabel("Sales ($)")
    plt.tight_layout()
    return fig

def plot_ad_efficiency_over_time():
    fig, ax = plt.subplots()
    efficiency = sales_df.groupby('QuarterLabel')['SalesPerDollarSpent'].mean()
    ax.plot(efficiency.index, efficiency.values, marker='o', color='orange')
    ax.set_title("Ad Efficiency Over Time")
    ax.set_xlabel("Quarter")
    ax.set_ylabel("Sales per $ Spent")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

def plot_customer_age_distribution():
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].hist(customer_df['Age'], bins=20, color='skyblue', edgecolor='black')
    axes[0].set_title("Overall Age Distribution")
    for loc in locations:
        axes[1].hist(customer_df[customer_df['Location'] == loc]['Age'], bins=15, alpha=0.6, label=loc)
    axes[1].set_title("Age by Location")
    axes[1].legend()
    for ax in axes:
        ax.set_xlabel("Age")
        ax.set_ylabel("Count")
    plt.tight_layout()
    return fig

def plot_purchase_by_age_group():
    fig, ax = plt.subplots()
    bins = [18, 30, 40, 50, 60, 80]
    labels = ['18-29', '30-39', '40-49', '50-59', '60+']
    customer_df['AgeGroup'] = pd.cut(customer_df['Age'], bins=bins, labels=labels, right=False)
    customer_df.boxplot(column='PurchaseAmount', by='AgeGroup', ax=ax, grid=False)
    plt.suptitle('')
    ax.set_title("Purchase Amounts by Age Group")
    ax.set_xlabel("Age Group")
    ax.set_ylabel("Purchase Amount ($)")
    plt.tight_layout()
    return fig

def plot_purchase_amount_distribution():
    fig, ax = plt.subplots()
    ax.hist(customer_df['PurchaseAmount'], bins=30, color='lightgreen', edgecolor='black')
    ax.set_title("Purchase Amount Distribution")
    ax.set_xlabel("Purchase Amount ($)")
    ax.set_ylabel("Count")
    plt.tight_layout()
    return fig

def plot_sales_by_price_tier():
    fig, ax = plt.subplots()
    tier_sales = customer_df.groupby('PriceTier')['PurchaseAmount'].sum()
    ax.pie(tier_sales, labels=tier_sales.index, autopct='%1.1f%%', startangle=90)
    ax.set_title("Sales by Price Tier")
    plt.tight_layout()
    return fig

def plot_category_market_share():
    fig, ax = plt.subplots()
    cat_sales = sales_df.groupby('Category')['Sales'].sum()
    ax.pie(cat_sales, labels=cat_sales.index, autopct='%1.1f%%', startangle=90)
    ax.set_title("Market Share by Category")
    plt.tight_layout()
    return fig

def plot_location_sales_distribution():
    fig, ax = plt.subplots()
    loc_sales = sales_df.groupby('Location')['Sales'].sum()
    ax.pie(loc_sales, labels=loc_sales.index, autopct='%1.1f%%', startangle=90)
    ax.set_title("Sales Distribution by Location")
    plt.tight_layout()
    return fig

def create_business_dashboard():
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    trend = sales_df.groupby('QuarterLabel')['Sales'].sum()
    axs[0, 0].plot(trend.index, trend.values, marker='o', color='teal')
    axs[0, 0].set_title("Quarterly Sales Trend")
    axs[0, 0].tick_params(axis='x', rotation=45)

    eff = sales_df.groupby('QuarterLabel')['SalesPerDollarSpent'].mean()
    axs[0, 1].plot(eff.index, eff.values, marker='o', color='orange')
    axs[0, 1].set_title("Ad Efficiency Over Time")
    axs[0, 1].tick_params(axis='x', rotation=45)

    tier_sales = customer_df.groupby('PriceTier')['PurchaseAmount'].sum()
    axs[1, 0].pie(tier_sales, labels=tier_sales.index, autopct='%1.1f%%', startangle=90)
    axs[1, 0].set_title("Sales by Price Tier")

    cat_sales = sales_df.groupby('Category')['Sales'].sum()
    axs[1, 1].pie(cat_sales, labels=cat_sales.index, autopct='%1.1f%%', startangle=90)
    axs[1, 1].set_title("Market Share by Category")

    plt.tight_layout()
    return fig

def main():
    print("\n" + "=" * 60)
    print("SUNCOAST RETAIL VISUAL ANALYSIS RESULTS")
    print("=" * 60)

    # Call functions
    plot_quarterly_sales_trend()
    plot_location_sales_comparison()
    plot_category_performance_by_location()
    plot_sales_composition_by_location()
    plot_ad_spend_vs_sales()
    plot_ad_efficiency_over_time()
    plot_customer_age_distribution()
    plot_purchase_by_age_group()
    plot_purchase_amount_distribution()
    plot_sales_by_price_tier()
    plot_category_market_share()
    plot_location_sales_distribution()
    create_business_dashboard()

    print("\nKEY INSIGHTS:")
    print("- Q4 peaks show strong holiday seasonality.")
    print("- Miami consistently leads in total sales.")
    print("- Electronics dominate overall sales share.")
    print("- Higher ad spend correlates with better sales.")
    print("- Premium tier customers bring in higher revenue.")

    plt.show()

if __name__ == "__main__":
    main()
    
      
#matplotlib installed
#answered all questions needed within code
#all data stored into two dataframes sales_df and customer_df to organize and tell difference of
#this was the most difficult assignment for me yet

