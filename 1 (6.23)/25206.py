sum1 = 0
sum2 = 0

rating = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

for _ in range(20):
    sub, sco, gra = input().split()
    if gra == "P":
        continue
    sum1 += float(sco) * rating[gra]
    sum2 += float(sco)
    
print(sum1/sum2)
