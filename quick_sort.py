# THERE ARE MULTIPLE WAYS TO DO QUICKSORT
# 1. PICK THE low ELEMENT
# 2. PICK THE high ELEMENT
# 3. PICK A RANDOM ELEMENT
# 4. PICK MEDIAN
#====================================
#  WORST    CASE:   O(n^2)          #
#  BEST     CASE:   O(n log n)      #
# AVERAGE   CASE:   O(n log n)      #
#====================================
# FOR METHOD 2:
'''def partition(arr,low, high):
    i = low - 1         # ASSIGN i TO BE INDEX OF SMALLER ELEMENT
    pivot = arr[high]   # ASSIGN high element TO BE THE PIVOT
    for j in range(low, high): # FOR EVERY ELEMENT FROM RANGE LOW TO HIGH
        # CHECKS IF jth position IS SMALLER THAN PIVOT OR NOT
        if arr[j] < pivot:
            i+=1 # INCREMENT ith BY ONE
            arr[i],arr[j] = arr[j],arr[i]   # SWAP ith AND jth POSITION
    arr[i+1],arr[high] = arr[high],arr[i+1] # SWAP ith + 1 position (near high) with high element
    return i+1
def quickSort2(arr,low,high):
    # CHECK IF low element is smaller than high
    if low < high:
        # CALL PARTITION FUNCTION
        pi = partition(arr,low,high)
        # SEPARATELY SORT ELEMENT BEFORE PARTITION AND AFTER PARTITION
        quickSort2(arr, low, pi-1)
        quickSort2(arr, pi+1, high)
arr = [10,9,8,4,3,5]
quickSort2(arr,0,len(arr)-1)
print("Sorted!")
for i in range(len(arr)):
    print("%d" %arr[i])
'''



# FOR METHOD 1:   https://www.thecrazyprogrammer.com/2017/12/python-quick-sort.html
def quickSort(arr):

  QShelper(arr,0,len(arr)-1)

def QShelper(arr,low,high):
    print('QShelper',(arr,low,high))
    if low<high:
      splitpoint = partition1(arr,low,high)
      QShelper(arr,low,splitpoint-1)
      QShelper(arr,splitpoint+1,high)

def partition1(arr,low,high):
  pivot = arr[low] # SET FIRST ELEMENT TO BE THE PIVOT
  i = low+1        # SET ith ELEMENT TO BE ELEMENT NEXT TO THE PIVOT
  j = high         # SET jth ELEMENT TO BE THE LAST ELEMENT
  done = False
  while not done:
      # WHILE THE ith ELEMENT IS LESS THAN/ EQUAL TO jth ELEMENT     # AND arr[i] IS LESS THAN/ EQUAL TO THE PIVOT
      while i <= j and arr[i] <= pivot:
          i = i + 1 # INCREMENT ith ELEMENT
          if i < len(arr):
            print('case1i',arr[i])
          if j >= 0:
            print('case1j',arr[j])
          print('pivot',pivot,'\n---\n')
      # WHILE THE arr[j] IS LARGER/ EQUAL TO THE PIVOT     # AND jth IS LARGER/ EQUAL TO ith ELEMENT
      while arr[j] >= pivot and j >= i:
          j = j - 1 # DECREMENT jth ELEMENT
          if i < len(arr):
              print('case2i', arr[i])
          if j >= 0:
              print('case2j', arr[j])
      # CHECK IF jth ELEMENT IS LESS THAN ith     # IF YES, THEN SET THE CONDITION BACK TO TRUE AND MAKE SWITCH IN 78
      if j < i:
          done = True
      # IF NOT, MAKE A SWAP BETWEEN THE arr[i] and arr[j]
      else:

          arr[i], arr[j] = arr[j], arr[i]
          print('swap ', (i,j),arr[i], arr[j], 'to ',arr[j], arr[i])
  '''temp = arr[low]
  arr[low] = arr[j]
  arr[j] = temp'''
  arr[low], arr[j] = arr[j], arr[low]
  print('swap2 ', (i,j), arr[low], arr[j], 'to ', arr[j], arr[low])
  return j

arr = [ 8, 9, 1, 5]
quickSort(arr)
print(arr)
