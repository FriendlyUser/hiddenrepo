Below are four illustrative examples—one each for **Code Generation/Completion**, **Code Fixing**, **Test-Case Generation**, and **Output Generation**—that mirror the style and complexity outlined in the provided documentation. Each example includes multiple inputs/outputs or highlights multiple constraints.

---

## 1) Code Generation / Completion

### Prompt

```python
def convert_time_12_to_24(time_str: str) -> str:
    """
    Convert a given time string from 12-hour format (hh:mm:ssAM or hh:mm:ssPM)
    to 24-hour format (HH:mm:ss). 
    
    Constraints / Requirements:
    1. The input string always follows the format "hh:mm:ssXX" where:
       - hh is two digits (01 to 12),
       - mm is two digits (00 to 59),
       - ss is two digits (00 to 59),
       - XX is either "AM" or "PM".
    2. If the time is in AM, 
       - "12:xx:xxAM" should be converted to "00:xx:xx".
       - Otherwise, keep the same hour if it's not "12".
    3. If the time is in PM,
       - "12:xx:xxPM" should remain "12:xx:xx".
       - For other hours (01-11), add 12 to the hour.
    4. Return the resulting 24-hour format as "HH:mm:ss".
    
    Examples:
    >>> convert_time_12_to_24("12:00:00AM")
    '00:00:00'
    >>> convert_time_12_to_24("07:05:45PM")
    '19:05:45'
    >>> convert_time_12_to_24("12:40:22PM")
    '12:40:22'
    >>> convert_time_12_to_24("01:01:01AM")
    '01:01:01'
    >>> convert_time_12_to_24("12:59:59PM")
    '12:59:59'
    """
```

### **Response (Code Completion)**

```python
def convert_time_12_to_24(time_str: str) -> str:
    """
    Convert a given time string from 12-hour format (hh:mm:ssAM or hh:mm:ssPM)
    to 24-hour format (HH:mm:ss).
    
    Constraints / Requirements:
    1. The input string always follows the format "hh:mm:ssXX".
    2. Handle '12' edge cases for both AM and PM.
    3. Return the resulting 24-hour format as "HH:mm:ss".

    Examples:
    >>> convert_time_12_to_24("12:00:00AM")
    '00:00:00'
    >>> convert_time_12_to_24("07:05:45PM")
    '19:05:45'
    >>> convert_time_12_to_24("12:40:22PM")
    '12:40:22'
    >>> convert_time_12_to_24("01:01:01AM")
    '01:01:01'
    >>> convert_time_12_to_24("12:59:59PM")
    '12:59:59'
    """
    # Extract hour, minute, second, and the AM/PM suffix
    hour = int(time_str[:2])
    minute = time_str[3:5]
    second = time_str[6:8]
    meridiem = time_str[8:].upper()  # 'AM' or 'PM'

    # Convert based on the meridiem
    if meridiem == "AM":
        # If hour is 12 (special case), convert to 00
        if hour == 12:
            hour = 0
    else:  # PM
        # If hour is not 12, add 12
        if hour != 12:
            hour += 12

    # Format hour back to two digits
    hour_24 = f"{hour:02d}"
    return f"{hour_24}:{minute}:{second}"


# Explanation / Reasoning:
# 1. Parse the components of the time string: hour, minute, second, AM/PM.
# 2. For AM: If hour is 12, reset to 00. Otherwise keep it as is.
# 3. For PM: If hour is between 1 and 11, add 12 to convert to 24-hour format.
# 4. Construct the final string in HH:mm:ss format.

# Example usage to validate multiple inputs:
print(convert_time_12_to_24("12:00:00AM"))  # Expected '00:00:00'
print(convert_time_12_to_24("07:05:45PM"))  # Expected '19:05:45'
print(convert_time_12_to_24("12:59:59PM"))  # Expected '12:59:59'
```

---

## 2) Code Fixing

### Prompt

**(User’s original buggy code snippet)**

```python
# The user wants to calculate the factorial of a given number n (n >= 0),
# but the code produces incorrect results for certain values of n.

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    factorial(0) = 1
    factorial(n) = n * factorial(n-1)
    
    >>> factorial(0)
    1
    >>> factorial(5)
    120
    >>> factorial(7)
    5040
    >>> factorial(10)
    3628800
    """
    if n == 0:
        return 0  # <-- This is incorrect
    else:
        return n * factorial(n - 1)

```

