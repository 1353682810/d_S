from typing import List
def ThreeSumCloses(nums: List[int],target: int) -> int:
    nums.sort()
    min=abs(nums[0]+nums[1]+nums[2]-target)
    res=nums[0]+nums[1]+nums[2]
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum=nums[i]+nums[left]+nums[right]
            if abs(sum-target)<min:
                min=abs(sum-target)
                res=sum

            elif sum > target:
                right-= 1
            elif sum < target:
                left -= 1
            elif abs(sum-target) == min:
                return sum

            left += 1
            right -= 1

    return res
nums = [-1, 2, 1, -4]
print(ThreeSumCloses(nums,1))