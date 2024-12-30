from pet.PetInfo import UserPetInfo, RivalPetInfo


class PetBag:
    def __init__(self, param1):
        self.data = param1
        self.firstBag = []
        self.secondBag = []
        self.upDateByOnce()

    def upDateByOnce(self):
        _loc2_ = self.readUnsignedInt(self.data)
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc5_ = UserPetInfo(self.data, True, True, True)
            self.firstBag.append(_loc5_)
            self.data = _loc5_.data
            _loc3_ += 1
        _loc2_ = self.readUnsignedInt(self.data)
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc5_ = UserPetInfo(self.data, True, True, True)
            self.secondBag.append(_loc5_)
            self.data = _loc5_.data
            _loc3_ += 1

    def readUnsignedInt(self, param):
        res = int(param[0:8], 16)
        self.data = self.data[8:]
        return res


class rivalPetBag:
    def __init__(self, param1):
        self.data = param1
        self.bag=[]
        self.GetUserPetInfoById()

    def GetUserPetInfoById(self):
        _loc1_=self.readUnsignedInt(self.data)
        self.readUnsignedInt(self.data)
        for i in range(_loc1_):
            _loc2_=RivalPetInfo(self.data)
            self.data=_loc2_.data
            self.bag.append(_loc2_)


    def readUnsignedInt(self, param):
        res = int(param[0:8], 16)
        self.data = self.data[8:]
        return res
