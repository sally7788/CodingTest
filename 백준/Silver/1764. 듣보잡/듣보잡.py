n,m=map(int, input().split())
l1,l2=set(), set()
for _ in range(n):
    l1.add(input())

for _ in range(m):
    l2.add(input())


result=l1 & l2

result=sorted(result)
print(len(result))
print('\n'.join(result))