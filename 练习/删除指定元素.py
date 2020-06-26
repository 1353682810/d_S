#[0,1,2,2,3,0,4,2]
def remove_element(nums,element):
    slow=0
    fast=0
    while fast<len(nums):
        if nums[fast]==element:
            fast+=1

        else:
            nums[slow]=nums[fast]
            slow+=1
            fast+=1
    return slow,nums[:slow]
print(remove_element([0,1,2,2,3,0,4,2],2))