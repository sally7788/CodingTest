from collections import deque
n,k= map(int, input().split())

visited=set()
sec=0
def bfs(x):
    queue=deque([(x,sec)])
    visited.add(x)

    while queue:
        nx, current_time=queue.popleft()

        if nx==k:
            return current_time

        for dx in [nx-1, nx+1, nx*2]:
                        
            if 0 <= dx <= 100000:
                if dx not in visited:                
                    visited.add(dx)
                    queue.append((dx,current_time+1))
print(bfs(n))