# '''
# 1. 몇시간 있었는지 구한다 
#     1-1. records를 반복문으로 받아서 
#         차 번호를 키로 두고 딕셔너리로 구한다. value를 리스트로 구성한다. 
#         리스트 길이가 짝수면 빼면 되고 (여러번 반복되면?)
#         리스트 길이가 홀수면 앞에 것 빼고, 뒤에 것을 23:59분에서 뺀다 
#         [차량번호, 시간] 같이 저장 
# 2. 시간에 따라 가격을 계산한다
# 3. 차량 번호가 작은 자동차부터 return 
# '''
from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    

    time=defaultdict(list)
    for r in records:
        t, num, _ = r.split()
        h,m=map(int,t.split(':'))
        cal_t=h*60+m
        time[num].append(cal_t)
    
    final=[]
    for k,v in time.items():
        length=len(v)
        if length % 2 == 0:
            key_time=sum(v[1+i]-v[i] for i in range(0,length,2))
        else: 
            key_time=sum(v[1+i]-v[i] for i in range(0,length-1,2)) + (23*60+59)-v[-1]
            
        if key_time > fees[0]:
            money=fees[1]+math.ceil((key_time-fees[0])/fees[2])*fees[3]
        else: money=fees[1]
        final.append([k,money])
    s_final=sorted(final, key=lambda x:x[0])
    for num,money in s_final:
        answer.append(money)
    return answer

