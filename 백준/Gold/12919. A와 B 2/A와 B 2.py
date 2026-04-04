s=input()
t=input()

def dfs(t):
    if t==s:
        print(1)
        exit()
    if len(t)<len(s):
        return 0 
    
    if t[-1]=='A':
        dfs(t[:-1])
    if t[0]=="B":
        dfs(t[1:][::-1])


dfs(t)
print(0)