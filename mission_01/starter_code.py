# ============================================================
#  Mission 01 — Smart Budget & Expense Tracker
#  GDG CU Data Science, AI & ML Track
# ============================================================
#
#  YOUR TASK: Fill in the missing logic wherever you see "..."
#  Read every comment carefully — it tells you exactly what to do.
#
#  Key concepts you will practise:
#    - while loops
#    - input() with type conversion to float
#    - augmented assignment (+=)
#    - if / else conditionals
# ============================================================


# --- Step 1: Get the budget from the user ---
# Use input() to ask for the budget, then convert it to a float.

budget = ...   # TODO: replace ... with the correct input() call + float() conversion


# --- Step 2: Initialise a variable to track total spending ---
# This variable will grow as the user logs expenses.

total_spent = ...   # TODO: what value should a running total start at?


# --- Step 3: Start the expense-tracking loop ---
# The loop should keep running until the user types 'quit'.

while ...:   # TODO: what condition keeps this loop going?

    # --- Step 4: Ask for an expense ---
    # Hint: the user might type a number OR the word 'quit'.
    user_input = input("Enter expense amount (or 'quit' to stop): ")

    # --- Step 5: Check if the user wants to quit ---
    if user_input.lower() == "quit":
        ...   # TODO: exit the loop (one keyword does this)

    # --- Step 6: Convert the input to a float and add it to the total ---
    # Hint: use float() and the += operator.
    expense = ...   # TODO: convert user_input to a float
    # TODO: add expense to total_spent using +=  (hint: total_spent += expense)

    # --- Step 7: Print the running total ---
    # Format the output to 2 decimal places using an f-string, e.g. f"${total_spent:.2f}"
    print(...)   # TODO: print a message showing total_spent so far

    # --- Step 8: Warn the user if they are over budget ---
    if ...:   # TODO: what condition means the user has exceeded their budget?
        print(...)   # TODO: print a warning message


# --- Step 9: Print a final summary ---
# This code runs after the loop ends (i.e. after the user types 'quit').
print("\n--- Final Summary ---")
print(...)   # TODO: print the total amount spent
print(...)   # TODO: print the remaining budget (budget - total_spent), which may be negative