### **Response (Code Fixing)**

```python
def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    factorial(0) = 1
    factorial(n) = n * factorial(n-1)

    >>> factorial(0)
    1
    >>> factorial(5)
    120
    >>> factorial(7)
    5040
    >>> factorial(10)
    3628800
    """
    # Explanation of the error:
    # The original code returned 0 when n == 0, which yields a final result of 0 for any call involving factorial(0).
    # Factorial(0) should be 1, by definition.
    
    if n == 0:
        return 1  # Corrected this line
    else:
        return n * factorial(n - 1)

# Explanation of Corrections:
# 1. Changed the base case from 'return 0' to 'return 1' for n == 0.
# 2. No other changes were needed; the recursive structure remains the same.

# Testing the corrected code:
print(factorial(0))   # Expected 1
print(factorial(5))   # Expected 120
print(factorial(7))   # Expected 5040
print(factorial(10))  # Expected 3628800
```

---

## 3) Test-Case Generation

### Prompt

```python
# We have a function that merges overlapping time intervals.
# The function is supposed to accept a list of tuples (start, end) in ascending order by start time
# and merge any intervals that overlap. If an interval doesn't overlap with the current one,
# it is simply appended to the result.

def merge_intervals(intervals):
    """
    Merges all overlapping intervals and returns the result as a list of tuples.
    Example:
    >>> merge_intervals([(1,3),(2,6),(8,10),(15,18)])
    [(1,6),(8,10),(15,18)]
    """
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
    return merged

# Prompt: Generate a diverse set of test cases to validate 'merge_intervals' correctness.
```

### **Response (Test-Case Generation)**

```python
# Here is a comprehensive suite of test cases covering various scenarios:

# 1. No intervals (edge case)
test_input_1 = []
# Expected output is an empty list
# Because there are no intervals to merge.

# 2. Single interval
test_input_2 = [(5, 7)]
# Expected output: [(5, 7)]
# Only one interval, nothing to merge.

# 3. Already non-overlapping intervals
test_input_3 = [(1,2), (3,4), (5,6)]
# Expected output: [(1,2), (3,4), (5,6)]
# Each interval is distinct, no merges should occur.

# 4. Fully overlapping intervals
test_input_4 = [(1,5), (2,4), (3,5)]
# Expected output: [(1,5)]
# All intervals overlap into one big interval from 1 to 5.

# 5. Partially overlapping intervals
test_input_5 = [(1,3), (2,6), (8,10), (15,18)]
# Expected output: [(1,6), (8,10), (15,18)]
# The first two intervals merge; others remain as-is.

# 6. Intervals that just touch at endpoints
test_input_6 = [(1,3), (3,5), (5,6)]
# Depending on the definition of "overlapping", these might or might not merge.
# If we assume intervals [1,3] and [3,5] DO overlap at point 3,
# the expected output could be [(1,5), (5,6)] or even [(1,6)] if [3,5] and [5,6] are considered overlapping at 5.
# For the current code, intervals are merged only if the start of the new interval is 
# <= the end of the last one. So actual merges:
# => [(1,5), (5,6)]
# Because 5 == 5 again merges the second and third intervals:
# => final = [(1,6)]

# 7. Large or extended intervals
test_input_7 = [(0, 1), (1, 100), (99, 200)]
# Expected output: [(0, 200)]
# Because (0,1) and (1,100) merge, then that result merges with (99,200).

# 8. Intervals already sorted in ascending order but with duplicates
test_input_8 = [(2, 3), (2, 3), (3, 4)]
# Expected output: [(2, 4)]
# All intervals can merge into one.

# Summaries:
# 1. test_input_1 => []
# 2. test_input_2 => [(5, 7)]
# 3. test_input_3 => [(1,2), (3,4), (5,6)]
# 4. test_input_4 => [(1,5)]
# 5. test_input_5 => [(1,6), (8,10), (15,18)]
# 6. test_input_6 => [(1,6)]
# 7. test_input_7 => [(0, 200)]
# 8. test_input_8 => [(2, 4)]

# Testing example:
print(merge_intervals(test_input_1))  # Expected []
print(merge_intervals(test_input_2))  # Expected [(5, 7)]
print(merge_intervals(test_input_3))  # Expected [(1,2), (3,4), (5,6)]
print(merge_intervals(test_input_4))  # Expected [(1,5)]
print(merge_intervals(test_input_5))  # Expected [(1,6), (8,10), (15,18)]
print(merge_intervals(test_input_6))  # Should result in [(1,6)]
print(merge_intervals(test_input_7))  # Expected [(0,200)]
print(merge_intervals(test_input_8))  # Expected [(2,4)]
```

