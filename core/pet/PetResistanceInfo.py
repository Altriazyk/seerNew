class PetResistanceInfo:
    def __init__(self, param1):
        self.data = param1
        _loc2_ = self.readUnsignedInt(self.data)
        self.cirt=self.getbitValue(_loc2_,17,16)
        self.cirt_adj=self.getbitValue(_loc2_,1,16)
        _loc2_ = self.readUnsignedInt(self.data)
        self.regular = self.getbitValue(_loc2_, 17, 16)
        self.regular_adj = self.getbitValue(_loc2_, 1, 16)
        _loc2_ = self.readUnsignedInt(self.data)
        self.precent = self.getbitValue(_loc2_, 17, 16)
        self.precent_adj = self.getbitValue(_loc2_, 1, 16)
        _loc3_=1
        self.ctl={}
        while _loc3_<4:
            _loc2_=self.readUnsignedInt(self.data)
            self.ctl["ctl_"+str(_loc3_)+"_idx"]=self.getbitValue(_loc2_,17,8)
            self.ctl["ctl_" + str(_loc3_) ] = self.getbitValue(_loc2_, 9, 8)
            self.ctl["ctl_" + str(_loc3_) + "_adj"] = self.getbitValue(_loc2_, 1, 8)
            _loc3_+=1
        _loc3_=1
        self.weak = {}
        while _loc3_ < 4:
            _loc2_ = self.readUnsignedInt(self.data)
            self.weak["weak_" + str(_loc3_) + "_idx"] = self.getbitValue(_loc2_, 17, 8)
            self.weak["weak_" + str(_loc3_)] = self.getbitValue(_loc2_, 9, 8)
            self.weak["weak_" + str(_loc3_) + "_adj"] = self.getbitValue(_loc2_, 1, 8)
            _loc3_ += 1
        self.resist_all = self.readUnsignedInt(self.data)
        self.resist_state = self.readUnsignedInt(self.data)
        self.red_gem = self.readUnsignedInt(self.data)
        self.green_gem = self.readUnsignedInt(self.data)
        self.reserve = self.readUnsignedInt(self.data)

    def getBit(self, param1, param2):
        return (param1 & 1 << param2 - 1) >> param2 - 1

    def getbitValue(self, param1, param2, param3):
        _loc4_ = 0
        _loc5_ = 0
        while _loc5_ < param3:
            _loc4_ += self.getBit(param1, param2 + _loc5_) * pow(2, _loc5_)
            _loc5_ += 1
        return _loc4_

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
