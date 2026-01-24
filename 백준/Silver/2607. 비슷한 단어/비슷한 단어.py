import sys

input=sys.stdin.readline
n=int(input())

first=input().strip() 
first_dic={chr(i):0 for i in range(ord('A'), ord('Z')+1)}
for f in first:    
    first_dic[f]=first_dic.get(f,0)+1

answer=0
for _ in range(n-1):
    word=input().strip()
    word_dic={chr(i):0 for i in range(ord('A'), ord('Z')+1)}
    for w in word:
        word_dic[w]=word_dic.get(w,0)+1

    cnt=0
    for i in range(ord('A'), ord('Z')+1):
        cnt+=abs(first_dic[chr(i)]-word_dic[chr(i)])
            
    if cnt <= 2 and abs(len(first)-len(word)) <=1:
        answer+=1
print(answer)