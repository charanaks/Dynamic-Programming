#MINIMUM COST TO TRAVEL FROM M[0][0] TO M[-1][-1]
r=int(input())
c=int(input())
x=r
m=[]
dp=[[0 for k in range(c)]for t in range(r)]
while(x):
    x=x-1
    l=list(map(int,input().split()))
    m.append(l)
dp[0][0]=m[0][0]
for i in range(1,r):
    dp[i][0]=dp[i-1][0]+m[i][0]
for i in range(1,c):
    dp[0][i]=dp[0][i-1]+m[0][i]
for i in range(1,r):
    for j in range(1,c):
        dp[i][j]=m[i][j]+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
print(dp[-1][-1])
