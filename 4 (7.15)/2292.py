num = int(input())
box = 1
cnt = 1

while num > box:
    box += 6 * cnt
    cnt += 1
    
print(cnt)
