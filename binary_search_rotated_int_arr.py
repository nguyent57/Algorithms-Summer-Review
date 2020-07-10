# ASSIGN MID ELEMENT INDEX OF THE ARRAY
def binary_search_rotated_int_arr(arr,l,h,x):
    while l<=h:
        mid = l + (h - l) // 2
        # IF MID INDEX IS EQUAL TO X, RETURN IT
        if arr[mid]==x:
            return mid
        # IF ARR[left] <= ARR[mid] --> sorted array
        if arr[l] <= arr[mid]:
            # CHECK TO SEE IF X LIES BETWEEN OR WITHIN LEFT INDEX AND MID
            if x >= arr[l] and x <= arr[mid]:
                # RETURN LEFT HALF VALUE
                return binary_search_rotated_int_arr(arr,l,mid-1,x)
            # OR RETURN RIGHT HALF VALUE
            return binary_search_rotated_int_arr(arr,mid+1,h,x)
        # ROTATED ARRAY WHERE ARRAY[left->mid] IS NOT SORTED
        # CHECK IF X LIES BETWEEN MID TO HIGH
        if x >= arr[mid] and x <= arr[h]:
            # RETURN THE VALUE FROM VALUE TO THE RIGHT OF MID TO HIGH OF RECURSIVE FUNC
            return binary_search_rotated_int_arr(arr, mid+1, h, x)
        # OR RETURN VALUE FROM LOW TO MID OF RECURSIVE FUNC
        return binary_search_rotated_int_arr(arr,l,mid-1,x)
    return -1

arr=[5,6,7,8,9,10,4]
x = 6
# CALL THE FUNCTION
res = binary_search_rotated_int_arr(arr,0,len(arr)-1,x)
# IF THE FUNCTION DOES NOT RETURN NOTHING, THEN THE ANSWER IS...
if res !=-1:
    print("its index is at %d"%res)
# ELSE, X HAS NOT MATCHED THE ARRAY
else:
    print("nothing")

