'''
#Exercise : Function and Objects Exercise-2
#Implement a function that converts the given testList = [1, -4, 8, -9] into [2, -3, 9, -8]
'''

def apply_to_each(l_i, inc_i):
    '''
    input: int or float
    returns int or float
    '''
    for i_i in range(len(l_i)):
        l_i[i_i] = inc_i(l_i[i_i])
    return l_i
def inc_i(a_i):
	return a_i + 1
def main():
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, inc_i))
if __name__ == "__main__":
    main()
