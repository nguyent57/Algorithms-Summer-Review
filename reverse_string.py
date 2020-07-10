# METHOD 1 USING STACK
# RUN TIME: O(n)
# CREATE A FUNCTION TAKES IN ANY STRING
def recursive_Reverse(str):
    # CREATE A STACK ARRAY
    stack=[]
    # FOR EVERY ELEMENT IN THE RANGE OF THE STR
    for i in range(len(str)):
        # APPEND IT INTO THE ARRAY CHAR BY CHAR
        stack.append(str[i])
    # FOR EVERY ELEMENT IN THE RANGE OF THE STR
    for i in range(len(str)):
    # current stack =
    # ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 't', 'e', 's', 't']
    # STACK = LAST IN FIRST OUT
        str[i]=stack.pop()
str = "this is a test"
str = list(str) # CONVERT STRING INTO LIST SINCE STR DOES NOT SUPPORT ITEM ASSIGNMENT
recursive_Reverse(str)
str = ''.join(str) # JOIN THE POPPED ITEM BACK AS ONE SINGLE STRING
print(str)

# METHOD 2 ITERATIVE
def reverseStr(str):
    str1 = ''
    i = len(str)-1