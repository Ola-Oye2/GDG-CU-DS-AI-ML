# Mission 01 — Smart Budget Tracker

## 🎯 Overview

In this mission you will build an interactive **Smart Budget & Expense Tracker** in pure Python.  
The program asks the user for a budget, then lets them log expenses one by one until they type `quit`.  
After each entry it reports the running total and warns the user when they have gone over budget.

---

## 📚 Learning Objectives

By completing this mission you will practise:

- **`while` loops** — keeping a program running until a stop condition is met.
- **`input()` with type conversion** — reading user input and converting it to `float` for arithmetic.
- **Augmented assignment (`+=`)** — accumulating a running total with the `+=` operator.
- **Conditional logic (`if` / `else`)** — comparing values and printing context-aware messages.

---

## 📝 Requirements

Your completed script (`main.py`) **must**:

1. **Prompt for a budget**  
   Ask the user to enter their total budget and store it as a `float`.

2. **Enter an expense loop**  
   Use a `while` loop that continues until the user types `quit`. The starter code already handles case-insensitive matching via `.lower()`.

3. **Accept expense amounts**  
   Inside the loop, prompt the user to enter an expense amount (or `quit` to stop).  
   Convert the input to a `float` and add it to a running total using `+=`.

4. **Print the running total after every entry**  
   After each expense is logged, print the total amount spent so far.

5. **Warn when over budget**  
   After updating the total, check whether `total_spent > budget`.  
   If so, print a clear warning message telling the user they are over budget.

6. **Print a final summary on exit**  
   When the user types `quit`, display the final total spent and the remaining budget  
   (which may be negative if they overspent).

---

## 💡 Example Interaction

```
Enter your total budget: 100
Enter expense amount (or 'quit' to stop): 40
Total spent so far: $40.00
Enter expense amount (or 'quit' to stop): 35
Total spent so far: $75.00
Enter expense amount (or 'quit' to stop): 30
Total spent so far: $105.00
⚠️  Warning: You are over budget!
Enter expense amount (or 'quit' to stop): quit

--- Final Summary ---
Total spent:      $105.00
Budget remaining: $-5.00
```

---

## 🗂️ Files

| File | Description |
|------|-------------|
| `README.md` | This file — mission brief and requirements |
| `starter_code.py` | Points you to create your own `main.py` |
| `main.py` | **Create this file** — write your solution here |

---

## ✅ Submission Checklist

- [ ] My script runs without errors.
- [ ] It correctly accumulates the running total with `+=`.
- [ ] It prints the total after every entry.
- [ ] It warns the user when they exceed their budget.
- [ ] It prints a final summary when the user types `quit`.
- [ ] I have pushed my code (`main.py`) to a branch named `mission-01-submission` and opened a Pull Request.

Good luck! 🚀
