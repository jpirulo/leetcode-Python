from collections import defaultdict
def majorityElement(nums) -> int:
    num_count = defaultdict(int)
    num_count = {num:nums.count(num) for num in set(nums)}

    return max(num_count, key=lambda x: num_count[x])
    


if __name__ == "__main__":
   print(majorityElement([2,2,1,1,1,2,2]))
   