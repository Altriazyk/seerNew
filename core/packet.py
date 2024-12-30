from function.Misc import decimal_to_8hex, hex_to_bytearray


class PacketData:
    def __init__(self, length, version, cmdId, userId, result, body):
        self.length = length  # 包头：封包(包头+包体)长度
        self.version = version  # 包头：版本号
        self.cmdId = cmdId  # 包头：命令号
        self.userId = userId  # 包头：米米号
        self.result = result  # 包头：序列号，进行验证封包是否合法
        self.byteBody = hex_to_bytearray(body)
        self.body = body  # 包体
        self.updateLength()

    def updateLength(self):
        self.length = decimal_to_8hex(len(self.getPacket()) // 2)

    def getPacket(self):
        return str(self.length) + str(self.version) + str(self.cmdId) + str(self.userId) + str(self.result) + str(
            self.body)
