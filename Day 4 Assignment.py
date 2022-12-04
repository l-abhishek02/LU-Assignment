def prime(l1):
    l2=[]
    cnt=0
    for x in l1:
        for y in range(1,x+1):
            if(x%y==0):
                cnt+=1
        if(cnt==2):
            l2.append(x)
        cnt=0
    return l2

l1=[]
for x in range(1,101):
    l1.append(x)
l2=prime(l1)
print(l2)
