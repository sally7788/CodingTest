def solution(name, yearning, photo):
    answer = []
    dic=dict(zip(name, yearning))
    for p in photo:
        score=0
        for n in p: 
            score+=dic.get(n,0)
        answer.append(score)
    return answer