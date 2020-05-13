l=list(map(int,input().split()))
dl=l[::-1]
ans=[-1]*len(l)
inc=[1]*len(l)
dec=[1]*len(l)
for i in range(1,len(l)):
    for j in range(i):
        if l[j]<l[i]:
            inc[i]=max(inc[i],inc[j]+1) #increasing sub sequence from 1 to n
        if dl[j]<dl[i]:
            dec[i]=max(dec[i],dec[j]+1) #increasing sub sequence from n to 1
dec=dec[::-1] #reverse again
for i in range(len(l)):
    ans[i]=ans[i]+inc[i]+dec[i] #inc+dec-1  excluding particular number 
print(max(ans))