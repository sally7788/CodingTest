def solution(n, k, cmd):
    prev=[i-1 for i in range(n)]
    next=[i+1 for i in range(n)]
    next[n-1]=-1
    
    deleted=[]
    cur=k
    
    for c in cmd:
        if c[0]=="U":
            x=int(c.split()[1])
            for _ in range(x):
                cur=prev[cur]
        elif c[0]=="D":
            x=int(c.split()[1])
            for _ in range(x):
                cur=next[cur]
        elif c[0]=="C":
            deleted.append((cur, prev[cur], next[cur]))
            
            if prev[cur] != -1:
                next[prev[cur]]=next[cur]
            if next[cur] != -1:
                prev[next[cur]]=prev[cur]
            
            if next[cur] != -1:
                cur=next[cur]
            else: 
                cur=prev[cur]
        else:
            node, p, nxt=deleted.pop()
            
            if p!= -1:
                next[p]=node
            if nxt != -1:
                prev[nxt]=node
            
            prev[node]=p
            next[node]=nxt
    answer=["O"] * n 
    for node, _, _ in deleted:
        answer[node]="X"
    return "".join(answer)
                
            
            
   