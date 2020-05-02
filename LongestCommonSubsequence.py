s1=input()
s2=input()
result=0
dp=[[0 for k in range(len(s2)+1)]for l in range(len(s1)+1)]
for i in range(len(s1)+1):
    for j in range(len(s2)+1):
        if i==0 or j==0:
            dp[i][j]=0
        elif s1[i-1]==s2[j-1]:
            dp[i][j]=1+dp[i-1][j-1]
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])
print(dp[len(s1)][len(s2)])