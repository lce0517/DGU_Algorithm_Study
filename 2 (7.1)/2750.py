N = int(input())
num = []

for i in range(N):
    num.append(int(input()))
num1 = sorted(num)
for i in range(len(num)):
    print(num1[i])
