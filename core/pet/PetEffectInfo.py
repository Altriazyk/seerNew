class PetEffectInfo:
    def __init__(self, param1):
        self.data = param1
        self.addArray = []
        self.levelArray = []
        self.args_all={}
        self.itemId = self.readUnsignedInt(self.data)
        self.status = self.readUnsignedByte(self.data)
        self.leftCount = self.readUnsignedByte(self.data)
        self.effectID = self.readUnsignedShort(self.data)
        a1 = self.readUnsignedByte(self.data)
        a1 += self.checkAdd(self.data)
        a2 = self.readUnsignedByte(self.data)
        a2 += self.checkAdd(self.data)
        a3 = self.readUnsignedByte(self.data)
        a3 += self.checkAdd(self.data)
        a4 = self.readUnsignedByte(self.data)
        a4 += self.checkAdd(self.data)
        a5 = self.readUnsignedByte(self.data)
        a5 += self.checkAdd(self.data)
        a6 = self.readUnsignedByte(self.data)
        a6 += self.checkAdd(self.data)
        a7 = self.readUnsignedByte(self.data)
        a7 += self.checkAdd(self.data)
        a8 = self.readUnsignedByte(self.data)
        a8 += self.checkAdd(self.data)
        a=[]
        a.append(a2)
        a.append(a3)
        a.append(a4)
        a.append(a5)
        a.append(a6)
        a.append(a7)
        a.append(a8)
        self.args_all[a1]=a2
        self.args_all[a3] = a4
        self.args_all[a5] = a6
        self.args_all[a7] = a8
        if a2==0 and a3==0 and a4==0 and a5==0 and a6==0:
            self.args=str(a1)+" "+str(0)
        else :
            self.args=str(a1)
            i=6
            while i>=0:
                if a[i]>0:
                    j=0
                    while j<=i:
                        self.args+=" "+str(a[j])
                        j+=1
                    break
                i-=1
        self.args_6=str(a2) + " " + str(a3) + " " + str(a4) + " " + str(a5) + " " + str(a6) + " " + str(a1)
        if self.effectID ==171:
            self.addArray.append(a1)
            self.addArray.append(a2)
            self.addArray.append(a3)
            self.addArray.append(a4)
            self.addArray.append(a5)
            self.addArray.append(a6)
            lv=int(a7)
            self.levelArray.append(lv%16)
            lv-=lv%16
            lv/=16
            self.levelArray.append(lv % 16)
            lv -= lv % 16
            lv /= 16
            self.levelArray.append(lv % 16)
            lv=int(a8)
            self.levelArray.append(lv % 16)
            lv -= lv % 16
            lv /= 16
            self.levelArray.append(lv % 16)
            lv -= lv % 16
            lv /= 16
            self.levelArray.append(lv % 16)


    def checkAdd(self, param1):
        _loc2_ = self.readUnsignedByte(param1)
        if _loc2_:
            return _loc2_ * 256
        return 0

    def readUnsignedByte(self, param):
        res = int(param[0:2], 16)
        self.data = self.data[2:]
        return res

    def readUnsignedInt(self, param):
        res = int(param[0:8], 16)
        self.data = self.data[8:]
        return res

    def readUnsignedShort(self, param):
        res = int(param[0:4], 16)
        self.data = self.data[4:]
        return res
