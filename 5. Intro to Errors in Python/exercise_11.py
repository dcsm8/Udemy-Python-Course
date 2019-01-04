"""
for the function below, add your code in appropriate place that checks the input n.
n should be a non-negative integer, otherwise a ValueError should be raised
and a proper error message should be provided informing the user of the error
for simplicity, you may assume that the input is always an integer for this exercise
"""


def count_from_zero_to_n(n):
    if n < 0:
        raise ValueError('The number should be a non-negative number')

    for x in range(0, n+1):
        print(x)


count_from_zero_to_n(3)
count_from_zero_to_n(0)
count_from_zero_to_n(-1)
