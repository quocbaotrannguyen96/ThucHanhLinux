a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))

def swap(a,b):
	tam = a
	a = b
	b = tam
	print "Hoan doi, so a: %d" %a
	print "Hoan doi, so b: %d" %b
swap(a,b)
