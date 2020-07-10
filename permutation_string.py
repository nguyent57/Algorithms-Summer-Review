def permutation1(list):
    if len(list) == 0: # IF THE LIST DOESN'T HAVE ANYTHING, RETURN NOTHING
        return []
    elif len(list) == 1: # IF THE LIST HAS ONLY ONE ELEMENT, RETURN THAT ELEMENT
        return [list]
    else:
        l = []
        for i in range(len(list)):
            # LET x BE ith ELEMENT IN ARRAY
            x = list[i]
            # LET xs BE ELEMENT UP TILL ith (NOT INCLUDE ith element)
            # AND FROM ith's next element UNTIL THE END
            xs = list[:i] + list[i+1:]
            # RECURSIVE
            for p in permutation1(xs):
                l.append(([x]+p))
        return l


# USED FOR BIGGER LIST
def permutation2(list):
    if len(list) == 0: # IF THE LIST DOESN'T HAVE ANYTHING, RETURN NOTHING
        yield []
    elif len(list) == 1: # IF THE LIST HAS ONLY ONE ELEMENT, RETURN THAT ELEMENT
        yield list
    else:
        for i in range(len(list)):
            # LET x BE ith ELEMENT IN ARRAY
            x = list[i]
            # LET xs BE ELEMENT UP TILL ith (NOT INCLUDE ith element)
            # AND FROM ith's next element UNTIL THE END
            xs = list[:i] + list[i+1:]
            # RECURSIVE
            for p in permutation1(xs):
                yield ([x]+p)


data = list('abc')
for j in permutation1(data):
    print(j)
for j in permutation2(data):
    print(j)