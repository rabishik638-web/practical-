def sum(*num):
    s1 = 0
    for i in num:
        s1 = s1 + i
    return s1

r1 = sum(10, 15)
print(r1)

r2 = sum(10, 15, 20)
print(r2)