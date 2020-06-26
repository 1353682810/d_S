def baoli(nums, he):
    for i in range(len(nums)):
        n = 0
        for j in nums[i + 1:]:
            n += 1
            if j + nums[i] == he:
                return i, n + i
                break
    return None

print(baoli([2, 7, 11, 15], 9))


def nums_dict(nums, he):
    dict = {}
    for i in range(len(nums)):
        temp = he - nums[i]
        if temp in dict:
            return dict[temp], i
            break
        else:
            dict[nums[i]] = i
    return None

print(nums_dict([1, 3, 7, 66, 35, 78, 2, 10], 9))


def duizhaung(nums, he):
    nums1=nums[:]
    nums.sort()
    head = 0
    tail = len(nums) - 1
    while head<tail:
        sum = nums[head] + nums[tail]
        if sum == he:
            left=nums[head]
            right=nums[tail]
            head +=1
            tail -=1
        else:
            if sum<he:
                head +=1
            elif sum>he:
                tail -= 1
        if nums1.index(left)>nums1.index(right):
            return nums1.index(right),nums1.index(left)
        else:
            return nums1.index(left), nums1.index(right)

print(duizhaung([ 3,3], 6))


