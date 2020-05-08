#Program to find first 10 pairs of amicable numbers
from math import sqrt
def sod(a):
    sum = 0
    for i in range(2,int(sqrt(a)) + 1):
        if(a % i == 0):
            sum += i
            if(a // i != a % (a // i)):
                sum += a//i 
    return sum + 1


print("First 10 amicable numbers are")
count = 0
i = 1
l = 0
while(count < 10):
    k = sod(i)
    if(sod(k) == i and i != k):
        print(i,k)
        l = k
        count += 1
    if(i == l - 1):
        i += 2
    else:
        i += 1
