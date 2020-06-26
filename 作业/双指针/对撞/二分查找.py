def binarysearch(nums,val):
    left=0
    right=len(nums)-1
    while left<=right:
        if val not in nums:
            return -1
        if nums[left]==val:
            return left
        elif nums[right]==val:
            return  right
        else:
            mid=int(left+right/2)
            if val<nums[mid]:
                right =mid
            elif val>nums[mid]:
                left=mid
            else:
                return mid
print(binarysearch([1,5,17,36,85,89,93,97,100],85))

def binarysearch(nums,val):
    left = -1
    right = len(nums)
    if val not in nums:
        return -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < val:
            left = mid
        elif nums[mid] > val:
            right = mid
        else:
            return mid

print(binarysearch([1,5,17,36,85,89,93,97,100],85))

def tiguierfenchazhao(nums,val,left,right):
    if right>0:
        mid=left+(right-left)//2
        while left<=right:
            if val==nums[mid]:
                return  mid
            elif val>nums[mid]:
                return tiguierfenchazhao(nums,val,mid+1,right)
            else:
                return tiguierfenchazhao(nums,val,left,mid-1)
    else:
        return -1
nums=[1,5,17,36,85,89,93,97,100]
print(tiguierfenchazhao(nums,85,0,len(nums)))