monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = (monthly_income - monthly_expenses)
# anual_intereset_rate = 0.05
projected_savings = (monthly_savings * 12 + (monthly_savings * 12 * 0.05))
r_projected_savings = int(projected_savings)
print(f'Your monthly savings are ${monthly_savings}.')
print(f'Projected savings after one year, with interest, is: ${r_projected_savings}.')
