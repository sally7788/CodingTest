from collections import Counter
word=input()
holsu=''
result=''
odd_cnt=0

dic=Counter(word)
dic=sorted(dic.items(), key=lambda x:x[0])


for k,v in dic:
    if v%2==1:
        odd_cnt+=1
        holsu=k
    result+=k*(v//2)

if odd_cnt >1:
    print("I'm Sorry Hansoo")
else:
    print(result+holsu+result[::-1])