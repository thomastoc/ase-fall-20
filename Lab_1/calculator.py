#calc.py

def sum(m, n):
    sumRes = m
    while(n > 0):
        sumRes += 1
        n = n - 1

    return sumRes

def divide(m, n):
    tempM = abs(m)
    tempN = abs(n)
    divRes = 0
    while(tempM >= tempN):
        tempM -= tempN
        divRes += 1

    if((m < 0 and not n<0) or (n < 0 and not m<0)):
        return -divRes
    
    return divRes

valu = sum(5,3)
print(valu)
valu = divide(15,5)
print(valu)
