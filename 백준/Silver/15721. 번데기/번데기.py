A = int(input())
T = int(input())
find = int(input())  

count = 0   
idx = 0     

# 게임 반복 회차
n = 1
while True:
    
    base = [0, 1, 0, 1]
    for x in base:
        if x == find:
            count += 1
        if count == T:
            print(idx % A)
            exit()
        idx += 1

    # n번 뻔
    for _ in range(n+1):
        if find == 0:
            count += 1
        if count == T:
            print(idx % A)
            exit()
        idx += 1

    # n번 데기
    for _ in range(n+1):
        if find == 1:
            count += 1
        if count == T:
            print(idx % A)
            exit()
        idx += 1

    n += 1
