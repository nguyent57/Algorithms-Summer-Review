# METHOD 1: USING A FUNCTION
# RUN TIME: O(n)
# CREATE A FUNCTION THAT WOULD TAKE ANY STRING
def all_unique_char(str):
    # CREATE A DICTIONARY TO STORE THE COUNT OF EACH CHARACTER
    count = {}
    # CREATE AN ARRAY TO STORE THE CHAR
    char = []
    # FOR EVERY ITEM IN STRING
    for i in str:
        # IF THE COUNT EXIST -> INCREMENT BY ONE
        if i in count:
            count[i] +=1
        # ELSE SET IT TO ONE AND APPEND THE CHAR INTO THE ARRAY
        else:
            count[i] = 1
            char.append(i)
    # FOR EVERY ITEM IN CHAR ARRAY
    for i in char:
        # IF THE COUNT IS LARGER THAN 1
        if count[i] > 1:
            # RETURN FALSE
            return False
    # OR RETURN TRUE IF EXISTS
    return True
str = 'TOM'
print(all_unique_char(str))

