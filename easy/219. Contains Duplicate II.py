def containsNearbyDuplicate(nums, k):
    j = {}
    for i, num in enumerate(nums):
        if num in j and i - j[num] <= k:
            return True
        j[num] = i
    return False

nums = [1,2,3,1,2,3]
k = 3
print(containsNearbyDuplicate(nums,k))