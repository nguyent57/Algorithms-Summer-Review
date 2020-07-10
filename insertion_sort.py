# RUN TIME: O(n^2)
# USES FOR: WHEN NUMBER OF ELEMENTS IS SMALL. ALSO USEFUL WHEN INPUT ARRAY IS ALMOST SORTED
def Insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i] # SET KEY TO BE CURRENT ELEMENT
        # SHIFT ALL ELEMENTS of arr[0->i-1], that are greater than key
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
arr = [12, 11, 13, 5, 6]
Insertion_sort(arr)
print(arr)