# RecursionError: maximum recursion depth exceeded

This repository demonstrates an example of the `RecursionError: maximum recursion depth exceeded` error in Python and provides a solution.

The `bug.py` file contains a recursive function that demonstrates the error. The `bugSolution.py` file shows how to resolve the error using an iterative approach.

## Bug
The bug occurs when the recursive function calls itself repeatedly without a proper base case or optimization.  When the recursion depth exceeds Python's limit, the `RecursionError` is raised. 

## Solution
The solution uses an iterative approach to avoid exceeding the recursion depth.  This is a more efficient way to calculate the result in this particular case.

## How to reproduce the bug
1. Clone this repository.
2. Navigate to the repository's directory.
3. Run `python bug.py` to trigger the error.

## How to run the solution
1. Run `python bugSolution.py` to see the correct result.