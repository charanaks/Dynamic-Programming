#Minimum Number of steps Taken to convert s1 to s2 or viceversa
s1=input()
s2=input()
dp=[[0 for i in range(len(s2)+1)]for j in range(len(s1)+1)]
for i in range(len(s1)+1):
    for j in range(len(s2)+1):
        if i==0:
            dp[i][j]=j
        elif j==0:
            dp[i][j]=i
        elif s1[i-1]==s2[j-1]:
            dp[i][j]=dp[i-1][j-1]
        else:
            dp[i][j]=1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
print(dp[-1][-1])