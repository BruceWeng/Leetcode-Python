def cityNumber(edges):
    '''
    type edges: Int List
    rtype result: Int List
    '''
    result = [0 for i in range(len(edges) - 1)]
    # Init Graph
    adjList = [set() for i in range(len(edges))]
    # Build Graph and find root
    root = 0
    for k, v in enumerate(edges):
        if k == v:
            root = k

        adjList[k].add(v)
        adjList[v].add(k)

    # Build obj with props of node and dist
    obj = {'node': root, 'dist': -1}
    stack = [obj]
    visited = set()
    visited.add(root)
    # DFS:
    # 1. Pop node from stack, obj = stack.pop()
    # 2. Put neighbors for i in range(len(adjList[obj['node']])) {'node': i, 'dist' obj['dist'] + 1} in stack
    # 3. visited[obj['node']] = True
    # 4. if obj['dist'] > 1: result[obj['dist']] += 1
    while stack:
        obj = stack.pop()
        for i in adjList[obj['node']]:
            if i not in visited:
                stack.append({'node': i, 'dist': obj['dist'] + 1})
                visited.add(i)

        if obj['dist'] > -1:
            result[obj['dist']] += 1

    return result

test1 = [9, 1, 4, 9, 0, 4, 8, 9, 0, 1]
print cityNumber(test1)
