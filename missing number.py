def missing_number(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2
    current_sum = sum(nums)
    return total_sum - current_sum
print(missing_number([3, 0, 1]))  
print(missing_number([0, 1]))     
print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))  
