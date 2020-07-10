# RUN TIME: O(n^2)
# IDEA:     REPEATEDLY FINDING THE MINIMUM ELEMENT CONSIDERING ASCENDING ORDER FROM UNSORTED PART
#           AND PUTTING IT AT THE BEGINNING
# HOW:      FIND THE MINIMUM IN RANGE 0 - N -> PLACE AT THE BEGINNING
#           FIND THE MINUMIN IN RANGE 1 - N -> PLACE AT THE BEGINNING...
def Selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[min_idx]>arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
arr = [64, 25, 12, 22, 11]
Selection_sort(arr)
print(arr)