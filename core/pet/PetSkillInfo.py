class PetSkillInfo:
    def __init__(self, param1):
        if param1!=None:
            self.data = param1
            self._id = self.readUnsignedInt(self.data)
        self.pp = self.readUnsignedInt(self.data)
        if self.pp < 0:
            self.pp = 0

    def readUnsignedInt(self, pram):
        res = int(pram[0:8], 16)
        self.data = self.data[8:]
        return res
