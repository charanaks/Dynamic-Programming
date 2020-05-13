t=int(input())
while(t):
    t=t-1
    n=int(input())
    dp=[0]*n
    l=list(map(int,input().split()))
    dp[0]=l[0]
    if n>1:
        dp[1]=max(l[0],l[1])
        for i in range(2,n):
            dp[i]=max(dp[i-1],l[i]+dp[i-2])
    print(dp[n-1])