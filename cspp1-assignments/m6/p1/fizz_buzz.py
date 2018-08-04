'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
def main():
    '''
    In a given number
    we  have to print Fizz for multiples of 3,
    Buzz for mutiples of 5 and
    FizzBuzz for multiples of 5.
    '''
    num_i = int(input())
	i_i = 1
	while i_i <= num_i:
		if (i_i % 3 == 0) and (i_i % 5) == 0:
			print("FizzBuzz")
		elif i_i % 5 == 0:
			print("Buzz")
		elif i_i % 3 == 0:
			print("Fizz")
		else:
			print(i_i)
		i_i += 1
if __name__ == "__main__":
    main()
