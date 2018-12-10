queen = input()
horse = input()

qrow = int(queen[1])
hrow = int(horse[1])

cell = []

chess = 'abcdefgh'
q_letter = queen[0]
qcol = chess.find(q_letter) + 1

h_letter = horse[0]
hcol = chess.find(h_letter) + 1

for i in range(1,9):
    for j in range(1,9):
        if (abs(hcol - i) == 2) and (abs(hrow - j) == 1) or (abs(hcol - i) == 1) and (abs(hrow - j) == 2):
            cell.append(str(i)+ " " + str(j))

for i in range(1,9):
    for j in range(1,9):
        if qcol == i or qrow == j or abs(qcol - i) == abs(qrow - j):
            cell.append(str(i)+ " " + str(j))


cell.append(str(hcol)+ " " + str(hrow))
cell.append(str(qcol)+ " " + str(qrow))
cell_queen = str(qcol)+ " " + str(qrow)
cell_horse = str(hcol)+ " " + str(hrow)
s = []
for i in cell:
       if i not in s:
          s.append(i)

s.remove(cell_horse)
s.remove(cell_queen)
print(len(s))

#cell = set(cell)
#cell_horse = set(cell_horse)
#cell_queen = set(cell_queen)
#d1 = cell & cell_horse
#d2 = cell & cell_queen
#res = len(cell) - len(d1) - len(d2)
