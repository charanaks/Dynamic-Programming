#code
s=input()
p=input()
dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
dp[0][0]=True
for j in range(1,len(p)+1):
    if p[j-1]=='*':
        dp[0][j]=dp[0][j-1]  #if pattern starts with '*'
for i in range(1,len(s)+1):
    for j in range(1,len(p)+1):
        if p[j-1]=='?' or s[i-1]==p[j-1]:
            dp[i][j]=dp[i-1][j-1]
        elif p[j-1]=='*':
            dp[i][j]=dp[i][j-1] or dp[i-1][j]
        else:
            dp[i][j]=False
print(dp[-1][-1])
