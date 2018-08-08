'''
#Exercise : Function and Objects Exercise-3
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 16, 64, 81]
'''
def applyto_each(l_i, f_i):
    '''
    input: int or float
    returns int or float
    '''
    for i_i in range(len(l_i)):
        l_i[i_i] = square(l_i[i_i])
    return l_i
def square(a_i):
    '''
    calculating square
    '''
    return a_i*a_i
def main():
    '''
    giving input as list
    '''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(applyto_each(list1, square))
if __name__ == "__main__":
    main()
