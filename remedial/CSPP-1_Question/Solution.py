import re
def main():
	inp = input()
	inp = list(inp)
	if len(inp) == 81:
		print("Given sudoku is solved")
	else:
		lis = []
		i = 0
		temp = []
		for i in range(len(inp)):
			if i%9==0 and i!=0:
				lis.append(temp)		
				temp = []
			temp.append(inp[i])
		lis.append(temp)
		# for i in range(len(lis)):
		# 	print(lis[i])
		# 	print()
		for i in range(len(lis)):
			for j in range(len(lis[0])):
				if lis[i][j] == '.':
					print(sudoku(lis,i,j))
def sudoku(lis,i,j):
	tem = []
	for k in range(len(lis)):
		tem.append(lis[k][j])
	for m in range(len(lis[0])):
		tem.append(lis[i][m])
	if (i >= 0 and i <= 2) and (j >= 0 and j <= 2):
		for x in range(0,3):
			for y in range(0,3):
				tem.append(lis[x][y])
	elif (i >= 0 and i <= 2) and (j >= 3 and j <= 5):
		for x in range(0,3):
			for y in range(3,6):
				tem.append(lis[x][y])
	elif (i >= 0 and i <= 2) and (j >= 6 and j <= 8):
		for x in range(0,3):
			for y in range(6,9):
				tem.append(lis[x][y])
	elif (i >= 3 and i <= 5) and (j >= 0 and j <= 2):
		for x in range(3,6):
			for y in range(0,3):
				tem.append(lis[x][y])
	elif (i >= 3 and i <= 5) and (j >= 3 and j <= 5):
		for x in range(3,6):
			for y in range(3,6):
				tem.append(lis[x][y])
	elif (i >= 3 and i <= 5) and (j >= 6 and j <= 8):
		for x in range(3,6):
			for y in range(6,9):
				tem.append(lis[x][y])
	elif (i >= 6 and i <= 8) and (j >= 0 and j <= 2):
		for x in range(6,9):
			for y in range(0,3):
				tem.append(lis[x][y])
	elif (i >= 6 and i <= 8) and (j >= 3 and j <= 5):
		for x in range(6,9):
			for y in range(3,6):
				tem.append(lis[x][y])
	elif (i >= 6 and i <= 8) and (j >= 6 and j <= 8):
		for x in range(6,9):
			for y in range(6,9):
				tem.append(lis[x][y])
	string = ''.join(tem)
	string = string.replace(".", "")
	string = list(string)
	inti = list(map(int,string))
	whole = [1,2,3,4,5,6,7,8,9]
	numbers = []
	for h in range(len(whole)):
		if whole[h] not in inti:
			numbers.append(whole[h])
	string1 = list(map(str,numbers))
	string1 = ''.join(string1)
	return string1
def notthere(temp):
	# num = []
	# horve = list(set(horve))
	# sq = list(set(sq))
	# print(horve)
	# print(sq)
	# for i in range(len(sq)):
	# 	if sq[i] not in horve:
	# 		num.append(sq[i])
	# return num
	whole = ['1','2','3','4','5','6','7','8','9']
	numbers = []
	for h in range(len(whole)):
		if whole[h] not in temp:
			numbers.append(whole[h])
	return numbers
	
# def hori(lis,i,j):
# 	tem = []
# 	for k in range(len(lis)):
# 		tem.append(lis[k][j])
# 	return tem
# def veri(lis,i,j):
# 	tem = []
# 	for k in range(len(lis)):
# 		tem.append(lis[k][j])
# 	return tem
# def squ(lis,i,j):
# 	tem = []
# 	if (i >= 0 and i <= 2) and (j >= 0 and j <= 2):
# 		for x in range(0,3):
# 			for y in range(0,3):
# 				tem.append(lis[x][y])
# 	elif (i >= 0 and i <= 2) and (j >= 3 and j <= 5):
# 		for x in range(0,3):
# 			for y in range(3,6):
# 				tem.append(lis[x][y])
# 	elif (i >= 0 and i <= 2) and (j >= 6 and j <= 8):
# 		for x in range(0,3):
# 			for y in range(6,9):
# 				tem.append(lis[x][y])
# 	elif (i >= 3 and i <= 5) and (j >= 0 and j <= 2):
# 		for x in range(3,6):
# 			for y in range(0,3):
# 				tem.append(lis[x][y])
# 	elif (i >= 3 and i <= 5) and (j >= 3 and j <= 5):
# 		for x in range(3,6):
# 			for y in range(3,6):
# 				tem.append(lis[x][y])
# 	elif (i >= 3 and i <= 5) and (j >= 6 and j <= 8):
# 		for x in range(3,6):
# 			for y in range(6,9):
# 				tem.append(lis[x][y])
# 	elif (i >= 6 and i <= 8) and (j >= 0 and j <= 2):
# 		for x in range(6,9):
# 			for y in range(0,3):
# 				tem.append(lis[x][y])
# 	elif (i >= 6 and i <= 8) and (j >= 3 and j <= 5):
# 		for x in range(6,9):
# 			for y in range(3,6):
# 				tem.append(lis[x][y])
# 	elif (i >= 6 and i <= 8) and (j >= 6 and j <= 8):
# 		for x in range(6,9):
# 			for y in range(6,9):
# 				tem.append(lis[x][y])
# 	return tem
main()

