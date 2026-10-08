# Jonas von Ruden-Doll
# 09/30/2026
# homework 2

# INPUTS
loan_amount = float(input("Enter the loan amount ($): "))
annual_rate = float(input("Enter the annual interest rate (%): "))
loan_years = int(input("Enter the loan term (years): "))

# PROCESSING
# Convert annual percentage rate to monthly decimal rate
monthly_rate = (annual_rate / 100) / 12

# Calculate total number of monthly payments
num_payments = loan_years * 12

# Calculate monthly payment using formula
monthly_pmt = (
    loan_amount
    * (monthly_rate * (1 + monthly_rate) ** num_payments)
    / ((1 + monthly_rate) ** num_payments - 1)
)

# OUTPUT
print()
print(f"Monthly Payment: ${monthly_pmt:.2f}")
print()

# Table Header
print(
    f"{'Month':>5} {'Payment':>10} {'Principal':>12} {'Interest':>10} {'Balance':>12}"
)

# Loop to calculate and print monthly amortization schedule
balance = loan_amount

for month in range(1, num_payments + 1):
    interest = balance * monthly_rate
    principal_paid = monthly_pmt - interest
    balance = balance - principal_paid

    # Handle minor rounding float remainder on final month
    if balance < 0:
        balance = 0.0

    print(
        f"{month:5} {monthly_pmt:10,.2f} {principal_paid:12,.2f} {interest:10,.2f} {balance:12,.2f}"
    )
