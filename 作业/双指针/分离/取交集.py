# 分离指针专题
# 分离指针是指两个指针分别在两个容器中移动；
# 根据问题的不同，初始位置可能都在头部，或者都在尾部，或一头一尾
#
# 349 - 两个数组的交集
# 题目描述
# 给定两个数组，编写一个函数来计算它们的交集。
#
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2]
#
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [9,4]
#
# 说明:
# 输出结果中的每个元素一定是唯一的。
# 我们可以不考虑输出结果的顺序。
#
def intersection(nums1,nums2):
    nums1.sort()
    nums2.sort()
    i,j=0,0
    nums_set=set()
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<nums2[j]:
            i+=1
        elif nums1[i]>nums2[j]:
            j+=1
        else:
            nums_set.add(nums1[i])
            i+=1
            j+=1
    return list(nums_set)
nums1=[3,6,9,4,5,8]
nums2=[9,0,1,3]
print(intersection(nums1,nums2))