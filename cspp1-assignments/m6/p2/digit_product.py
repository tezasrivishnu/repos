s = input()
l = len(s)
p = 1
for x in s in range(0,len(s)+1,2):
	p = p*s[x]*s[x+1]
print(p)
