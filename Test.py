# Machine Problem: Loan Calculator
print("Machine Problem: Loan Calculator")
 # Inputs
principal = float(input("Enter Principal Amount (amount borrowed): "))
interest_rate = float(input("Enter Interest Rate (%): "))
loan_duration = int(input("Enter Loan Duration in months: "))
 # Initialize variables
remaining_balance = principal
monthly_principal = principal / loan_duration
total_interest = 0
print("\nMonthly Payment Schedule:")
print(f"{'Month':<6} {'Principal':<12} {'Rate (%)':<10} {'Interest':<10} {'Due':<10} {'Remaining':<12}")
print("-" * 60)
 # Calculate and display monthly details
for month in range(1, loan_duration + 1):
     # Monthly interest calculation (as per formula: (remaining_balance + monthly_principal) * (rate/100))
     monthly_interest = (remaining_balance + monthly_principal) * (interest_rate / 100)
     monthly_due = monthly_principal + monthly_interest
     
     # Update totals and remaining balance
     total_interest += monthly_interest
     remaining_balance -= monthly_principal  # Principal is fixed, so subtract monthly principal
     
     # Display monthly data (formatted for readability)
     print(f"{month:<6} {monthly_principal:<12.2f} {interest_rate:<10.2f} {monthly_interest:<10.2f} {monthly_due:<10.2f} {remaining_balance:<12.2f}")
 # Final summary
print("\nLoan Summary:")
print(f"Total Interest Paid: PHP {total_interest:.2f}")
print(f"Total Amount to Pay: PHP {principal + total_interest:.2f}") 