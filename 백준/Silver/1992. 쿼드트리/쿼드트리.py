n=int(input())
graph=[input() for _ in range(n)]

def is_same(x,y,size):
    first=graph[x][y]
    for i in range(x,x+size):
        for j in range(y, y+size):
            if graph[i][j] != first:
                return False
    return True

def quad(x,y,size):
    
    if is_same(x,y,size):
        return graph[x][y]
    
    half=size//2
    return (
        "("
        + quad(x,y,half)
        + quad(x,y+half,half)
        + quad(x+half, y, half)
        + quad(x+half, y+half, half)
        +")"
    )
print(quad(0,0,n))