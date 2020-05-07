a=list(map(int,input().split()))
allneg=True
cur=0
maxneg=-1000000000
maxsum=0
for i in range(len(a)):
    if allneg and a[i]>0:
        allneg=False
    elif allneg and a[i]<0 and maxneg<a[i]:
        maxneg=a[i]
    cur+=a[i]
    if cur<0:
        cur=0
    elif maxsum<cur:
        maxsum=cur
if allneg:
    print(maxneg)
else:
    print(maxsum)
