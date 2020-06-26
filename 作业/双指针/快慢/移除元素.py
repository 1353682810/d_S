# 题目1
# leetcode 27 移除元素
# 给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O (1) 额外空间的条件下完成。
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
# 示例 1:
#
# 给定 nums = [3,2,2,3], val = 3, 函数应该返回新的长度 2,
# 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。
#
# 示例 2:
#
# 给定 nums = [0,1,2,2,3,0,4,2], val = 2, 函数应该返回新的长度 5,
# 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。注意这五个元素可为任意顺序。
# 你不需要考虑数组中超出新长度后面的元素。
#[0,1,2,2,3,0,4,2]
def remove_element(nums,element):
    solm=0
    fast=1
    shu=0
    if len(nums)==1:
        return shu
    elif len(nums)>1:
        while fast<len(nums):
                if nums[solm]!=element :
                       solm+=1
                       fast+=1
                elif nums[solm]==element and nums[fast]==element:
                        fast+=1
                elif nums[solm]==element and nums[fast]!=element:
                        nums[solm]=nums[fast]
                        nums[fast]=element
                        solm+=1
                        shu+=1
        return nums[:len(nums)-shu],shu
    #自己写的有BUG,特殊情况没法处理
print(remove_element([0,1,2,2,3,0,4,2],2))
print("--------"*5)
print(remove_element([3,2,2,3],3))


def RemoveElement(nums,val):
    solm=0
    fast=0
    while fast<len(nums):
        if nums[fast]==val:
            fast+=1
        else :
            nums[solm]=nums[fast]
            fast +=1
            solm +=1
    return solm

print(RemoveElement([0,1,2,2,3,0,4,2],2))

