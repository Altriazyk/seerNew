from .PetSkillInfo import PetSkillInfo
from .PetEffectInfo import PetEffectInfo
from .PetResistanceInfo import PetResistanceInfo


class UserPetInfo:
    def __init__(self, param1, param2, param3, param4):
        self.data = param1.replace(" ", '')
        self.id = self.readUnsignedInt(self.data)
        self.name = self.readUTFBytes(self.data)
        if param2:
            self.generation = self.readUnsignedInt(self.data)
        self.dv = self.readUnsignedInt(self.data)
        self.nature = self.readUnsignedInt(self.data)
        self.abilityType = self.readUnsignedInt(self.data)
        self.level = self.readUnsignedInt(self.data)
        self.exp = self.readUnsignedInt(self.data)
        self.lvExp = self.readUnsignedInt(self.data)
        self.nextLvExp = self.readUnsignedInt(self.data)
        self.hp = self.readUnsignedInt(self.data)
        self.maxHp = self.readUnsignedInt(self.data)
        self.attack = self.readUnsignedInt(self.data)
        self.defence = self.readUnsignedInt(self.data)
        self.s_a = self.readUnsignedInt(self.data)
        self.s_d = self.readUnsignedInt(self.data)
        self.speed = self.readUnsignedInt(self.data)
        self.ev_hp = self.readUnsignedInt(self.data)
        self.ev_attack = self.readUnsignedInt(self.data)
        self.ev_defence = self.readUnsignedInt(self.data)
        self.ev_sa = self.readUnsignedInt(self.data)
        self.ev_sd = self.readUnsignedInt(self.data)
        self.ev_sp = self.readUnsignedInt(self.data)
        self.readUnsignedInt(self.data)
        self.skillNum = 0
        _loc5_ = 0
        self.skillArray = []
        while _loc5_ < 5:
            _loc10_ = PetSkillInfo(self.data[0:16])
            self.data = self.data[16:]
            self.skillArray.append(_loc10_)
            self.skillNum += 1
            _loc5_ += 1
        self.catchTime = self.readUnsignedInt(self.data)
        self.catchMap = self.readUnsignedInt(self.data)
        self.catchRect = self.readUnsignedInt(self.data)
        self.catchLevel = self.readUnsignedInt(self.data)
        self.abilityMark = self.readUnsignedInt(self.data)
        self.skillMark = self.readUnsignedInt(self.data)
        self.commonMark = self.readUnsignedInt(self.data)
        if param3:
            self.commonMarkActived = self.readUnsignedInt(self.data)
        self.effectCount = self.readUnsignedShort(self.data)
        _loc6_ = 0
        self.effectList = []
        while _loc6_ < self.effectCount:
            self.effectList.append(PetEffectInfo(self.data[0:48]))
            self.data = self.data[48:]
            _loc6_ += 1
        self.resistanceinfo = PetResistanceInfo(self.data[0:112])
        self.data = self.data[112:]
        self._skinId = self.readUnsignedInt(self.data)
        self.assistMoveId = self.readUnsignedInt(self.data)
        self.abilityValues = []
        _loc7_ = 0
        while _loc7_ < 3:
            _loc11_ = self.readUnsignedInt(self.data)
            self.abilityValues.append(_loc11_ >> 16 * 0 & 65535)
            self.abilityValues.append(_loc11_ >> 16 * 1 & 65535)
            _loc7_ += 1
        _loc8_ = ["hp", "attack", "defence", "s_a", "s_d", "speed"]
        _loc9_ = 0
        self.base = {}
        self.pvp = {}
        self.pve = {}
        while _loc9_ < 6:
            self.base["base_" + _loc8_[_loc9_] + "_total"] = self.readUnsignedInt(self.data)
            self.pvp["pvp_" + _loc8_[_loc9_] + "_total"] = self.readUnsignedInt(self.data)
            self.pve["pve_" + _loc8_[_loc9_] + "_total"] = self.readUnsignedInt(self.data)
            _loc9_ += 1
        self.base_curHp = self.readUnsignedInt(self.data)
        self.pvp_curHp = self.readUnsignedInt(self.data)
        self.pve_curHp = self.readUnsignedInt(self.data)
        if param4 and False:
            self.sum_favor = self.readUnsignedInt(self.data)
            self.is_favor_locked = self.readUnsignedInt(self.data)

    def readUnsignedInt(self, param):
        res = int(param[0:8], 16)
        self.data = self.data[8:]
        return res

    def readUTFBytes(self, param):
        res = bytes.fromhex(param[0:32]).decode('utf-8')
        self.data = self.data[32:]
        return res

    def readUnsignedShort(self, param):
        res = int(param[0:4], 16)
        self.data = self.data[4:]
        return res


class RivalPetInfo():
    def __init__(self, param):
        self.data = param
        self.catchTime = self.readUnsignedInt(self.data)
        self.userflag = self.readUnsignedInt(self.data)
        self.id = self.readUnsignedInt(self.data)
        self.level = self.readUnsignedInt(self.data)
        self.dev = self.readUnsignedInt(self.data)
        self.nature = self.readUnsignedInt(self.data)
        self.hp = self.readUnsignedInt(self.data)
        self.maxhp = self.readUnsignedInt(self.data)
        self.maxhp_adj = self.readUnsignedInt(self.data)
        self.atk = self.readUnsignedInt(self.data)
        self.atk_adj = self.readUnsignedInt(self.data)
        self.sp = self.readUnsignedInt(self.data)
        self.spatk_adj = self.readUnsignedInt(self.data)
        self.df = self.readUnsignedInt(self.data)
        self.df_adj = self.readUnsignedInt(self.data)
        self.sp_def = self.readUnsignedInt(self.data)
        self.spdef_adj = self.readUnsignedInt(self.data)
        self.spd = self.readUnsignedInt(self.data)
        self.spd_adj = self.readUnsignedInt(self.data)
        self.evlistArray = []
        for i in range(6):
            self.evlistArray.append(self.readUnsignedByte(self.data))
        self.skillArray = []
        n = self.readUnsignedInt(self.data)
        for i in range(5):
            o = self.readUnsignedInt(self.data)
            t = self.readUnsignedInt(self.data)
            if n > i:
                self.skillArray.append({"movID": str(o), "pp": str(t)})
        self.activated_sp_movesArrary = []
        for i in range(6):
            self.activated_sp_movesArrary.append(self.readUnsignedInt(self.data))
        self.mintmarkArray=[]
        for i in range(3):
            self.mintmarkArray.append(self.readUnsignedInt(self.data))
        self.common_slot_activated = self.readUnsignedInt(self.data)
        self.skinId = self.readUnsignedInt(self.data)

    def readUnsignedInt(self, param):
        res = int(param[0:8], 16)
        self.data = self.data[8:]
        return res

    def readUnsignedByte(self, param):
        res = int(param[0:2], 16)
        self.data = self.data[2:]
        return res

    def readUTFBytes(self, param):
        res = bytes.fromhex(param[0:32]).decode('utf-8')
        self.data = self.data[32:]
        return res

    def readUnsignedShort(self, param):
        res = int(param[0:4], 16)
        self.data = self.data[4:]
        return res
