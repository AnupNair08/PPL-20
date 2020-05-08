#Program to display first 10 harmonic divisor numbers
from math import sqrt
def div(a):
    num = 0
    den = 0
    for i in range(1,int(sqrt(a)) + 1):
        if(a % i == 0):
            # print(i, a / i)
            den += 1/i
            num += 1
            if(a // i != a % (a // i)):
                den += 1/ (a//i)
                num += 1
    k = num / den
    k = round(k,4)
    if (k.is_integer()):
        return True
    else:
        return False



print("First 10 Harmonic Divisor numbers are :")
count = 0
i = 1

while(count < 10):
    if(div(i) == True):
        print(i)
        count += 1
    i += 1