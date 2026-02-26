n=int(input())
street=list(map(int,input().split()))
price=list(map(int,input().split()))

min_price=price[0]
total_price=0

for i in range(n-1):
    min_price=min(min_price, price[i])
    total_price+=min_price*street[i]
print(total_price)