n = int(input())
l = []
for i in range(0,n):
	ip = int(input())
	l.append(ip)
if l[0]>l[1]:
	print(l[0])
for i in range(2,n-1):
	if l[i]>l[i-1] and l[i+1]:
		print(l[i])
if l[n-1]>l[n-2]:
	print(l[n-1])
