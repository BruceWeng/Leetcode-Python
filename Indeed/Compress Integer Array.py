def compress(nums):
    if nums == None or len(nums) == 0:
        return []

    result = []
    start = 0
    end = 0
    for i in range(len(nums)):
        end = i
        if end - start < nums[end] - nums[start]:
            if end - 1 != start:
                ranges = str(nums[start]) + '-' + str(nums[end - 1])
            else:
                ranges = str(nums[start])
            result.append(ranges)
            start = end

    if nums[end] != nums[start]:
        ranges = str(nums[start]) + '-' + str(nums[end])
    else:
        ranges = str(nums[start])
    result.append(ranges)

    return result
test1 = [1, 2, 3, 5, 6, 8, 10]
print compress(test1) #['1-3', '5-7', '10']
test2 = [1, 2, 2, 2, 10, 10, 10]
print compress(test2)
