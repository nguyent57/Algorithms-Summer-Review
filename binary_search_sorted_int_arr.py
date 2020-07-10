# ASSIGN MID ELEMENT INDEX OF THE ARRAY
def binary_search_sorted_int_arr(arr,l,h,x):
    while l<=h:
        mid = l + (h - l) // 2
        # IF MID INDEX IS EQUAL TO X, RETURN IT
        if arr[mid]==x:
            return mid
        # IF MID INDEX IS SMALLER THAN X, THAT MEANS X IS ON THE RIGHT OF MID
        # THEREFOR, ASSIGN LOW ELEMENT TO BE ONE ELEMENT TO THE RIGHT OF MID AND RECALCULATE MID
        elif arr[mid] < x:
            l = mid + 1
        # ELSE IT WILL BE ON THE LEFT OF MID, THEREFOR ASSIGN HIGH ELEMENT TO BE THE ONE ON THE LEFT OF MID
        # THEN RECALCULATE THE MID
        else:
            h = mid -1
    return -1

arr=[5,6,7,1,2,3,4]
x = 1
# CALL THE FUNCTION
res = binary_search_sorted_int_arr(arr,0,len(arr)-1,x)
# IF THE FUNCTION DOES NOT RETURN NOTHING, THEN THE ANSWER IS...
if res !=-1:
    print("its index is at %d"%res)
# ELSE, X HAS NOT MATCHED THE ARRAY
else:
    print("nothing")

