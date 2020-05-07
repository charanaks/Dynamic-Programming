s1=input()
s2=input()
result=0
s=""
dp=[[0 for k in range(len(s2)+1)]for l in range(len(s1)+1)]
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1]==s2[j-1]:
            dp[i][j]=1+dp[i-1][j-1]
            if dp[i][j]>result:
                result=dp[i][j]
                ii=i-1
print(result)
while(result>0):
    s=s+s1[ii]
    ii=ii-1
    result=result-1
print(s[::-1])    
