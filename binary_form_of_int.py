def decimalToBinary(N):
    # STORE BINARY NUMBER
    B_Number = 0
    # EXPONENTIAL COUNT
    cnt = 0
    # AS LONG AS IT IS NOT A 0
    while (N != 0):
        # CALCULATE THE REMAINDER
        rem = N % 2
        c = pow(10, cnt) # COUNT = 0 -> 10^0 =1
        # -> INCREMENT EXPONENTIAL COUNT
        cnt += 1
        #STORE THE BINARY VALUE:
        # 10^0 = 1     -> 0 + 1*1     = 1
        # 10^1 = 10    -> 0 + 10*2    = 100
        # ...
        # 10^4 = 10000 -> 1 + 1*10000 = 10001
        B_Number = B_Number + rem * c
        # ASSIGN NEW N TO BE WHOLE NUM OF THE CAL 17//2 = 8, 8//2= 4, 4//2=2, 2//2=1
        N = N // 2

    return B_Number
while True:
    N = (input())
    try:
        val = int(N)
        print(decimalToBinary(val))
    except ValueError:
        try:
            val = str(N)
            if val=='stop':
                break
            else:
                print("please input an integer")
        except ValueError:
            print("please input an integer")


