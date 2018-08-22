#define the gen_primes function here
def genPrimes():
    prime = 2
    while prime>0:
    	if prime(prime):
    		yield prime
    	prime += 1
def prime():
	for num in range(2,n):
		if n/num == 0:
			return False
	return True
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
