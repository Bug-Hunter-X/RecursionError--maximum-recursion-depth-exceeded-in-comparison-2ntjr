def function_with_uncommon_error_solution(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    total = 0
    for i in range(n + 1):
        total += i
    return total