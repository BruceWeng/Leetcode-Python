def compress2(nums):
    if nums == None or len(nums) == 0:
        return None

    result = []
    start = 0
    end = 1
    step = nums[end] - nums[start]
    for i in range(1, len(nums)):
        end = i
        if step == 0:
            step = nums[end] - nums[end - 1]
        if nums[end] - nums[start] != step * (end - start):
            ranges = str(nums[start]) + '-' + str(nums[end - 1]) + '/' + str(step)
            result.append(ranges)
            start = end
            step = 0

    if nums[end] - nums[start] == step * (end - start):
        if end != start:
            ranges = str(nums[start]) + '-' + str(nums[end]) + '/' + str(step)
        else:
            ranges = str(nums[end])
        result.append(ranges)

    return result

test1 = [1,2,3,5,7,8,13,20]
print compress2(test1)
test2 = [1, 2, 3, 4, 6, 8, 10]
print compress2(test2)
test3 = [2, 4, 6, 7, 8, 9, 12]
print compress2(test3)
