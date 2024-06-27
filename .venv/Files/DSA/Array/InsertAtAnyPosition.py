def insertElement(arr, n, x, pos):
    for i in range(n-1, pos-1, -1):
        arr[i + 1] = arr[i]

    arr[pos] = x

if __name__ == "__main__":
    arr = [2, 4, 1, 8, 5, -1, -1, -1, -1, -1 ,-1, -1, -1, -1, -1]
    n = 5

    print("Before Insertion: ")
    for i in range(0, n):
        print(arr[i], end=' ')
    print("\n")

    x = 10
    pos = 2
    insertElement(arr, n, x, pos)

    print("After Insertion: ")
    for i in range(0, n):
        print(arr[i], end = ' ')