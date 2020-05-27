n=int(input())
a=list(map(int,input().split()))
pos=[0]*(n+1)
pos[0]=1
neg=[0]*(n+1)
ans=0
diff=0
for i in range(len(a)):
    if a[i]%2==0:
        diff=diff-1
    else:
        diff=diff+1
    if diff<0:
        ans+=neg[-diff]
        neg[-diff]+=1
    else:
        ans+=pos[diff]
        pos[diff]+=1
print(ans)

