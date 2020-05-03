rl=int(input())
wt=list(map(int,input().split()))
v=list(map(int,input().split()))
dp=[[0 for m in range(rl+1)]for n in range(len(wt)+1)]
for i in range(len(wt)+1):
    for j in range(rl+1):
        if i==0 or j==0:
            dp[i][j]=0
        elif wt[i-1]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-wt[i-1]]+v[i-1]) #This line differs this problem from 0/1 knapsack
print(dp[len(wt)][rl])