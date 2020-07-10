def square_root(x):
    # BASE CASE WHEN X == 0 OR X == 1, JUST RETURN X
    if (x == 0 or x == 1):
        return(x)
    # STARTING VALUE FROM 2 SINCE WE ALREADY CHECKED FOR BASE CASE
    i = 2
    # PERFECT SQUARE IS THE SQUARE NUMBER ON THE RIGHT OF THE GIVEN NUMBER
    # SAY, WE HAVE 7 -> PERSQUARE IS 9, 3 PERSQUARE IS 4
    persquare = 2
    # AS LONG AS PERFECT SQUARE IS <= X -> INCREMENT ith BY ONE AND 
    # CALCULATE THE PERFECT SQUARE, EXIT WHILE LOOP WHEN LARGER.
    while (persquare <= x):
        i += 1
        persquare = i * i
    # CALCULATE THE ROOT OF THE PERSQUARE
    sqrtpersquare = (persquare/i)
    # DIVIDE NUMBER BY THE GIVEN NUMBER
    xnew = x/sqrtpersquare
    # THEN CALCULATE THAT NUMBER'S AVG BY ADDING THAT NUMBER WITH THE ROOT OF PERSQUARE
    avgxnew = (xnew + sqrtpersquare)/2
    # REPEAT THE PROCESS: X/AVGNEW = AVGNEW-> (AVGXNEW + AVGNEW)/2
    avgnew = x /avgxnew
    newavg = round((avgxnew + avgnew)/2,3)
    sqrt = newavg*newavg
    if sqrt>x:
        avgnew = x/newavg
        newavg = round((newavg + avgnew) / 2, 3)
        sqrt = newavg * newavg
        if sqrt > x:
            newavg = round((newavg + avgnew) / 2, 3)
            return (newavg)
    return(newavg)
# Driver Code
x = 4
print(square_root(x))
x = 5
print(square_root(x))
x = 7
print(square_root(x))
x = 9
print(square_root(x))

