'''
# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991
'''

def main():
	'''
	here we are finding the square root of a number using
	newton-rampson method
	'''
	s = int(input())
	epsilon = 0.01
	guess = s/2.0
	nguess = 0
	while (guess*guess-s) >= epsilon and guess <= s:
		nguess += 1
		guess = guess - (((guess**2) - s)/(2*guess))
	print(guess)
if __name__ == "__main__":
	main()
