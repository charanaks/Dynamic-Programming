bw=int(input())
wt=list(map(int,input().split()))
v=list(map(int,input().split()))
dp=[[0 for m in range(bw+1)]for n in range(len(wt)+1)]
for i in range(len(wt)+1):
    for j in range(bw+1):
        if i==0 or j==0:
            dp[i][j]=0
        elif wt[i-1]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-wt[i-1]]+v[i-1])
print(dp[len(wt)][bw])