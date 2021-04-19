s=input()
p=input()
ans=[]
t=p+"$"+s
z=[0]*len(t)
l=0
r=0
for k in range(1,len(t)):
    if k>r:
        l=k
        r=k
        while(r<len(t) and t[r]==t[r-l]):
            r+=1
        z[k]=r-l
        r-=1
    else:
        k1=k-l
        if z[k1]<r-k+1:
            z[k]=z[k1]
        else:
            l=k
            while(r<len(t) and t[r]==t[r-l]):
                r+=1
            z[k]=r-l
            r-=1
for i in range(len(z)):
    if len(p)==z[i]:
        print(i-len(p)-1)
