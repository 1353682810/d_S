#[1,1,2,2,3,4]
from typing import List
class Solution:
    def remove_chong(self,nums: List):
        slow=0
        fast=1
        while fast<len(nums):
            if nums[fast]==nums[slow]:
                fast +=1
            else:
                slow+=1
                nums[slow]=nums[fast]
                fast+=1
        return slow+1,nums[:slow+1]
nums=Solution()
print(nums.remove_chong([1,1,2,2,3,4]))

def remove_chongfu(nums):
    n=len(set(nums))
    i=0
    while i<n-1:
        if nums[i]==nums[i+1]:
            temp=nums[i+1]
            nums[i+1:n-1]=nums[i+2:]
            nums[-1]=temp
            continue
        else:
            i+=1
    return i+1,nums[:i+1]
print(remove_chongfu([1,1,2,2,3,4]))