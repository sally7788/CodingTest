from collections import defaultdict
def solution(info, edges):
    answer = 0
    graph=defaultdict(list)
    for s,e in edges: 
        graph[s].append(e)
    
    def dfs(sheep, wolf, candidate):
        nonlocal answer
        answer=max(answer, sheep)
        
        for node in candidate:
            nsheep=sheep
            nwolf=wolf
            
            if info[node]==0:
                nsheep+=1
            else:
                nwolf+=1
                
            if nwolf >= nsheep :
                continue
            next_candidate=candidate.copy()
            next_candidate.remove(node) #방문했으니까 삭제 
            next_candidate.extend(graph[node]) # 그 아래 노드로 내려간다 
            
            dfs(nsheep, nwolf, next_candidate)
    dfs(1,0,graph[0][:])
    return answer