def get_largest_num(list_of_nums):
  list_of_nums.sort()
  last_index = len(list_of_nums) - 1
  return list_of_nums(last_index)


print(get_largest_num([5, 2, 17, 8, 3]))
