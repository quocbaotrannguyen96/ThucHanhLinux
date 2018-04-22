a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))

def cong(a,b):
	tong = a + b
	print "Tong hai so = %d" %tong
def tru(a,b):
	hieu = a - b
	print "Hieu hai so = %d" %hieu
def nhan(a,b):
	tich = a * b
	print "Tich hai so = %d" %tich
def chia(a,b):
	thuong = a / b
	print "Thuong hai so = %d" %thuong
def luythua(a,b):
	lt=1
	for i in (1,b,1):
		lt*=a
	print "Luy thua = %d" %lt 
def laydu(a,b):
	c = a % b
	print "Chia lay du = %d" %c
cong(a,b)
tru(a,b)
nhan(a,b)
chia(a,b)
luythua(a,b)
laydu(a,b)
