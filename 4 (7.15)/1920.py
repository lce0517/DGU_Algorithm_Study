import sys
input = sys.stdin.readline

n = int(input())
n_nums = list(map(int, input().split()))
n_nums.sort()

m = int(input())
m_nums = list(map(int, input().split()))

def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return True
        
        if target < arr[mid]:
            right = mid - 1
        if target > arr[mid]:
            left = mid + 1
            
    return False

for i in range(m):
    if binarySearch(n_nums, m_nums[i]):
        print(1)
    else:
        print(0)
