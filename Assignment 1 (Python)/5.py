print("Enter the list")
l = [str(i) for i in input().split()]
rl = []
for ele in l:
    if(len(ele) == 1 or len(ele) == 2):
        rl.append(int(ele))
    elif(len(ele) == 3):
        n = int(ele[0])
        m = int(ele[2])
        for i in range(n,m+1):
            rl.append(i)
    elif(len(ele) == 4):
        n = int(ele[0])
        m = int(ele[2:4])
        for i in range(n,m+1):
            rl.append(i)
    else:
        n = int(ele[0:2])
        m = int(ele[3:5])
        for i in range(n,m+1):
            rl.append(i)
print("Missing Pages are : ")
for i in range(1,26):
    if(i not in rl):
        print(i,end = " ")
print()
