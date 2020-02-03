sen = input()
l = sen.split()
for i in range(0,len(l)-1):
	if l[i] >= l[i+1]:
		print('No')
		break
else:
	print('Yes')
