#Module 12 Assignment: Green Grocer Data Analysis 
#Python for Buss
#Chloe cunningham
#Nov 12 2025

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
#Data Creation 
# ------------------------------
np.random.seed(42)

stores = ["Tampa", "Orlando", "Miami", "Jacksonville", "Gainesville"]
store_data = {
    "Store": stores,
    "SquareFootage": [15000, 12000, 18000, 10000, 8000],
    "StaffCount": [45, 35, 55, 30, 25],
    "YearsOpen": [5, 3, 7, 2, 1],
    "WeeklyMarketingSpend": [2500, 2000, 3000, 1800, 1500]
}
store_df = pd.DataFrame(store_data)

departments = ["Produce", "Dairy", "Bakery", "Grocery", "Prepared Foods"]
categories = {
    "Produce": ["Organic Vegetables", "Organic Fruits", "Fresh Herbs"],
    "Dairy": ["Milk & Cream", "Cheese", "Yogurt"],
    "Bakery": ["Bread", "Pastries", "Cakes"],
    "Grocery": ["Grains", "Canned Goods", "Snacks"],
    "Prepared Foods": ["Hot Bar", "Salad Bar", "Sandwiches"]
}

store_perf = {"Tampa":1.0, "Orlando":0.85, "Miami":1.2, "Jacksonville":0.75, "Gainesville":0.65}
dept_perf = {"Produce":1.2, "Dairy":1.0, "Bakery":0.85, "Grocery":0.95, "Prepared Foods":1.1}

# Reduced date range for memory
dates = pd.date_range("2023-01-01","2023-06-30")
sales_data = []

for date in dates:
    month = date.month
    seasonal = 1.0
    if month in [6,7,8]: seasonal = 1.15
    elif month==12: seasonal=1.25
    elif month in [1,2]: seasonal=0.9
    dow = 1.3 if date.dayofweek>=5 else 1.0
    
    for store in stores:
        sf = store_perf[store]
        for dept in departments:
            dfp = dept_perf[dept]
            for cat in categories[dept]:
                base_sales = np.random.normal(500,100)
                sales = base_sales*sf*dfp*seasonal*dow*np.random.normal(1.0,0.1)
                base_margin = {"Produce":0.25,"Dairy":0.22,"Bakery":0.35,"Grocery":0.20,"Prepared Foods":0.40}[dept]
                profit_margin = max(min(base_margin*np.random.normal(1.0,0.05),0.5),0.15)
                profit = sales*profit_margin
                sales_data.append({"Date":date,"Store":store,"Department":dept,"Category":cat,
                                   "Sales":round(sales,2),"ProfitMargin":round(profit_margin,4),"Profit":round(profit,2)})

sales_df = pd.DataFrame(sales_data)




# Customer Data
customer_data = []
segments = ["Health Enthusiast","Gourmet Cook","Family Shopper","Budget Organic","Occasional Visitor"]
segment_prob = [0.25,0.20,0.30,0.15,0.10]
store_prob = {"Tampa":0.25,"Orlando":0.20,"Miami":0.30,"Jacksonville":0.15,"Gainesville":0.10}

for i in range(1000):  # Reduced number of customers
    age = int(np.random.normal(42,15)); age=max(18,min(age,85))
    gender = np.random.choice(["M","F"],p=[0.48,0.52])
    income = int(np.random.normal(85,30))*1000; income=max(income,20000)
    segment = np.random.choice(segments,p=segment_prob)
    pref_store = np.random.choice(stores,p=list(store_prob.values()))
    
    if segment=="Health Enthusiast": freq=np.random.randint(8,15); basket=np.random.normal(75,15)
    elif segment=="Gourmet Cook": freq=np.random.randint(4,10); basket=np.random.normal(120,25)
    elif segment=="Family Shopper": freq=np.random.randint(5,12); basket=np.random.normal(150,30)
    elif segment=="Budget Organic": freq=np.random.randint(6,10); basket=np.random.normal(60,10)
    else: freq=np.random.randint(1,5); basket=np.random.normal(45,15)
    
    freq=max(1,min(freq,30)); basket=max(basket,15)
    monthly_spend = freq*basket
    if monthly_spend>1000: loyalty="Platinum"
    elif monthly_spend>500: loyalty="Gold"
    elif monthly_spend>200: loyalty="Silver"
    else: loyalty="Bronze"
    
    customer_data.append({"CustomerID":f"C{i+1:04d}","Age":age,"Gender":gender,"Income":income,
                          "Segment":segment,"PreferredStore":pref_store,"VisitsPerMonth":freq,
                          "AvgBasketSize":round(basket,2),"MonthlySpend":round(monthly_spend,2),
                          "LoyaltyTier":loyalty})
