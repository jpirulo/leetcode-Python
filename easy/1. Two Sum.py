def twoSum(self, nums: List[int], target: int) -> List[int]:
    sum=0
    for i in range(len(nums)):
        list=[]
        list.append(i)
        for j in range((i+1),len(nums)):
            sum = nums[i] + nums[j]
            if sum==target:
                list.append(j)
                return list