# RUN TIME: WOSRT CASE O(n^2)
#           BEST CASE  O(n) when array is already sorted
# https://www.geeksforgeeks.org/bubble-sort/
def Bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            # IF CURRENT ELEMENT IS BIGGER THAN THE NEXT ELEMENT
            if arr[j] > arr[j+1]:
                # SWAP POSITION
                arr[j], arr[j+1] = arr[j+1],arr[j]
arr = [64, 34, 25, 12, 22, 11, 90]
Bubble_sort(arr)
print(arr)