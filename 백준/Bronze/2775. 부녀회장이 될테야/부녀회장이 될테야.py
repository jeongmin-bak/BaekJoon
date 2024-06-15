T = int(input())

for _ in range(T) :
    k = int(input())
    n = int(input())
    
    dp = []
    for i in range(n) :
        dp.append(i+1) #0층 i호 명수 설정
    
    for i in range(1, k+1) :
        for j in range(n) :
            if j>0 :
                dp[j] += dp[j-1] # 현재 층 j호수 = 현재 층 j-1호수 + 전 층 j호수
            else :
                pass # 각 층의 1호는 무조건 1이기 때문에
            
    print(dp[n-1])