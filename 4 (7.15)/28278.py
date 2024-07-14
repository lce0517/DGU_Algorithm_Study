import sys

stack = []

n = int(sys.stdin.readline())

for _ in range(n):
    com = sys.stdin.readline().split()
    
    if com[0] == '1':
        stack.append(com[1])
    elif com[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif com[0] == '3':
        print(len(stack))
    elif com[0] == '4':
        if stack:
            print(0)
        else:
            print(1)
    elif com[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)
