import math
def solution(n, stations, w):
    answer = 0
    # 기존에 빛이 드는 곳과, 빛이 들지 않는 곳을 분리하나 
    # 그리고 빛이 들지 않는 곳을... w칸마다 띄워서 배치 
    no_light=[]
    for i in range(1,len(stations)): 
        leng = (stations[i]-w-1)-(stations[i-1]+w)        
        no_light.append(leng)
    no_light.append(stations[0]-w-1)
    no_light.append(n-(stations[-1]+w))
    
    
    for n in no_light:
        if n <= 0: 
            continue
        else: 
            answer+=math.ceil(n/(2*w+1))
    
    return answer