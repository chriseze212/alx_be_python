def safe_divide(numerator, denominator):
    """Perform division with robust error handling."""
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        return f"Result: {result}"
    except ValueError:
        return "Error: Cannot divide by zero."
    except ZeroDivisionError:
        return "Error: Please enter numeric values only."
