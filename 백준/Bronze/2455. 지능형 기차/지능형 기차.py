train=0
max_train=0
for _ in range(4):
    pin,pout=map(int, input().split())
    if train < 0:
        train=0
    train-=pout
    train+=pin
    max_train=max(max_train, train)

print(max_train)