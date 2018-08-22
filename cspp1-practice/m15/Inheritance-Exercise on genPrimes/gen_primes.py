#define the gen_primes function here
def genPrimes():
    prime = [2]
    temp = 3
    while True:
        for num in prime:
            count = 0
            if temp%num != 0:
                count += 1
            if count == len(prime):
                prime.append(temp)
            if temp == prime[-1]:
                yield prime[-1]
        temp += 2
def main():
    data=input()
    l=data.split()
    a=int(l[0])
    b=int(l[1])
    primeGenerator = genPrimes()
    for i in range(a):
        p=primeGenerator.__next__()
        if(i%b==0):
            print(p)
    
if __name__== "__main__":
    main()
