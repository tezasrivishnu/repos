s = input()
l = list(s)
i = 1
p = 1
while i+1 <= len(l):
	p *= l[i]*l[i+1]
	i += 2
print(p)