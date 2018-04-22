class SV:
    mssv=""
    hoten=""
    khoa=""
    def __init__(self,mssv,hoten,khoa):
        self.mssv=mssv
        self.hoten=hoten
        self.khoa=khoa
    def getKhoa(self):
        return self.khoa
    def xuat(self):
        print(self.mssv," ",self.hoten," ",self.khoa)
class Khoa:
    mKhoa=""
    tKhoa=""
    def __init__(self,mKhoa,tKhoa):
        self.mKhoa=mKhoa
        self.tKhoa=tKhoa
    def getMaKhoa(self):
        return self.mKhoa
    def getTenKhoa(self):
        return self.tKhoa
    def xuat(self):
        print(self.mKhoa," ",self.tKhoa)
