import sys

input=sys.stdin.readline

t=int(input())

for _ in range(t):
    cnt=1
    dic={}
    for _ in range(int(input())):
        _,cloth=input().split()
        dic[cloth]=dic.get(cloth,0)+1

    for _, value in dic.items():
        cnt*=(value+1)
    print(cnt-1)