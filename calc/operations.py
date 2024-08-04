"""Basic math operations."""

# calc/operations.py

def add(a, b):
    """Add a and b."""
    return a + b

def sub(a, b):
    """Subtract b from a."""
    return a - b

def mult(a, b):
    """Multiply a and b."""
    return a * b

def div(a, b):
    """Divide a by b."""
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
