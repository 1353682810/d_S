#
# 题目2
# leetcode 283 - 移动零
# 问题描述
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 说明:
#
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
#
#
# 思路
# i 指针用于存放非零元素
# j 指针用于遍历寻找非零元素
# （注：j 指针找到一个非零元素后，nums[i] 的位置 i++，用于下一个 j 指针找到的非零元素）
# j 指针遍历完后，最后 nums 数组还有空位置，存放 0 即可
# [0,1,0,3,12]
def move_zore(nums):
    solm = 0
    fast = 1
    while fast < len(nums):
        if nums[solm] == 0 and nums[fast] == 0:
            fast += 1
        elif nums[solm] == 0 and nums[fast] != 0:
            nums[solm] = nums[fast]
            nums[fast] = 0
            solm += 1
            fast += 1
    return nums

def move_zeor1(nums):
    solm=0
    fast=0
    while fast<len(nums):
        if  nums[fast]==0:
            fast+=1
        else:
            nums[solm],nums[fast]=nums[fast],nums[solm]
            solm+=1
            fast+=1
    return nums


print(move_zeor1([0, 1, 0, 3, 12]))

def move_zeor2(nums):
    solm=0
    fast=0
    while fast<len(nums):
        if  nums[fast]==0:
            fast+=1
        else:
            nums[solm]=nums[fast]
            solm+=1
            fast+=1
    for i in range(solm,len(nums)):
            nums[i]=0
    return nums

print(move_zeor2([0, 1, 0, 3, 12]))