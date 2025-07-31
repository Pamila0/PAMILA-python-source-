income = float(input("Monthly income (THB): "))
rent = float(input("Housing / Rent cost (THB): "))
food = int(input("Food budget (THB): "))
transport = float(input("Transportation cost (THB): "))
entertainment = int(input("Entertainment budget (THB): "))
emergency_percent = float(input("Emergency fund percent (%): "))
invest_percent = float(input("Investment percent (%): "))

fixed_exp = rent + transport
variable_exp = food + entertainment
total_exp = fixed_exp + variable_exp
remaining = income - total_exp

emergency_saving = income * (emergency_percent / 100)
investment_saving = income * (invest_percent / 100)
free_saving = remaining - emergency_saving - investment_saving

expense_ratio = (total_exp / income) * 100

print("\n=== MONTHLY BUDGET REPORT ===")
print(f"Income: {income:.2f} THB")
print(f"Fixed Expenses: {fixed_exp:.2f} THB")
print(f"Variable Expenses: {variable_exp:.2f} THB")
print(f"Total Expenses: {total_exp:.2f} THB")
print(f"Remaining: {remaining:.2f} THB")

print("\n=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund ({emergency_percent}%): {emergency_saving:.2f} THB")
print(f"Investment ({invest_percent}%): {investment_saving:.2f} THB")
print(f"Available for Savings: {free_saving:.2f} THB")

print("\n=== ANALYSIS ===")
print(f"Expense Ratio: {expense_ratio:.2f}%")