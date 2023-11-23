def leap(year):
    if year%400==0:
        return True
    elif year%4==0 and year%100!=0:
        return True
    else:
        return False
s,e=map(int,input().split())
l=[i for i in range(s,e+1)if leap(i)]
print(len(l))
