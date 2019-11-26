# 给定 nums = [2, 7, 11, 15], target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
nums = [3, 2, 4]
target = 6
# 暴力解析 双重循环 时间复杂度 O(n²)
flag = False
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] + nums[j] == target and i != j:
            print([i, j])
            flag = True
            break
    if flag:
        break
# 相加运算 单循环 时间复杂度 O(n)  以下为错误示例 当序列中有重复数据时 不适用
flag = False
for i in range(len(nums)):
    if (target - nums[i]) in nums:
        if i != nums.index(target - nums[i]):
            print([i, nums.index(target - nums[i])])
            flag = True

    if flag:
        break
# 正确示例 分治
j = -1
for i in range(len(nums)):
    temp = nums[i + 1:]
    num = target - nums[i]
    if num in temp:
        j = temp.index(num) + i + 1
        break
if j >= 0:
    print([i, j])
