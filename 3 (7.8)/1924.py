import calendar
week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

a, b = map(int, input().split())

day = calendar.weekday(2007, a, b)
print(week[day])