customer_df = pd.DataFrame(customer_data)




# Operational Data
operational_data=[]
for store in stores:
    row = store_df[store_df["Store"]==store].iloc[0]
    sales_total = sales_df[sales_df["Store"]==store]["Sales"].sum()
    profit_total = sales_df[sales_df["Store"]==store]["Profit"].sum()
    operational_data.append({"Store":store,"AnnualSales":round(sales_total,2),"AnnualProfit":round(profit_total,2),
                             "SalesPerSqFt":round(sales_total/row["SquareFootage"],2),
                             "ProfitPerSqFt":round(profit_total/row["SquareFootage"],2),
                             "SalesPerStaff":round(sales_total/row["StaffCount"],2),
                             "InventoryTurnover":round(np.random.uniform(12,18)*store_perf[store],2),
                             "CustomerSatisfaction":round(min(5,np.random.normal(4.0,0.3)*store_perf[store]**0.5),2)})
operational_df=pd.DataFrame(operational_data)




#Functions 
def analyze_sales_performance():
    return {
        "total_sales": sales_df["Sales"].sum(),
        "total_profit": sales_df["Profit"].sum(),
        "avg_profit_margin": sales_df["ProfitMargin"].mean(),
        "sales_by_store": sales_df.groupby("Store")["Sales"].sum(),
        "sales_by_dept": sales_df.groupby("Department")["Sales"].sum()
    }



def visualize_sales_distribution():
    s_fig, ax1 = plt.subplots(); sales_df.groupby("Store")["Sales"].sum().plot(kind="bar",ax=ax1); ax1.set_title("Sales by Store"); plt.close(s_fig)
    d_fig, ax2 = plt.subplots(); sales_df.groupby("Department")["Sales"].sum().plot(kind="bar",color="orange",ax=ax2); ax2.set_title("Sales by Department"); plt.close(d_fig)
    t_fig, ax3 = plt.subplots(); sales_df.groupby(pd.Grouper(key="Date",freq="ME"))["Sales"].sum().plot(ax=ax3); ax3.set_title("Monthly Sales Trend"); plt.close(t_fig)
    return s_fig,d_fig,t_fig



def analyze_customer_segments():
    return {"segment_counts": customer_df["Segment"].value_counts(),
            "segment_avg_spend": customer_df.groupby("Segment")["MonthlySpend"].mean(),
            "segment_loyalty": customer_df.groupby("Segment")["LoyaltyTier"].value_counts().unstack(fill_value=0)}



def analyze_sales_correlations():
    corr_df = operational_df[["AnnualSales","AnnualProfit","SalesPerSqFt","ProfitPerSqFt","SalesPerStaff","InventoryTurnover","CustomerSatisfaction"]].corr()
    top_corr = corr_df["AnnualSales"].drop("AnnualSales").abs().sort_values(ascending=False)
    top_correlations = list(zip(top_corr.index,top_corr.values))
    fig, ax = plt.subplots(); cax = ax.matshow(corr_df,cmap="coolwarm"); plt.colorbar(cax,ax=ax)
    ax.set_xticks(range(len(corr_df.columns))); ax.set_yticks(range(len(corr_df.columns)))
    ax.set_xticklabels(corr_df.columns,rotation=45); ax.set_yticklabels(corr_df.columns); ax.set_title("Correlation Matrix"); plt.close(fig)
    return {"store_correlations":corr_df,"top_correlations":top_correlations,"correlation_fig":fig}



def compare_store_performance():
    eff = operational_df[["Store","SalesPerSqFt","SalesPerStaff"]]
    rank = operational_df.set_index("Store")["AnnualProfit"].sort_values(ascending=False)
    fig, ax = plt.subplots(); x = np.arange(len(eff))
    ax.bar(x-0.2,eff["SalesPerSqFt"],0.4,label="SalesPerSqFt"); ax.bar(x+0.2,eff["SalesPerStaff"],0.4,label="SalesPerStaff")
    ax.set_xticks(x); ax.set_xticklabels(eff["Store"]); ax.set_title("Store Efficiency Comparison"); ax.legend(); plt.close(fig)
    return {"efficiency_metrics":eff,"performance_ranking":rank,"comparison_fig":fig}



def analyze_seasonal_patterns():
    monthly = sales_df.groupby(pd.Grouper(key="Date",freq="ME"))["Sales"].sum()
    dow = sales_df.groupby(sales_df["Date"].dt.day_name())["Sales"].sum()
    fig, ax = plt.subplots(); monthly.plot(ax=ax); ax.set_title("Seasonal Sales Patterns"); ax.set_ylabel("Sales ($)"); ax.grid(True); plt.close(fig)
    return {"monthly_sales":monthly,"dow_sales":dow,"seasonal_fig":fig}



