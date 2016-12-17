def findMaxDiff(nums):
    '''
    type nums: int List
    rtype result: int
    '''
    # Step1: Map nums into array of dict(obj) with properties 'index' and 'value'
    # Step2: Sort array of dict(obj) by value
    # Step3: Create an array contains mostMin and create an array contains mostMax
    # Step4: Create a pointer to preValue for checking the change of the value
    # Step5: Create localMin, localMax, if obj[i].value == preValue: update localMin and localMax
    # Step6: Else: push localMin into mostMin and push localMax into mostMax
    #        localMin = obj[i].index, localMax = obj[i].index, preValue = obj[i].value
    # Step7: After traversal, result = Math.max(result, mostMax[i] - mostMin[i-1])
    objList = [{'index': index, 'value': value} for index, value in enumerate(nums)]
    objList = sorted(objList, key = lambda obj: obj['value'])
    mostMin = []
    mostMax = []
    preValue = objList[0]['value']
    localMin = objList[0]['index']
    localMax = objList[0]['index']
    result = 0
    for i in range(1, len(objList)):
        if objList[i]['value'] == preValue:
            localMin = min(localMin, objList[i]['index'])
            localMax = max(localMax, objList[i]['index'])
        else:
            mostMin.append(localMin)
            mostMax.append(localMax)
            localMin = objList[i]['index']
            localMax = objList[i]['index']
            preValue = objList[i]['value']

    mostMin.append(localMin)
    mostMax.append(localMax)
    
    for i in range(1, len(mostMax)):
        result = max(result, abs(mostMax[i] - mostMin[i-1]))

    print 'objList: ', objList
    print 'mostMin: ', mostMin
    print 'mostMax: ', mostMax
    return result

test1 = [0, 3, 3, 7, 5, 3, 11, 1]
print findMaxDiff(test1) #7
test2 = [1, 4, 7, 3, 3, 5]
print findMaxDiff(test2) #4
