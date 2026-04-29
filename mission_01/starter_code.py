# ============================================================
#  Mission 01 — Smart Budget & Expense Tracker
#  GDG CU Data Science, AI & ML Track
# ============================================================
#
#  YOUR TASK: Write the code for each step using the hints below.
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
# Example: budget = float(input("Enter your total budget: "))


# --- Step 2: Initialise a variable to track total spending ---
# This variable will grow as the user logs expenses.
# A running total should start at 0.


# --- Step 3: Start the expense-tracking loop ---
# Use a while loop that keeps running until the user types 'quit'.


    # --- Step 4: Ask for an expense ---
    # Hint: the user might type a number OR the word 'quit'.
    # Example: user_input = input("Enter expense amount (or 'quit' to stop): ")


    # --- Step 5: Check if the user wants to quit ---
    # If user_input.lower() equals "quit", exit the loop (one keyword does this).


    # --- Step 6: Convert the input to a float and add it to the total ---
    # Convert user_input to a float, then add it to total_spent using +=.
    # Example: expense = float(user_input)
    # Example: total_spent += expense


    # --- Step 7: Print the running total ---
    # Format the output to 2 decimal places using an f-string.
    # Example: print(f"Total spent so far: ${total_spent:.2f}")


    # --- Step 8: Warn the user if they are over budget ---
    # Check if total_spent is greater than budget.
    # If so, print a warning message.


# --- Step 9: Print a final summary ---
# This code runs after the loop ends (i.e. after the user types 'quit').
# Print the total amount spent and the remaining budget (budget - total_spent).