**Concise Summary of the Code**:  
- The code iterates over a sorted list of `(start, end)` intervals.  
- If the current interval cannot be merged (i.e., its start is after the end of the last merged interval), it’s appended to the result. Otherwise, the last interval in the result is updated (its end is set to the maximum end among the overlapping intervals).

---

## 4) Output Generation

### Prompt

```python
# We have a function that takes two integers and performs several operations:
# 1. Add them
# 2. Subtract the second from the first
# 3. Multiply them
# 4. Check if the division is possible (non-zero divisor). If yes, do integer division; otherwise return None.

def multi_operations(a, b):
    """
    Given two integers a and b, return a tuple of four values:
    (a+b, a-b, a*b, integer_div_result_or_None)

    For example:
    >>> multi_operations(5, 3)
    (8, 2, 15, 1)
    >>> multi_operations(2, 0)
    (2, 2, 0, None)
    >>> multi_operations(-4, 2)
    (-2, -6, -8, -2)
    """
    add_res = a + b
    sub_res = a - b
    mul_res = a * b
    div_res = a // b
    return (add_res, sub_res, mul_res, div_res)

# Prompt: If the input is multiple pairs of integers, what would the function outputs be?
input_values = [(5, 3), (2, 0), (-4, 2), (0, 5), (10, -2)]
```

### **Response (Output Generation)**

Below is the expected output for each pair, with a brief explanation:

1. **Input**: `(5, 3)`
   - **Step-by-step**:
     - a + b = 5 + 3 = 8
     - a - b = 5 - 3 = 2
     - a * b = 5 * 3 = 15
     - a // b = 5 // 3 = 1  (integer division)
   - **Result**: `(8, 2, 15, 1)`

2. **Input**: `(2, 0)`
   - **Step-by-step**:
     - a + b = 2 + 0 = 2
     - a - b = 2 - 0 = 2
     - a * b = 2 * 0 = 0
     - Since b = 0, we return `None` for integer division
   - **Result**: `(2, 2, 0, None)`

3. **Input**: `(-4, 2)`
   - **Step-by-step**:
     - a + b = -4 + 2 = -2
     - a - b = -4 - 2 = -6
     - a * b = -4 * 2 = -8
     - a // b = -4 // 2 = -2
   - **Result**: `(-2, -6, -8, -2)`

4. **Input**: `(0, 5)`
   - **Step-by-step**:
     - a + b = 0 + 5 = 5
     - a - b = 0 - 5 = -5
     - a * b = 0 * 5 = 0
     - a // b = 0 // 5 = 0
   - **Result**: `(5, -5, 0, 0)`

5. **Input**: `(10, -2)`
   - **Step-by-step**:
     - a + b = 10 + (-2) = 8
     - a - b = 10 - (-2) = 12
     - a * b = 10 * -2 = -20
     - a // b = 10 // -2 = -5  (integer division rounds toward negative infinity in Python)
   - **Result**: `(8, 12, -20, -5)`

---

### Why These Examples Are “Similarly Complex”

- **Multiple inputs/outputs**: Each example deals with multiple or varied inputs (e.g., times, intervals, integers) and produces multiple outputs or requires multiple checks.
- **Edge cases**: Each example includes edge conditions (e.g., zero divisor, 12-hour vs. 24-hour midnight/noon, nested intervals, empty lists).
- **Constraint handling**: Prompts explicitly detail constraints or special rules (e.g., merging intervals only when they overlap, time conversion edge cases, factorial base case).
- **Explanation / Reasoning**: All responses include a clear explanation of approach or reasons for correctness.

These samples align with the guidelines for crafting coding prompts with multiple conditions and outputs, ensuring a higher level of complexity and thoroughness.