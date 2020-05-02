from math import sqrt
def divisor(a):
    count = 0
    sum = 0
    for i in range(1,int(sqrt(a))):
        if( a % i == 0 and i != a//i):
            sum += 1 / i
            sum += i / a
            count += 2
        elif( a % i == 0 and i == a// i):
            sum += 1 / i
            count += 1
    
    print(count,sum)


i = 0
j = 1
for i in range(10):
    divisor(j)