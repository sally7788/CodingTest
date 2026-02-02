n=int(input())
switch=list(map(int, input().split()))
stu_n=int(input())

for _ in range(stu_n):
    sex, num=map(int, input().split())
    if sex == 1:
        for i in range(n):
            if (i+1) % num == 0:
                switch[i]=1-switch[i]
    else: 
        left, right=num-1, num-1
        
        while left-1>=0 and right+1<n and switch[left-1] == switch[right+1]:
            left-=1
            right+=1
            
        for i in range(left, right+1):
            switch[i]=1-switch[i]

for i in range(n):
    print(switch[i], end=" ")
    if (i+1) % 20 == 0:
        print()