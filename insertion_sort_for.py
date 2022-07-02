# Python: InsertionSort

list = [0, 2, 3, 5, 11, 7, 1]
print(list)


def insertionSort(list):
    for i in range(1,len(list)):
        for j in range(i-1, -1, -1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
            else:
                break
            print(list)

insertionSort(list)
