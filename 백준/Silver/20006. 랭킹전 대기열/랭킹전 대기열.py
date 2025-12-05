

p, m = map(int, input().split())

rooms=[]

for _ in range(p):
    level, id=input().split()
    level=int(level)
    places=False

    for room in rooms:
        base=room["min_level"]
        players=room["players"]

        if base-10 <= level <= base+10 and len(players)<m:
            players.append((level,id))
            places=True
            break
    if not places:
        rooms.append({
            "min_level":level,
            "players":[(level,id)]
        })

for room in rooms:
    players=sorted(room["players"], key=lambda x:x[1])

    if len(players)==m:
        print("Started!")
    else:
        print("Waiting!")
    for level,id in players:
        print(level, id)
