"""
Exercise 1
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?

# Expected: The largest difference in a list [5, 3, 1, 2, 6, 4]
# Actual: Error Message

# - What error message (if any) is there?
# 
# ### Problem 1 ###
# Traceback (most recent call last):
#   File "exercise-1.py", line 31, in <module>
#     answer = find_largest_diff([5, 3, 1, 2, 6, 4])
#   File "exercise-1.py", line 23, in find_largest_diff
#     diff = abs(list_of_nums[i] - list_of_nums[i+1])
# IndexError: list index out of range

# - What line number is causing the error?

# line 23, but it keeps changing as I write more notes.
# ""

# - What can you deduce about the cause of the error?

# There is an index ouf range in line "for i in range(len(list_of_nums)):"
# updated line to "for i in range(len(list_of_nums)-1):"


# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!

def find_largest_diff(list_of_nums):
    """Find the largest difference between *consecutive* numbers in a list."""
    largest_diff = 0
    for i in range(len(list_of_nums)-1):
        diff = abs(list_of_nums[i] - list_of_nums[i+1])
        if diff > largest_diff:
            largest_diff = diff

    return largest_diff

if __name__ == '__main__':
    print('### Problem 1 ###')
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])

    # This should print 4, as the largest diff between consecutive numbers is between 2 and 6
    print(answer)