# AI Code Review Assignment (Python)

## Candidate
- Name: Oğuz Nurlu
- Approximate time spent: 30 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- If passed argument "orders" is not a list, it would throw an error while iterating over it.
- If passed argument has numbers or any other objects, it would throw an error.
- While taking the average, it also counts the cancelled orders. It makes the computation wrong.
- If there are no non-cancelled orders, it would throw an error because of division by 0.
- If the order doesn't have the fields "status" or "error", it would throw an error becuase the code can't access these fields.

### Edge cases & risks
- The code can crash if the passed argument "orders" is not a list.
- The code can crash if the passed argument "orders" has incompatible types in the list.
- The code can crash if broken or incomplete orders (that don't have the required fields) are passed in the "orders" list.
- The code can crash if the list is empty or has no non-cancelled orders.

### Code quality / design issues
- The function assumes the passed argument "orders" is always perfect and doesn't handle any edge cases or invalid inputs, which is not a good practice.
- The function also doesn't calculate the average correctly.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Checked if "orders" variable is a list at the start, and returned 0 if it isn't.
- Started the "count" variable from 0, and counted the non-cancelled orders in the loop to correctly get the "count".
- If "count" variable is still 0 at the end, returning 0 to avoid throwing an error.
- Checked if orders are not broken or incomplete (don't have the required fields) and only proceeding if there are no problems with that.


### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- I would test it by giving lists that don't have any orders, that do have orders but incomplete, that has other types other than the expected "order" types (like integers) and passing it non-list variables.


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- It doesn't correctly exclude cancelled orders from the calculation, because it counts all orders instead of just non-cancelled ones.

### Rewritten explanation
- This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of non-cancelled orders. It correctly excludes cancelled orders from the calculation and safely handles edge cases like empty lists or invalid input types.

## 4) Final Judgment
- Decision: Reject
- Justification: The original code contains several critical bugs that can lead to crashes or incorrect calculations. The proposed fixes address these issues and improve the robustness of the function.
- Confidence & unknowns: I am confident that the proposed fixes will resolve all the severe issues in the original code. The bugs can be easily solved by following best practices. The only unknown can be deciding on what the code should do when it encounters invalid input.
---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- If passed argument "emails" has non-string objects (like None or int), it would throw an error.
- The validation logic is too simple; it counts any string with "@" as valid (e.g. "@" or "a@b").

### Edge cases & risks
- The code can crash if the passed argument "emails" has incompatible types.
- The code accepts invalid email formats as valid.

### Code quality / design issues
- The function uses a naive check for email validation which is not sufficient for real-world scenarios.
- The function assumes all items in the list are strings.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Imported "re" module and used a regex pattern for robust validation.
- Wrapped the validation in a try-except block to ignore non-string inputs without crashing.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- I would test it by giving lists with valid emails, invalid formats (missing domain, missing user), and non-string types.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- It doesn't safely ignore invalid entries if they are not strings; it crashes.
- It counts invalid email formats as valid.

### Rewritten explanation
- This function counts the number of valid email addresses using a regex pattern. It safely ignores invalid formats and non-string inputs.

## 4) Final Judgment
- Decision: Reject
- Justification: The original code fails to validate emails correctly and crashes on invalid types. The proposed fixes introduce proper regex validation and type safety.
- Confidence & unknowns: I am confident that the regex and try-except block solve the issues.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- If passed argument "values" is not a list, it would throw an error.
- It divides the total sum by the length of the list (including None values) instead of the count of valid numbers, making the average wrong.
- If the list is empty, it throws a division by zero error.
- If a value is not a number (e.g., "abc"), "float()" conversion throws an error.

### Edge cases & risks
- The code crashes on empty lists.
- The code crashes on non-numeric strings.
- The code calculates incorrect averages when "None" values are present.

### Code quality / design issues
- The function fails to separate the count of valid items from the total length.
- It assumes all non-None values are convertible to floats.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Checked if "values" is a list at the start, and returned 0 if it isn't.
- Tracked "count" manually only for valid numbers.
- Used try-except to handle values that cannot be converted to floats.
- Handled the division by zero case for empty lists or no valid numbers.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- I would test it with lists containing mixed types, None values, empty lists, and non-list inputs.


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- It claims to ensure an accurate average, but logic is flawed because it divides by the total length.
- It claims to handle mixed input types safely, but crashes on strings that aren't numbers.

### Rewritten explanation
- This function calculates the average of valid numeric measurements. It ignores missing values and non-numeric inputs, and safely handles empty lists.

## 4) Final Judgment
- Decision: Reject
- Justification: The original code has logic errors in calculation and lacks robustness against invalid types and empty lists. The fix ensures mathematical accuracy and type safety.
- Confidence & unknowns: I am confident the logic is now correct and robust.
