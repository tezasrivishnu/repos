'''
#Exercise : Odd Tuples
#Write a python function oddTuples(aTup) that takes
a some numbers in the tuple as input and returns a tuple
in which contains odd index values in the input tuple
'''
def odd_tuples(atup_i):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    return atup_i[::2]
def main():
    '''
    Giving input as tupple
    '''
    data = input()
    data = data.split()
    a_tup = ()
    for j in range(len(data)):
        a_tup += (data[j],)
    print(odd_tuples(a_tup))
if __name__ == "__main__":
    main()
