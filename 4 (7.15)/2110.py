import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = [int(input()) for i in range(n)]
house.sort()

left = 1
right = house[-1] - house[0]

def binarySearch(house, left, right):
    while left <= right:
        mid = (left + right) // 2
        current = house[0]
        cnt = 1
        for i in range(1, n):
            if house[i] >= current + mid:
                cnt += 1
                current = house[i]
        if cnt >= c:
            left = mid + 1
            result = mid
        else:
            right = mid - 1
    return result

print(binarySearch(house, left, right))
