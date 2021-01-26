"""
Exercise 3
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?

# Expected: 
# Actual: Error message

# - What error message (if any) is there?

# ### Problem 3 ###
# Traceback (most recent call last):
#   File "exercise-3.py", line 34, in <module>
#     answer = insertion_sort([5, 2, 3, 1, 6])
#   File "exercise-3.py", line 26, in insertion_sort
#     while key < arr[j] : 
# IndexError: list index out of range

# - What line number is causing the error?

# answer = insertion_sort([5, 2, 3, 1, 6])
# while key < arr[j]: 

# - What can you deduce about the cause of the error?

# the while loop is running over the end of the array, or else j == 0 and that is throwing the error

# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.

def insertion_sort(arr):
    """Performs an Insertion Sort on the array arr."""
    for i in range(1, len(arr)):
        key = arr[i] 

        j = i-1
        while key < arr[j] and j >= 0: 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    print('### Problem 3 ###')
    answer = insertion_sort([5, 2, 3, 1, 6])
    print(answer)

