n = int(input())
if n < 10:
    print(n)
else:
    a = n % 10
    n = n // 10
    while n > 0 and a > 0:
        digit = n % 10
        if digit == 0:
            a = 0
        elif digit == 1 or a == 1:
            a *= digit
        else:
            a += digit
        n = n // 10
    print(a)