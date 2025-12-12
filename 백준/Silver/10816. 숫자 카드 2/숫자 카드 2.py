from collections import Counter
import sys

input=sys.stdin.readline

n=int(input())
dic=Counter(list(map(int,input().split())))
answer=[]
m=int(input())

find_num=list(map(int,input().split()))
for i in range(m):
    answer.append(dic[find_num[i]])

print(*answer)