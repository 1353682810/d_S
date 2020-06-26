# 从有序数组中去除重复元素
# eg:输入[1,1,2]  去重后[1,2],输出2
# eg:输入[0,0,1,1,1,2,2,3,3,4],去重后[0,1,2,3,4],输出5
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


# 今天思考题:leetcode27
# 给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O (1) 额外空间的条件下完成。
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
# 示例 1:
# 给定 nums = [3,2,2,3], val = 3,
# 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。
# 示例 2:
# 给定 nums = [0,1,2,2,3,0,4,2], val = 2,
# 函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0,
# 4。注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。
print("-----------"*3)
nums = [3,2,2,3]
val=3
list=[]
n=0
for i in range(len(nums)):
    if nums[i] !=val:
       list.append(nums[i])
       n +=1
print(list,n)

print("--------------"*3)

nums = [0,1,2,2,3,0,4,2]
val=2
list=[]
n=0
for i in range(len(nums)):
    if nums[i] !=val:
       list.append(nums[i])
       n +=1
print(list,n)

