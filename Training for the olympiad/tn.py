a,b = open('input.txt', 'r').read().split()
a = int(a)
b = int(b)
open('output.txt', 'w').write(str((a % b) * (b % a) + 1))
