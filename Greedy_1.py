# 동전
km = list(map(int,input().split()))
k = km[1]
coin = []
for i in range(km[0]):
    coin.append(int(input()))

# coin = [1,5,10,50,100,500,1000,5000,10000,50000]
# k = 4200

def greedyCoin(coin,k):
    total_count = 0 #total
    coin.sort(reverse=True) #오름차순정렬
    for i in coin:
        i_num = k // i  #해당동전갯수
        total_count += i_num #더하기
        k -= i_num*i #빼주기
    return total_count

print(greedyCoin(coin,k))

