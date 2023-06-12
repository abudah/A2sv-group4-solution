n, m = list(map(int, input().split()))

rows = []
columns = []


for i in range(n):
	row = [i for i in input()]
	rows.append(row)

for j in range(m):
	cols = []
	for k in range(n):
		cols.append(rows[k][j])
	columns.append(cols)

answers = []


for i in range(n):
	for j in range(m):
		if rows[i].count(rows[i][j]) == 1 and columns[j].count(rows[i][j]) == 1:
			answers.append(rows[i][j])
print("".join(answers))