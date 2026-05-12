# Mission 02 — Data Cleaning & Insight Report

## 🎯 Overview

In this mission you will build a Python script that cleans a small dataset of student scores and prints a short insight report.
The program should remove invalid values, calculate key statistics, and classify each valid score into performance levels.

---

## 📚 Learning Objectives

By completing this mission you will practise:

- **Lists and loops** — iterating through raw values and building cleaned outputs.
- **Input validation** — rejecting invalid score entries safely.
- **Functions** — organizing your script into reusable logic blocks.
- **Basic statistics** — computing count, average, highest, and lowest scores.
- **Conditional logic (`if` / `elif` / `else`)** — assigning performance labels.

---

## 📝 Requirements

Your completed script (`main.py`) **must**:

1. **Define a raw score list**
   Create a list with mixed values (valid scores and invalid entries).

2. **Clean the data**
   Keep only numeric scores between `0` and `100` inclusive.

3. **Build reusable functions**
   Use at least one function for cleaning and one function for reporting.

4. **Compute summary metrics**
   Print:
   - Number of valid scores
   - Average score (2 decimal places)
   - Highest score
   - Lowest score

5. **Classify performance**
   For each valid score, print its label using this rule:
   - `90–100` → `Excellent`
   - `75–89` → `Good`
   - `50–74` → `Pass`
   - `0–49` → `Needs Improvement`

6. **Print a final report section**
   Output should be clear and grouped with headings.

---

## 💡 Example Output

```
--- Cleaned Scores ---
[95, 70, 45, 88, 100, 63]

--- Summary ---
Valid count: 6
Average: 76.83
Highest: 100
Lowest: 45

--- Performance Labels ---
95 -> Excellent
70 -> Pass
45 -> Needs Improvement
88 -> Good
100 -> Excellent
63 -> Pass
```

---

## 🗂️ Files

| File | Description |
|------|-------------|
| `README.md` | This file — mission brief and requirements |
| `main.py` | **Create this file** — write your solution here |

---

## ✅ Submission Checklist

- [ ] My script runs without errors.
- [ ] It removes invalid score values correctly.
- [ ] It prints accurate summary statistics.
- [ ] It labels each valid score with the correct performance level.
- [ ] I used functions to organize the solution.
- [ ] I have pushed my code (`main.py`) to a branch named `mission-02-submission` and opened a Pull Request.

Good luck! 🚀
