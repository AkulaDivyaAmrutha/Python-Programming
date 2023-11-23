def arm(n):
    s=0
    temp=n
    while n!=0:
        r=n%10
        s=s+r*r*r
        n=n//10
    if s==temp:
        return True
    else:
        return False
n=int(input())
l=[i for i in range(1,n+1)if arm(i)]
for i in l:
    print(i,end=' ')
