m=10000007
l=list(map(int,input().split()))
s=int(input())
dp=[[0 for k in range(s+1)]for m in range(len(l)+1)]
for i in range(s+1):
    dp[0][i]=m
for j in range(len(l)+1):
    dp[j][0]=0
for i in range(1,len(l)+1):
    for j in range(1,s+1):
        if l[i-1]<=j and dp[i][j-l[i-1]]!=m:
            dp[i][j]=min(dp[i-1][j],dp[i][j-l[i-1]]+1)
        else:
            dp[i][j]=dp[i-1][j]
if dp[-1][-1]==m:
    print("0") #not possible
else:
    print(dp[-1][-1])
