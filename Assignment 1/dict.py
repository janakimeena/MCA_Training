n = int(input())
d = {}
for i in range(0,n):
	ip = input().split()
	key = int(ip[0])
	d[key] = ip[1]
val = list(d.keys())
val.sort()
for v in val:
	print(d[v])

