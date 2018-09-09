t = float(input())
print(int(t // (360 / 12)), int(t // (360 / 12 / 60)) % 60, int(t // (360 / 12 / 60 / 60)) % 60)
