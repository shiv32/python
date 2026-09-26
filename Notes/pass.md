What is pass in python?

## `pass` in Python

In Python, `pass` is a null statement. 
It does nothing when executed. 
It is used as a placeholder when Python requires a statement, 
but you don't want to write any code there yet.

### 1. Example: Empty function

Python

Run

```
def my_function():
    pass

my_function()
```

Output: No output.

Without `pass`, an empty function causes an `IndentationError` or syntax error because Python expects a statement in the function body.

### 2. Example: Empty class

Python

Run

```
class MyClass:
    pass
```

This creates an empty class without any methods or attributes.

### 3. Example: `pass` in an `if` statement

Python

Run

```
x = 10

if x > 5:
    pass
else:
    print("x is small")
```

Output: No output.

The `if` condition is true, so Python executes `pass` and does nothing.

### 4. Example: Placeholder for future code

Python

Run

```
def calculate():
    # TODO: Add calculation logic later
    pass
```

You can fill in the function's implementation later.

In short: `pass` means "do nothing here for now."
