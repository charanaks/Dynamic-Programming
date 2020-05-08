s=input()
dp=[[0 for i in range(len(s))]for j in range(len(s))]
for i in range(len(s)):
    dp[i][i]=1
for l in range(1,len(s)):
    for i in range(len(s)-l):
        j=i+l
        if s[i]==s[j]:
            dp[i][j]=2+dp[i+1][j-1]
        else:
            dp[i][j]=max(dp[i][j-1],dp[i+1][j])
            
print(dp[0][len(s)-1])