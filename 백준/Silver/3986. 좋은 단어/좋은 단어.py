n=int(input())

cnt=0
for _ in range(n):
    word=input()
    l=[]
    for w in word:
        if not l or l[-1] != w:
            l.append(w)
        elif l[-1]==w:
            l.pop()
        
    if not l:
        cnt+=1

print(cnt)