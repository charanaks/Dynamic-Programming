l=list(map(int,input().split()))
inc=[1]*len(l)
for i in range(1,len(l)):
    for j in range(i):
        if l[j]<l[i]:
            inc[i]=max(inc[i],inc[j]+1)
print(max(inc))