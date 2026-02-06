
n=int(input())
a=list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_val=-10**9
min_val=10**9

def dfs(idx, current, plus, minus,mul,div):
    global max_val, min_val

    if idx==n:
        max_val=max(max_val, current)
        min_val=min(min_val, current)
        return 

    if plus > 0:
        dfs(idx+1, current+a[idx], plus-1, minus, mul, div)
    if minus > 0:
        dfs(idx+1, current-a[idx], plus, minus-1, mul, div)
    if mul > 0:
        dfs(idx+1, current*a[idx], plus, minus, mul-1, div)
    if div > 0:
        if current < 0:
            dfs(idx+1, -(abs(current) // a[idx]), plus, minus, mul, div-1)
        else: dfs(idx+1, current // a[idx], plus, minus, mul, div-1)
dfs(1,a[0],plus,minus,mul,div)

print(max_val)
print(min_val)