def function_with_uncommon_error(n):
    if n == 0:
        return 0  # This handles the base case correctly
    elif n < 0:
        raise ValueError("Input must be a non-negative integer")  # This explicitly handles negative input
    else:
        return n + function_with_uncommon_error(n - 1) # This is where the problem is.