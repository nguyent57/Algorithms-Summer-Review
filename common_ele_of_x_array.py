# CREATE A FOR LOOP THAT WOULD LOOK THROUGH EVERY ARRAY
# AS LONG AS THE CURRENT ELEMENT OF EACH ARRAY IS LESS THEN THE LENGTH OF ITS ARRAY
# IF THE CURRENT ELEMENT OF ARRAY1 = ELEMENT OF ARRAY2 AND ELEMENT OF ARRAY2 = ELEMENT OF ARRAY3
# PRINT CURRENT ELEMENT OF ANY ARRAY AND INCREMENT EACH ARRAY POSITION
# ELSE IF CURRENT ELEMENT OF ARRAY1 DOES NOT MATCH WITH CURRENT ELEMENT OF ARRAY2
# INCREMENT ith ELEMENT OF ARRAY1
# ELSE IF CURRENT ELEMENT OF ARRAY2 DOES NOT MATCH WITH CURRENT ELEMENT OF ARRAY3
# INCREMENT jth ELEMENT OF ARRAY 2
# ELSE -> JUST INCREMENT kth
def common_element(arr1, arr2, arr3, n1, n2, n3):
    i,j,k=0,0,0
    while (i<n1 and j<n2 and k<n3):

        if arr1[i] == arr2[j] and arr2[j] < arr3[k]:
            print(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i]<arr2[j]:
            i += 1
        elif arr2[j]<arr3[k]:
            j += 1
        else:
            k += 1
arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
n1 = len(arr1)
n2 = len(arr2)
n3 = len(arr3)
print(common_element(arr1, arr2, arr3, n1, n2, n3))