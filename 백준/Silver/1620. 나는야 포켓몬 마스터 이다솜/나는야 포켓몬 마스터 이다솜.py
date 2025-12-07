n,m=map(int, input().split())
name_dic={}
num_dic={}
for i in range(1,n+1):
    name=input()
    name_dic[name]=i
    num_dic[i]=name

for _ in range(m):
    question=input()
    if question.isdigit():
        idx=int(question)               
        print(num_dic[idx])
    else: 
        print(name_dic[question])