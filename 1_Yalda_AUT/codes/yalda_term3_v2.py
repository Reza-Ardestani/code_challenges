rows = int(input())
init_set = [0]
operations = []
latest3 = 0
kk = 0
for i in range(rows):
	line = input()
	temp_row = line.split(' ')
	for i in range(0, len(temp_row)):
		temp_row[i] = int(temp_row[i])
	operations.append(temp_row)
	if operations[i][0] == 3:
		latest3 = kk
	kk+=1
##  finding the latest operation 3print(latest3
print(latest3)
print(operations)
k = 0
for i in operations:
	if i[0] == 1:
		init_set.append(i[1])
	if i[0] == 2:
		for j in range(len(init_set)):
			init_set[j] = init_set[j] ^ i[1]
	if i[0] == 3:
		print(max(init_set))
	if k + 1> latest3:
		break
	k+=1


