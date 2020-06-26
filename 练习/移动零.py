def move_zero(nums):
    slow=0
    fast=0
    while fast<len(nums):
        if nums[fast]==0:
            fast+=1
        else:
            nums[slow]=nums[fast]
            fast+=1
            slow+=1
    for i in range(slow,len(nums)):
            nums[i]=0
    return nums
print(move_zero([0,3,0,4,5,0,0,7,0]))

def move_zero1(nums):
    slow=0
    fast=0
    while fast<len(nums):
        if nums[fast]==0:
            fast+=1
        else:
            nums[slow],nums[fast]=nums[fast],nums[slow]
            fast+=1
            slow+=1
    return nums
print(move_zero1([0,3,0,4,5,0,0,7,0]))