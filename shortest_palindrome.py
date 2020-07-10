# RUN TIME
# USE:  TAKE THE REVERSE STRING OF THE GIVEN STRING AND BRING IT TO THE END
#       TO SEE WHAT IS THE SUFFIX OF THE STRING COMPARING TO THE PREFIX OF THE STRING
#       REMOVE THE SUFFIX --> SHORTEST PALINDROME
def palindrom(str):
    # CREATE AN EMPTY STRING FOR PALINDROME
    reverse = ''
    # FOR EVERY ITEM IN GIVEN STR
    for char in str:
        # EMPTY STR WILL ADD THE NEXT ELEMENT TO CURRENT AVAILABLE IN w
        reverse = char + reverse
        #print(reverse)
        """
        DAD -> DAD 
        => IF THE REVERSE OF THE GIVEN STRING IS EXACTLY THE SAME => ALREADY PALINDROME
        """
    if reverse == str:
        print(str)
        """
        BANANA -> BANANAB 
        => COMPARE EVERY CHAR OF REVERSE STRING EXCEPT THE LAST CHAR WITH
        => STARTING OF THE INDEX 1 OF ORIGINAL STRING
        => IF THE SAME, THEN CREATE A STRING OF ORIGINAL STRING WITH THE LAST ELEMENT OF THE REVERSE STR
        """
    elif reverse[:-1] == str[1:]:
        print(reverse[:-1])
        pal = str + reverse[-1]
        print(pal)
        """
        ANAA -> AANAA
        => COMPARE EVERY CHAR OF REVERSE STRING FROM INDEX 1 WITH 
        => EVERY CHAR OF ORIGINAL STR EXCEPT LAST CHAR
        => IF THE SAME, THEN CREATE A STRING OF THE FIRST CHAR OF REVERSE STR WITH ORIGINAL STR
        """
    elif reverse[1:] == str[:-1]:
        pal = reverse[1] + str
        print(pal)
        """
        TOM -> TOMOT
        => ELSE, CREATE A STRING OF ORIGINAL STR WITH REVERSE STR STARTING FROM INDEX 1
        """
    else:
        pal = str + reverse[1:]
        print(pal)



str=input()
palindrom(str)

