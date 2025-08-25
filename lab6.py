

def safe_divide(a: float, b: float) -> float:

# Divides a by b, handling division by zero.
# Returns 'inf' if b == 0.

    try:
        return a / b
    except ZeroDivisionError:
        return float('inf')