a = []

for x in range(1, 7):
    a.append(x**2)
    a.sort(reverse=True)

print(a)

b = [x ** 2 for x in range(1, 7)]

b.sort(reverse=True)

print(b)

# Answer from video -  https://youtu.be/5K08WcjGV6c?t=314
c = []

for x in range(6, 0, -1):
    c.append(x**2)
print(c)

d = [x**2 for x in range(6, 0, -1)]
print(d)
