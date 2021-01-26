"""
Exercise 2
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?

# Expected:False, True
# Actual: False, False

# - What error message (if any) is there?

# No Error Message

# - What line number is causing the error?

# "for i in range(len(list_of_nums) - 2):""

# - What can you deduce about the cause of the error?

# not counting the last index
# doesn't account for the 3 consecutive numbers not starting with first index

# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!

# this function is assuming that the consecutive list of numbers will begin with the first index

def contains_3_consecutive(list_of_nums):
    """Return True if the list contains 3 consecutive numbers each increasing by 1."""
    for i in range(len(list_of_nums) - 1):
        if (list_of_nums[i+1] == list_of_nums[i] + 1 and
            list_of_nums[i+2] == list_of_nums[i] + 2):
            return True
        elif list_of_nums[i+1] != list_of_nums[i] + 1:
            i += 1
        else:
            return False

    return False

if __name__ == '__main__':
    print('### Problem 2 ###')
    answer1 = contains_3_consecutive([1, 2, 4])
    print("Answer1: ", answer1) # should print False

    answer2 = contains_3_consecutive([4, 1, 2, 3])
    print("Answer2: ", answer2) # should print True