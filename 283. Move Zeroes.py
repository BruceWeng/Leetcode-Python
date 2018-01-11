def moveZeros(nums):
    if nums == None or len(nums) == 0:
        return
    # Find the insert position to insert non zero numbers and insert zero from
    # the last insert position to the end of list
    insertPos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insertPos] = nums[i]
            insertPos += 1
    for i in range(insertPos, len(nums)):
        nums[i] = 0
