def containsDuplicate(nums) -> bool: 
    n_set = set()
    for num in nums:
        if num in n_set:
            return True
        n_set.add(num)
        print(n_set)


    return False

nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(containsDuplicate(nums))