def predict_store_sales():
    # Linear regression without sklearn
    df = operational_df.copy()
    X = df[['SalesPerSqFt','SalesPerStaff']].values
    y = df['AnnualSales'].values
    X = np.c_[np.ones(X.shape[0]), X]
    beta = np.linalg.pinv(X.T @ X) @ X.T @ y
    y_pred = X @ beta
    ss_res = np.sum((y - y_pred)**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    r2 = max(0.0, 1 - ss_res/ss_tot)
    coefficients = {'Intercept':beta[0],'SalesPerSqFt':beta[1],'SalesPerStaff':beta[2]}
    fig, ax = plt.subplots()
    ax.scatter(y, y_pred)
    ax.plot([y.min(), y.max()], [y.min(), y.max()],'r--'); ax.set_title(f'Predicted vs Actual Sales (R²={r2:.2f})'); plt.close(fig)
    return {"coefficients":coefficients,"r_squared":r2,"predictions":pd.Series(y_pred,index=df['Store']),"model_fig":fig}



def forecast_department_sales():
    dept_trends = sales_df.groupby([pd.Grouper(key='Date', freq='ME'), 'Department'])['Sales'].sum().unstack('Department')
    dept_trends = dept_trends.apply(pd.to_numeric)
    growth_rates = dept_trends.pct_change().mean()
    fig, ax = plt.subplots(figsize=(10,6)); dept_trends.plot(ax=ax); ax.set_title('Departmental Sales Trends'); plt.close(fig)
    return {'dept_trends':dept_trends,'growth_rates':growth_rates,'forecast_fig':fig}



def identify_profit_opportunities():
    merged = sales_df.merge(customer_df,left_on="Store",right_on="PreferredStore")
    combo = merged.groupby(["Store","Department","Segment"],as_index=False)["Profit"].sum()
    return {"top_combinations":combo.sort_values("Profit",ascending=False).head(10),
            "underperforming":combo.sort_values("Profit",ascending=True).head(10),
            "opportunity_score":combo.groupby("Store")["Profit"].sum().sort_values(ascending=False)}



def develop_recommendations():
    return ["Increase marketing in low-performing stores",
            "Focus promotions on high-margin departments",
            "Offer loyalty incentives to lower-spending segments",
            "Adjust staffing based on efficiency metrics",
            "Use seasonal trends for inventory planning"]



def generate_executive_summary():
    print("\n" + "="*60 + "\nGREEN GROCER EXECUTIVE SUMMARY\n" + "="*60)
    print("\nOverview:\nGreen Grocer's analytics provide insights into store performance, customer behavior, and departmental trends.\n")
    print("Key Findings:")
    for item in ["Top performing stores and departments","Distinct customer segment spending patterns","Seasonal trends affect sales","Operational metrics correlate with sales","Forecasting shows likely departmental growth"]:
        print(f"- {item}")
    print("\nRecommendations:")
    for r in develop_recommendations(): print(f"- {r}")
    print("\nExpected Impact:\nImproved profitability, optimized staffing and inventory, enhanced customer loyalty.\n" + "="*60)



#Main Function
def main():
    print("\n--- DESCRIPTIVE ANALYTICS ---")
    perf = analyze_sales_performance(); print("Total Sales:", perf["total_sales"]); print("Total Profit:", perf["total_profit"])
    s_fig,d_fig,t_fig = visualize_sales_distribution()
    seg = analyze_customer_segments(); print(seg["segment_counts"]); print(seg["segment_avg_spend"])
    
    print("\n--- DIAGNOSTIC ANALYTICS ---")
    corr = analyze_sales_correlations()
    comp = compare_store_performance()
    season = analyze_seasonal_patterns()
    
    print("\n--- PREDICTIVE ANALYTICS ---")
    pred = predict_store_sales()
    dept_forecast = forecast_department_sales()
    
    print("\n--- INTEGRATED ANALYSIS ---")
    opp = identify_profit_opportunities(); print("Top Combinations:\n",opp["top_combinations"])
    recs = develop_recommendations(); print("Recommendations:\n",recs)
    
    generate_executive_summary()
    
    plt.show()  # show all figures at once
    
    return {"performance":perf,"segments":seg,"correlations":corr,"store_comp":comp,"season":season,
            "prediction":pred,"forecast":dept_forecast,"opportunities":opp,"recommendations":recs}


#RUN THE ASSIGNMENT
#DONT CRASH
if __name__=="__main__":
    results = main()



