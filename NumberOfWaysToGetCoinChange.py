l=list(map(int,input().split()))
s=int(input())
dp=[[1 for k in range(s+1)]for m in range(len(l)+1)]
for i in range(s+1):
    dp[0][i]=0
for j in range(len(l)+1):
    dp[j][0]=1
for i in range(1,len(l)+1):
    for j in range(1,s+1):
        if l[i-1]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=dp[i-1][j]+dp[i][j-l[i-1]] #This Line Differs This Problem For Normal Coin Change
print(dp[len(l)][s],dp)