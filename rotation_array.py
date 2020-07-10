def leftRotate(arr, d, n):
    # FOR EVERY ITEM IN RANGE OF D
    for i in range(d):
        # ASSIGN TEMP TO BE FIRST ELEMENT
        temp = arr[0]
        # FOR EVERY ITEM IN THE RANGE OF HOW MANY ELEMENT OF THE ARRAY
        for i in range(n - 1):
            # ASSIGN THE CURRENT ELEMENT TO BE THE NEXT ELEMENT
            arr[i] = arr[i + 1]
        # THEN ASSIGN THE LAST ELEMENT TO BE THE FIRST ELEMENT
        arr[n - 1] = temp
def printArray(arr,size):
    for i in range(size):
        print("%d" % arr[i], end =" ")
arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr,2,7)
printArray(arr,7)
