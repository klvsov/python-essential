h, m = input().split()
h = int(h)
m = int(m)

t = 11 * (60 * h + m) % 720
if t != 0:
    t = 720 - t
print(t // 11)
