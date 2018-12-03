q = input()
h = input()

q2 = q[1]
h2 = h[1]

chess = 'abcdefgh'
q_letter = q[0]
q1 = chess.find(q_letter) + 1
h_letter = h[0]
h1 = chess.find(h_letter) + 1

count_q = 14

if (q1 == 1) or (q1 == 8) or (q2 == 1) or (q2 == 8):
    count_q += 7
elif (q1 == 2) or (q1 == 7) or (q2 == 2) or (q2 == 7):
    count_q += 9
elif (q1 == 3) or (q1 == 6) or (q2 == 3) or (q2 == 6):
    count_q += 11
elif (q1 == 4) or (q1 == 5) or (q2 == 4) or (q2 == 5):
    count_q += 13

print(count_q)
