from SinhVien import SV
from SinhVien import Khoa

l = []
l.append(SV("1","Tran Van An ","57"))
l.append(SV("2","Vo Thanh Tan  ","57"))
l.append(SV("3","Ngo Quoc Huy","57"))
l.append(SV("4","Bui Tien Minh ","59"))
l.append(SV("5","Le Quoc Bao ","58"))

for i in l:
    i.xuat()
    
print()

g = []
g.append(Khoa("56","Khoa 56 CNTT"))
g.append(Khoa("57","Khoa 57 CNTT"))
g.append(Khoa("58","Khoa 58 CNTT"))              
g.append(Khoa("59","Khoa 59 CNTT"))

for i in g:
    i.xuat()
            
print()
for i in l:
    if (str(i.getKhoa())=="57"):
        i.xuat()

