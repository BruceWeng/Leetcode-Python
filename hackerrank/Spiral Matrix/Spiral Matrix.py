def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if len(matrix) == 0 or len(matrix[0]) == 0 or matrix == None:
        return []

    x = 0
    y = 0
    row = len(matrix)
    col = len(matrix[0])
    result = []
    while row > 0 and col > 0:
        if row == 1:
            for i in range(col):
                result.append(matrix[x][y])
                y += 1
            break
        if col == 1:
            for i in range(row):
                result.append(matrix[x][y])
                x += 1
            break
        for i in range(col-1):
            result.append(matrix[x][y])
            y += 1

        for i in range(row-1):
            result.append(matrix[x][y])
            x += 1

        for i in range(col-1):
            result.append(matrix[x][y])
            y -= 1

        for i in range(row-1):
            result.append(matrix[x][y])
            x -= 1

        row -= 2
        col -= 2
        x += 1
        y += 1

    print ''.join(result)

def main():
    matrix = []
    while True:
        try:
            temp = raw_input().split(' ')
            matrix.append(temp)
        except EOFError:
            break
    spiralOrder(matrix)

if __name__ =='__main__':
    main()
