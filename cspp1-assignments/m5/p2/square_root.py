# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
'''
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991
'''
def main():
	'''
	to find out square root of a number
	using approximation
	'''
	s_i = int(input())
	epsilon_i = 0.01
	guess_i = 0.0
	i_i = 0.1
	while abs(guess_i**2-s_i) >= epsilon_i and guess_i <= s_i:
		guess_i += i_i
	if abs(guess_i**2-s_i) >= epsilon_i:
		print("failed")
	else:
		print(str(guess_i))
if __name__ == "__main__":
	main()
