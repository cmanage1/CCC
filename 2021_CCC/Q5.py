m = int(input())
n = int(input())

k = int(input())
rows = [0]*m
columns = [0]*n
count = 0

for i in range(k):
	line = input().split()
	if line[0]=='R':
		rows[int(line[1])]^=1
	else:
		columns[int(line[1))]^=1

for i in range(m):
	for j in range(n):
		isGold = rows[i]^columns[j]
		if isGold:
			count+=1
			
print(count)

