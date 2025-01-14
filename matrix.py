matrix = []
value = 1
for i in range(5):
    row = []
    for j in range(5):
        row.append(value)
        value += 1
    matrix.append(row)

for row in matrix:
    print(row)