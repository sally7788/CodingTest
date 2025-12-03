n=int(input())
a_score=0
b_score=0
prev_time=0
a_time=0
b_time=0
end=48*60

for _ in range(n):
    team, time= input().split()
    time=int(time[:2])*60 + int(time[3:])
    if a_score > b_score: 
        a_time += (time-prev_time)
    elif a_score < b_score:
        b_time += (time-prev_time)

    if team=="1":
        a_score+=1
    else: b_score+=1
    prev_time=time 

if a_score > b_score: 
    a_time += (end-prev_time)
elif a_score < b_score:
    b_time += (end-prev_time)

print(f"{a_time//60:02d}:{a_time%60:02d}")
print(f"{b_time//60:02d}:{b_time%60:02d}")