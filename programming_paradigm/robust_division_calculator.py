def safe_divide(numerator, denominator):
    """Perform division with robust error handling."""
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        return f"Result: {result}"
    except ValueError:
        return "Error: Both numerator and denominator must be numbers."
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
