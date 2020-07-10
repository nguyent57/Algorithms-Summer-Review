# RUN TIME: O(n log n)
# CREATE A FUNCTION THAT TAKES IN ANY 2 ARRAYS
def Anagrams(str1,str2):
    n1 = len(str1)
    n2 = len(str2)
    # CHECK IF LENGTH OF STR1 = STR2
    # IF NOT, RETURN AND DOES NOT THING
    if n1 != n2:
        return 0
    # SORT BY ARRAY FOR COMPARISON
    str1 = sorted(str1)
    str2 = sorted(str2)
    for i in range(n1):
        # IF STR1 POSITION ith IS NOT EQUAL TO STR2 POSITION ith -> RETURN FALSE
        if str1[i] != str2[i]:
            print("not")
    # RETURN TRUE
    print("correct")
str1 = "string"
str2 = "tsring"
Anagrams(str1,str2)



