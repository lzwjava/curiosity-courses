matrix = [[(i+j*4) for i in range(4)] for j in range(3)]
print(matrix)

t = []
for j in range(3):
  t.append([(i+j*4) for i in range(4)])
print(t)

mt = [[row[j] for row in matrix] for j in range(4)]
print(mt)