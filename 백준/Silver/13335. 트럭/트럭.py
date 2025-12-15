import sys
from collections import deque

input = sys.stdin.readline

n,w,l=map(int, input().split())
waiting=list(map(int, input().split()))
bridge=deque([0]*w)
time=0
current_weight=0

while waiting:
    time+=1

    removed_truck = bridge.popleft()
    current_weight-=removed_truck
    
    if current_weight + waiting[0] <=l:
        new=waiting.pop(0)
        bridge.append(new)
        current_weight+=new
    else:
        bridge.append(0)

time+=w
print(time)