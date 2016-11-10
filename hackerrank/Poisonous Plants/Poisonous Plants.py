def main():
    q = input()
    array = input().split(' ')
    arrayInt = [int(a) for a in array]
    print(poisonousPlants(arrayInt))

def poisonousPlants(arrayInt):
    count = 0

    while True:
        temp = [arrayInt[0]]
        for i in range(1, len(arrayInt)):
            if arrayInt[i] <= arrayInt[i-1]:
                temp.append(arrayInt[i])

        if len(temp) == len(arrayInt):
            break
        arrayInt = temp
        count += 1

    return count


if __name__ == '__main__':
    main()
