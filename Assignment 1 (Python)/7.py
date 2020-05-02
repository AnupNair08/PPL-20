n = int(input('Enter starting of range : '))
m = int(input('Enter ending of range : '))

def arms(a):
    temp = a
    sum = 0
    while(a):
        sum += (a % 10)**3
        a //= 10
    if(sum == temp):
        return 1
    else:
        return 0

print("Armstrong Numbers in the given range are: ")
for i in range(n,m+1):
    if(arms(i)):
        print(i)


    
