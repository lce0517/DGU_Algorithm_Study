d = [int(input()) for _ in range(9)]

for i in range(8):
    for j in range(i + 1, 9):
        if sum(d) - (d[i] + d[j]) == 100:
            m = [d[i], d[j]]
            break
            
d.remove(m[0])
d.remove(m[1])

print('\n'.join(map(str, sorted(d))))
