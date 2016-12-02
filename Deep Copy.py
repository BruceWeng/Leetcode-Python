def deepCopy(obj1, obj2):
    stack = []
    for key in obj2:
        stack.append(key)
    while stack:
        top = stack.pop()

        if type(top) == dict:
            for key in top:
                stack.append(top[key])
                obj1[key] = obj2[key]
        else:
            obj1[top] = obj2[top]

    return obj1
obj1 = {'A': 1, 'B': 3, 'C': 4}
obj2 = {'A': 2, 'B': {'b': 5}}
print deepCopy(obj1, obj2)
obj2['B'] = 3
print obj1
print obj2
