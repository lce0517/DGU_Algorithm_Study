from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))

permu = list(permutations(arr, n))
def calculator(li):
    total = 0
    for i in range(len(li)-1):
        total += abs(li[i] - li[i + 1])
    return total

ans = calculator(permu[0])
for li in permu:
    ans = max(ans, calculator(li))
    
print(ans)
