# py-session-1-2-tasks

Practice Exercises :

================================================================================

Exercise 1: Advanced Type Conversion & Validation
Topics Covered: Python Basics & Data Types, Exception Handling

Write a function `safe_convert(value, target_type)` that:
- Accepts a value and a target type (`int`, `float`, `str`, `bool`)
- Safely converts the value to the target type
- Returns a tuple `(success: bool, result: any, error_message: str)`
- Handles all edge cases (invalid conversions, None values, etc.)

Test Cases:
```python
assert safe_convert("123", int) == (True, 123, "")
assert safe_convert("12.5", float) == (True, 12.5, "")
assert safe_convert("abc", int)[0] == False
assert safe_convert(None, str) == (True, "None", "")
```

================================================================================

Exercise 2: Nested Dictionary Operations
Topics Covered: Data Structures (Dict), List/Dict Comprehensions

Given a nested dictionary representing a company hierarchy:
```python
company = {
    "Engineering": {
        "Backend": ["Alice", "Bob", "Charlie"],
        "Frontend": ["David", "Eve"],
        "DevOps": ["Frank"]
    },
    "Sales": {
        "North": ["Grace", "Henry"],
        "South": ["Ivy"]
    }
}
```

Write functions to:
1. Flatten the structure to get all employees in a single list
2. Count total employees per department (top-level only)
3. Find which team a specific employee belongs to
4. Use dict comprehension to create a reverse mapping: `{employee: [department, team]}`

================================================================================

Exercise 3: Advanced List Comprehension with Filters
Topics Covered: List Comprehensions, Control Flow

Create a single list comprehension that:
- Takes a list of integers from 1 to 100
- Filters numbers divisible by 3 or 5 (but not both)
- Squares the remaining numbers
- Only includes results less than 1000

Bonus: Convert this to a generator expression and explain the memory difference.

================================================================================

Exercise 4: Function Argument Mastery
Topics Covered: Functions, *args, **kwargs

Write a decorator-like function `merge_calls(*funcs, **defaults)` that:
- Accepts multiple functions and default keyword arguments
- Returns a new function that calls all funcs in sequence
- Passes results from one function to the next using *args/**kwargs
- Overrides with any defaults provided

Example:
```python
def add(x, y): return x + y
def multiply(x, factor=2): return x * factor
combined = merge_calls(add, multiply, factor=3)
result = combined(5, 10)  # Should be (5+10)*3 = 45
```

================================================================================

Exercise 5: OOP - Banking System
Topics Covered: OOP Classes & Objects, Exception Handling, Decorators

Design a banking system with:
- `Account` base class with properties: account_number, balance, owner
- `SavingsAccount` (interest rate, minimum balance)
- `CheckingAccount` (overdraft limit)
- Methods: deposit, withdraw, transfer
- Custom exceptions: `InsufficientFundsError`, `InvalidTransactionError`
- Decorator to log all transactions to a file
- Class method to track total money in all accounts

================================================================================

Exercise 6: Static, Class, and Instance Methods
Topics Covered: Static & Class Methods, OOP

Create a `DateUtils` class with:
- Instance method: `days_until(target_date)` - days from instance date to target
- Class method: `from_string(date_string, format)` - create instance from string
- Static method: `is_valid_date(year, month, day)` - validate date components
- Static method: `is_leap_year(year)`

Demonstrate when to use each method type.

================================================================================

Exercise 7: Abstract Base Classes - Payment System
Topics Covered: Abstract Classes & Methods, OOP

Create an abstract `PaymentProcessor` class with:
- Abstract methods: `validate()`, `process_payment(amount)`, `refund(transaction_id)`
- Concrete method: `log_transaction(details)`
- Implement subclasses: `CreditCardProcessor`, `PayPalProcessor`, `CryptoProcessor`
- Each should have unique validation logic

Demonstrate polymorphism by processing different payment types in a loop.

================================================================================

Exercise 8: Dataclasses with Validation         
Topics Covered: Dataclasses, Exception Handling

Create a `@dataclass` for `Employee` with:
- Fields: id, name, email, salary, department, hire_date
- Post-init validation (email format, salary > 0, valid department)
- Custom `__str__` for pretty printing
- Frozen dataclass option for immutable records
- Ordering based on salary
- Factory method to create from dictionary

================================================================================

Exercise 9: Custom Decorators Chain
Topics Covered: Decorators

Implement these decorators:
1. `@timer` - measures execution time
2. `@retry(attempts=3, delay=1)` - retries on exception
3. `@cache` - memoizes results (simple LRU)
4. `@validate_types(**type_hints)` - validates argument types

Apply all four to a function that fetches data from a slow API (simulate with sleep).

================================================================================

Exercise 10: Map, Filter, Reduce - Data Pipeline
Topics Covered: Decorators, Map-Reduce

Given a list of transaction dictionaries:
```python
transactions = [
    {"id": 1, "amount": 100, "type": "debit", "category": "food"},
    {"id": 2, "amount": 200, "type": "credit", "category": "salary"},
    # ... more
]
```

Use map/filter/reduce to:
1. Filter only debit transactions
2. Map to extract amounts
3. Reduce to calculate total debits
4. Bonus: Group by category and sum using `itertools.groupby`

================================================================================

Exercise 11: Custom Iterator - Fibonacci
Topics Covered: Iterators, Generators

Implement:
1. A `Fibonacci` class as an iterator (with `__iter__` and `__next__`)
2. A generator function `fibonacci_gen(limit)`
3. Compare memory usage and performance for generating first 1 million numbers

Add features:
- Start from custom indices
- Lazy evaluation
- Infinite sequence with `itertools.islice`

================================================================================

Exercise 12: Generator Pipeline - Log Processing
Topics Covered: Generators, File Reading & Writing

Create generator pipeline to process large log files:
1. `read_logs(filename)` - yields lines
2. `parse_logs(lines)` - yields parsed dicts
3. `filter_errors(logs)` - yields only ERROR level
4. `extract_timestamps(logs)` - yields timestamps

Chain them together to process 1GB log file without loading into memory.

================================================================================

Exercise 13: Collections Module - Counter & defaultdict
Topics Covered: Collections

Given a text file:
1. Use `Counter` to find top 10 most common words
2. Use `defaultdict(list)` to group words by their first letter
3. Use `deque` to implement a rotating buffer (max size 100)
4. Use `namedtuple` to create structured log entries

================================================================================

Exercise 14: Stack & Queue - Expression Evaluator
Topics Covered: Stacks & Queues, Data Structures & Algorithms

Implement:
1. Balanced parentheses checker using stack
2. Infix to postfix converter
3. Postfix expression evaluator
4. Queue-based level-order traversal of a binary tree

Test: `"3 4 + 2 * 7 /"` should evaluate to `2.0`

================================================================================
                
Exercise 15: Advanced File Operations
Topics Covered: File Reading & Writing, Exception Handling, Context Managers

Create a `FileManager` context manager that:
- Opens multiple files (read/write) at once
- Handles errors gracefully (file not found, permission errors)
- Automatically closes all files on exit
- Provides methods: `read_line()`, `write_line()`, `copy_content(src, dest)`
- Implements binary file operations (pickle, JSON, CSV)

================================================================================

Exercise 16: Exception Handling - Retry Logic
Topics Covered: Exception Handling, Decorators

Create a robust retry mechanism:
1. Custom exceptions: `RetryableError`, `FatalError`
2. Decorator `@retry_on_exception(max_attempts, backoff_strategy)`
3. Backoff strategies: linear, exponential, random jitter
4. Log all attempts with timestamps
5. Re-raise last exception if all attempts fail

================================================================================

