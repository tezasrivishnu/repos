'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    num_input = int(input())
    list_input = []
    for _ in range(num_input):
    	list_input.append(input())
    for _ in range(num_input):
    	print(list_input[_])


if __name__ == '__main__':
    main()
