a=list(map(int,input().split()))
dp=[100000000]*len(a)
dp[0]=0
for i in range(1,len(a)):
    for j in range(i):
        if a[j]+j>=i:
            dp[i]=min(dp[i],dp[j]+1)
print(dp[len(a)-1])