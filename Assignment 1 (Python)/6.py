t = int(input())
while(t):
    l = [int(i) for i in input().split()]
    n = l[0]
    s = l[1]
    price = [int(i) for i in input().split()]
    tp = [int(i) for i in input().split()]

    m1 = min(price)
    i = price.index(m1)
    s += m1
    if(i == 0):
        ck = 1
    else:
        ck = 0
    p = []
    for i in range(len(price)):
        if(tp[i] == ck):
            p.append(price[i])

    s += min(p)
    # print(s)
    if(s <= 100):
        print("yes")
    else:
        print("no")
    t -= 1

