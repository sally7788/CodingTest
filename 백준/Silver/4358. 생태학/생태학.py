import sys
names={}
for line in sys.stdin:
    if line =='\n':
        break
    name=line.rstrip()
    names[name]=names.get(name,0)+1
    
total=sum(names.values())

for name in sorted(names):
    print(f"{name} {names[name]/total*100:.4f}")