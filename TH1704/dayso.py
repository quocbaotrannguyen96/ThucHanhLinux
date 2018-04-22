n = int(input("Nhap n: "))
def inn(n):
	i=1
	while i <= n:
		print(i)
		i+=1
def tongchan(n):
	t=0
	i=1
	while i <=n:
		if(i%2==0):
			t+=i
			i+=1
		else:
			i+=1	
	print "Tong cac phan tu chan: %d" %t
inn(n)
tongchan(n)
