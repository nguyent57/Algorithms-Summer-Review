#1. USING NAIVE APPROACH
# COUNT FREQUENCY OF EACH ELEMENT
def most_frequent(List):
    counter = 0 # SET counter = 0
    num = List[0] # SET num to be 1st element
    for i in List: # FOR EVERY ITEM IN LIST
        # SET THE CURRENT FREQUENCY TO THE COUNT OF THE ith ELEMENT
        curr_frequency = List.count(i)
        # IF THE CURRENT FREQUENCY IS GREATER THAN THE PREVIOUS FREQUENCY
            # UPDATE THE COUNTER AND STORE THE ELEMENT
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i
    # RETURN THE ELEMENT
    return num
List = [2, 1, 2, 2, 1, 3]
print(most_frequent(List))

#==================================================================================
#2. USING PYTHONIC NAIVE APPROACH
def most_frequent(List):
    return max((List), key = List.count)

List = [2, 1, 2, 2, 1, 3, 1]
print(most_frequent(List))

#==================================================================================
#3. USING Counter IMPORTATION FROM COLECTIONS
from collections import Counter
def most_frequent(List):
    occurence_count = Counter(List)
    # cases:
    # 1. when (n) is not specified, returns a list of all elements and their frequencies
    # 2. when (n) is specified, return n number of most frequencies
    # 3. when (n) is not specified and [0][0] is used, return the most frequency
    # 4. when (n) is not specified and [0][1] is used, return the least frequency
    return occurence_count.most_common()[0][0]
List = [2, 1, 2, 2, 1, 3]
print(most_frequent(List))

#==================================================================================
#4. USING THE FIND OF MODE - MOST COMMON VALUE.

import statistics
from statistics import mode
def most_common(List):
    return mode(List)
List = [2, 1, 2, 2, 1, 3]
print(most_common(List))

#==================================================================================
#5. USING PYTHON DICTIONARY
def most_frequent(List):
    dict = {}
    count, itm = 0, ''
    for item in List:
        dict[item] = dict.get(item,0) + 1
        if dict[item] >= count:
            count, itm = dict[item], item
            return itm
List = [2, 1, 2, 2, 1, 3]
print(most_common(List))





