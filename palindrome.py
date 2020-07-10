def palindrom(str):
    # CREATE AN EMPTY STRING FOR PALINDROME
    w = ''
    # FOR EVERY ITEM IN GIVEN STR
    for i in str:
        # EMPTY STR WILL ADD THE NEXT ELEMENT TO CURRENT AVAILABLE IN w
        w = i+w
        print(w)
        # ONCE THE STR IS EQUAL TO w
        if (str==w):
            print('yes')
        else:
            print('no')

str = 'malam'
palindrom(str)

