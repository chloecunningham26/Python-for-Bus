#Chloe Cunningham
#Python Module 4 Assignment

#welcome message for program
print("=" * 60)
print("FASTFUNDS FINANCIAL - BUSINESS LOAN EVALUATION SYSTEM")
print("="*60)

#needed info
#keep all names the same
business_name = "TechSolutions Inc."
years_in_operation = 3.5
annual_revenue = 280000
credit_score = 690
requested_amount = 150000
business_type = "Technology" #options: "Retail", "Service", etc.

#Display application details
print("f\nLOAN APPLICATION DETAILS:")
print(f"Business Name: {business_name}")
print(f"Years in Operation: {years_in_operation:.1f} years")
print(f"Annual Revenue: ${annual_revenue:,.2f}")
print(f"Credit Score: {credit_score}")
print(f"Requested Loan Amount: ${requested_amount:,.2f}")
print(f"Business Type: {business_type}")
print("\nPROCESSING APPLICATION...")

#check if eligable
eligibility_reasons = []
if (years_in_operation >= 2) and (annual_revenue >= 100000):
    meets_basic_requirements = True
else:
    meets_basic_requirements = False
    eligibility_reasons.append(reason)
    

#access credit scores for low, medium, high risk loans
if credit_score >= 720:
    risk_tier = "Low"

elif credit_score >= 650:
    risk_tier = "Medium"

elif credit_score >=600:
    risk_tier = "High"

else:
    risk_tier = "Very High"
    
    
#loan amount 
if risk_tier == "Low":
    max_loan_amount = 500000.0
elif risk_tier == "Medium":
    max_loan_amount = 250000.0
elif risk_tier == "High":
    max_loan_amount = 100000.0
else:
    max_loan_amount = 25000.0
    
    
restricted_industries = ["Gambling", "Drugs", "Weapons"]

if business_type in restricted_industries :
    passes_industry_check = False
    industry_reasons = [f"Business in restricted industry: {business_type}"]
else:
    passes_industry_check = True
    industry_reasons = []
    

#Determine interest rate
if risk_tier == "Low":
        interest_rate = 5.0
elif risk_tier == "Medium":
        interest_rate = 7.5
elif risk_tier == "High":
            interest_rate = 11.0
else:
        interest_rate = 15.0
        
        
        
#combine everything, make final decision
if passes_industry_check:
    decision = "APPROVED"
    approved_amount = max_loan_amount
            
else:
    decision = "DENIED"
    approved_amount = 0.0
            
    
#output final decision
print("=====LOAN DECISION=====")
print(f"Decision: {decision}")
print(f"Risk Assessment: {risk_tier} Risk")
print(f"Loan Details:")
print(f"-Requested Amount: ${requested_amount}")
print(f"-Approved Amount: ${max_loan_amount}")
print(f"-Interest Rate: {interest_rate}%")
print(f"Reasons: Passes Industry Check = {passes_industry_check}")
print(f"Recommendations: INVEST WELL - PAY ME BACK!")
    