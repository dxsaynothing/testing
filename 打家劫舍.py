def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    pre, cur = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        # 迭代更新pre和cur
        pre, cur = cur, max(cur, pre + nums[i])
    return cur

# 测试示例
print(rob([1,2,3,1]))    # 4
print(rob([2,7,9,3,1]))  # 12