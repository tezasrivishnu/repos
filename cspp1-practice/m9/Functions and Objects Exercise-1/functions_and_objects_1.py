'''
#Exercise : Function and Objects Exercise-1
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 4, 8, 9]
'''
def apply_to_each(l_i, f_i):
    '''
    input: int or float
    returns int or float
    '''
    for i_i in range(len(l_i)):
        l_i[i_i] = f_i(l_i[i_i])
    return l_i
def main():
    '''
    giving input as list
    '''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, abs))
if __name__ == "__main__":
    main()
