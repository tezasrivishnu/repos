s = 100
nguess = 0
epsilon = 0.01
low = 0
high = s
ans = (low + high)/2.0
guess = 0

while guess is 0:
	
	print("Is you lucky number" + str(float(ans)) + "?")
	#print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly")
	inp = input()
	if inp == 'h':
		high = float(ans)
		ans = (low + high)/2.0
	elif inp == 'l':
		low = float(ans)
		ans = (low + high)/2.0
	elif inp == 'c': 
		print("your lucky number is ",float(ans))
		guess = 1
	else:
		print("wrong entry")

