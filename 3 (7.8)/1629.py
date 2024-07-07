def multi(a, b, c):
    if b == 1:
        return a % c
    
    temp = multi(a, b // 2, c)
    
    if b % 2 == 1:
        return((temp * temp) % c) * a % c
    else:
        return(temp * temp) % c
    
a, b, c = list(map(int, input().split()))
print(multi(a, b, c))
