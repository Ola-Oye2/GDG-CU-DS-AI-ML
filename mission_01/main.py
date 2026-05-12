# INTERACTIVE SMART BUDGET AND EXPENSE TRACKER

budget = float(input("Enter your budget -> "))
expense_total = 0

while True:
    expenses = input("Enter an expense amount or quit to stop -> ").lower()

    if expenses == "quit":
        break

    expense_amount = float(expenses)
    
    expense_total += expense_amount
    print(f"Your total expense so far ->{expense_total:.2f}")

    if expense_total > budget:
        print("WARNING!! You have gone over the budget")

remaining_budget = budget - expense_total

print("-------------------SMART BUDGET AND EXPENSE TRACKER---------------------")
print(f"Your total expense -> {expense_total:.2f}")
print(f"Your remaining budget -> {remaining_budget:.2f}")