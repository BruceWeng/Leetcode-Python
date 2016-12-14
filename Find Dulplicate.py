def find1(str):
    inputs = str.split(' ')
    cache = {}
    for i in range(len(inputs)):
        if inputs[i] in cache:
            return inputs[i]
        cache[inputs[i]] = True

def find2(str):
    inputs = str.split(' ')
    cache = {}
    minIndex = len(inputs)
    for i in range(len(inputs)):
        if inputs[i] in cache:
            minIndex = min(minIndex, cache[inputs[i]])
        cache[inputs[i]] = i

    return inputs[minIndex]
    
test1 = 'Java Python C C Python'
print find1(test1)
print find2(test1)
