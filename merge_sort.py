# RUN TIME: O(n log n)
# USES FOR: SORTING LINKED LISTS
# IDEA:
    # SPLIT ARRAY INTO TWO HALVES -> SORT LEFT AND RIGHT -> SORT BOTH SIDE -> MERGE BACK
def Merge_sort(arr):
    n = len(arr)
    # IF LENGTH IS GREATER THAN 1
    if n > 1:
        # DIVIDE IT INTO 2 HALVES
        mid = n//2
        # LEFT SIDE IS FROM 0 TO MID
        left = arr[:mid]
        # RIGHT SIDE IS FROM MID TO END
        right = arr[mid:]
        # SORT THE LEFTSIDE
        Merge_sort(left)
        # SORT THE RIGHT SIDE
        Merge_sort(right)
        # INITIALIZE i FOR LEFT, j FOR RIGHT, k FOR ENTIRE ARRAY
        i = 0
        j = 0
        k = 0
        #      [12, 11, 13]      [5, 6, 7]
        while i < len(left) and j < len(right):
            # IF I LEFT SIDE IS SMALLER THAN RIGHT SIDE
            if left[i] < right[j]:
                # ASSIGN arr[k] AS ELEMENT OF left[i]
                arr[k] = left[i]
                # THEN INCREMENT ith ELEMENT ON LEFT
                i+=1
            else:
                # arr[k] = [5] -> [5, 6] -> [5, 6 ,7] -> right side finished -> move to line 41
                # IF NOT, ASSIGN arr[k] AS ELEMENT OF right[j]
                arr[k] = right[j]
                # THEN INCREMENT jth ELEMENT ON RIGHT
                j+=1
            # INCREMENT k AFTER EACH PLACEMENT
            k+=1
        # CONDITION TO CHECK IF LEFT IS MORE THAN RIGHT OR RIGHT IS MORE THAN LEFT
        while i < len(left):
            # arr[k] = [5, 6, 7, 11] -> [5, 6, 7, 11, 12] - [5, 6, 7, 11, 12, 13]
            arr[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1
arr = [12, 11, 13, 5, 6, 7]
Merge_sort(arr)
print(arr)
