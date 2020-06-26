# 从有序数组中去除重复元素
# eg:输入[1,1,2]  去重后[1,2],输出2
# eg:输入[0,0,1,1,1,2,2,3,3,4],去重后[0,1,2,3,4],输出5
from typing import  List
eg = [1, 1, 2]
e = {}
n = 0
for i in eg:
    e[i] = eg.count(i)
e1 = list(e.keys())
for i in range(len(e1)):
    n += 1
print(e1, n)
print("------------------" * 2)

eg = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
e = {}
n = 0
for i in eg:
    e[i] = eg.count(i)
e1 = list(e.keys())
for i in range(len(e1)):
    n += 1
print(e1, n)


class Solution:
    def removeDuplicated(self,nums: List[int])->int:
        n=len(set(nums))
        i=0
        while i<n-1:
            if nums[i]==nums[i+1]:
                temp=nums[i+1]
                nums[i+1:len(nums)-1]=nums[i+2:]
                nums[-1]=temp
                continue
            else:
                i+=1
        return i+1,nums[:n]
nums=Solution()
print(nums.removeDuplicated([1,1,2,2,3,4]))

class Solution:
    def removeDuplicated(self,nums: List[int])->int:
        slow=0
        fast=1
        while fast<len(nums):
            if nums[fast]==nums[slow]:
                    fast +=1
            else:
                slow +=1
                nums[slow]=nums[fast]
                fast +=1
        return slow+1,nums[:slow+1]
nums=Solution()
print(nums.removeDuplicated([1,1,2,2,3,4]))


