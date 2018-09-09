time_1_h = int(input())
time_1_m = int(input())
time_1_s = int(input())
time_2_h = int(input())
time_2_m = int(input())
time_2_s = int(input())

time_h = time_2_h - time_1_h
time_m = time_2_m - time_1_m
time_s = time_2_s - time_1_s

print(time_h * 3600 + time_m * 60 + time_s)
