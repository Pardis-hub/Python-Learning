n = int(input('Enter number of votes: '))
system = {}
for i in range(n):
    vote = input()
    if vote in system:
        system[vote] += 1
    else:                          #counter[y]=counter.get(y,0)+1
        system[vote] = 1
sorted_keys = sorted(system.keys())
for key in sorted_keys:
    print(key , ': ' , system[key])
