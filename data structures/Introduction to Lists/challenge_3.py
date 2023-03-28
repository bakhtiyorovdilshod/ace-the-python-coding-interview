def find_sum(nums, k):
    result = []
    start = 0
    end = len(nums) - 1
    nums.sort()
    while start < end:
        if nums[start] + nums[end] == k:
            result.append(nums[start])
            result.append(nums[end])
            return result
        elif nums[start] + nums[end] > k:
            end = end - 1
        else:
            start = start + 1
    return False



